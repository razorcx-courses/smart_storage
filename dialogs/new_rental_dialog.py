import streamlit as st
import pandas as pd
from pydantic import ValidationError
from models.customer import Customer

def update_available_units():
    unit_type = st.session_state.selected_unit_type
    available = st.session_state.available_units_by_type.get(unit_type, [])
    st.session_state.available_units = available

@st.dialog("New Rental Agreement")
def show():
    units_list = pd.read_csv('data/units-list.csv')
    unit_specs = pd.read_csv('data/unit-specs.csv')

    unit_types = unit_specs['Size'].tolist()
    available_units = units_list[units_list['Status'] == 'available']
    
    if 'selected_unit_type' not in st.session_state:
        st.session_state.selected_unit_type = unit_types[0]
    if 'available_units_by_type' not in st.session_state:
        st.session_state.available_units_by_type = available_units.groupby('Unit Type')['Unit'].apply(list).to_dict()
    if 'available_units' not in st.session_state:
        st.session_state.available_units = []
    if 'rental_data' not in st.session_state:
        st.session_state.rental_data = {}
    
    update_available_units()

    st.title("Storage Unit Rental Form")

    selected_unit_type = st.selectbox(
        "Select Unit Type (Size)", 
        unit_types,
        key='selected_unit_type',
        on_change=update_available_units,
        index=0
    )

    with st.form("rental_form"):
        # Unit Selection Section
        st.subheader("Unit Selection")
        
        if st.session_state.available_units:
            filtered_units = pd.DataFrame({'Unit': st.session_state.available_units})
            filtered_units['Sort_Unit'] = filtered_units['Unit'].str.replace('A', '.5').astype(float)
            filtered_units = filtered_units.sort_values('Sort_Unit')
            filtered_units_list = filtered_units['Unit'].tolist()
            
            selected_unit_number = st.selectbox(
                "Select Available Unit Number", 
                filtered_units_list
            )
        else:
            st.write("No units available for the selected type.")
            selected_unit_number = None

        # Display unit details
        unit_index = unit_types.index(selected_unit_type)
        monthly_rate = unit_specs['Monthly_Rate'][unit_index]
        annual_rate = unit_specs['Annual_Rate'][unit_index]

        with st.container():
            st.info(unit_specs['Description'][unit_index])
            col_rate1, col_rate2 = st.columns(2)
            with col_rate1:
                st.metric("Monthly Rate", f"${monthly_rate:.2f}")
            with col_rate2:
                st.metric("Annual Rate", f"${annual_rate:.2f}")

        # Customer Information Section
        st.subheader("Personal Information")
        col1, col2 = st.columns(2)

        with col1:
            first_name = st.text_input("First Name", key="first_name")
            last_name = st.text_input("Last Name", key="last_name")
            phone = st.text_input("Phone Number", placeholder="(250) 555-1234", help="Format: (XXX) XXX-XXXX")
            email = st.text_input("Email", placeholder="example@email.com")

        with col2:
            address = st.text_input("Street Address", placeholder="123 Main Street")
            city = st.text_input("City")
            province = st.text_input("Province", max_chars=2, help="Two letter province code (e.g., BC)").upper()
            postal_code = st.text_input("Postal Code", placeholder="V1H 2X3", help="Format: A1A 1A1").upper()

        # Payment Information
        st.subheader("Payment Details")
        deposit = st.number_input("Security Deposit", value=50.0, step=10.0, min_value=0.0, help="Minimum security deposit required: $50.00")

        submitted = st.form_submit_button("Submit Rental Agreement", use_container_width=True, disabled=True)

        if submitted and selected_unit_number:
            try:
                customer = Customer(
                    unit_number=selected_unit_number,
                    first_name=first_name,
                    last_name=last_name,
                    phone=phone,
                    email=email,
                    address=address,
                    city=city,
                    province=province,
                    postal_code=postal_code,
                    unit_type=selected_unit_type,
                    monthly_rate=monthly_rate,
                    deposit_paid=deposit
                )

                st.session_state.rental_data = {
                    "customer": customer.model_dump(),
                    "unit": selected_unit_number
                }
                st.success(f"Rental agreement submitted for Unit Type: {selected_unit_type} and Unit Number: {selected_unit_number}")
                st.rerun()

            except ValidationError as e:
                st.error(f"Validation Error: {str(e)}")
            except Exception as e:
                st.error(f"Error processing rental agreement: {str(e)}")