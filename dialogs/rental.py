import streamlit as st
from pydantic import BaseModel, EmailStr, Field, ValidationError
from models.customer import Customer

@st.dialog("New Storage Unit Rental")
def create_new_rental():
    df = st.session_state.units_list
    data = st.session_state.unit_specs
    
    # Get available units from the main DataFrame
    available_units = df[df['Status'] == 'available'][['Unit', 'Unit Type']].sort_values('Unit')
    
    # Store form data in session state
    if 'rental_data' not in st.session_state:
        st.session_state.rental_data = {}
    
    with st.form("rental_form"):
        # Unit Selection Section
        st.subheader("Unit Selection")
        selected_size = st.selectbox(
            "Select Unit Size",
            options=data['Size'],
            key="size_select"
        )
        
        print(available_units)
        
        # Filter available units based on selected size (exact match)
        filtered_units = available_units.loc[available_units['Unit Type'] == selected_size].copy()
        
        # Sort units numerically, handling units with 'A' suffix
        if not filtered_units.empty:
            filtered_units['Sort_Unit'] = filtered_units['Unit'].str.replace('A', '.5').astype(float)
            filtered_units = filtered_units.sort_values('Sort_Unit')
            filtered_units_list = filtered_units['Unit'].tolist()
        else:
            filtered_units_list = ['No units available']
        
        unit = st.selectbox(
            "Select Available Unit",
            options=filtered_units_list,
            key="unit_select",
            disabled=filtered_units.empty
        )
        
        # Get rate and display unit information
        unit_index = data['Size'].index(selected_size)
        monthly_rate = data['Monthly_Rate'][unit_index]
        annual_rate = data['Annual_Rate'][unit_index]
        
        # Display unit details in a container
        with st.container():
            st.info(data['Description'][unit_index])
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
            phone = st.text_input(
                "Phone Number", 
                placeholder="(250) 555-1234",
                help="Format: (XXX) XXX-XXXX"
            )
            email = st.text_input(
                "Email",
                placeholder="example@email.com"
            )
            
        with col2:
            address = st.text_input(
                "Street Address",
                placeholder="123 Main Street"
            )
            city = st.text_input("City")
            province = st.text_input(
                "Province",
                max_chars=2,
                help="Two letter province code (e.g., BC)"
            ).upper()
            postal_code = st.text_input(
                "Postal Code",
                placeholder="V1H 2X3",
                help="Format: A1A 1A1"
            ).upper()
            
        # Payment Information
        st.subheader("Payment Details")
        deposit = st.number_input(
            "Security Deposit",
            value=50.0,
            step=10.0,
            min_value=0.0,
            help="Minimum security deposit required: $50.00"
        )
        
        # Submit Button
        submitted = st.form_submit_button(
            "Submit Rental Agreement",
            disabled=filtered_units.empty or unit == 'No units available',
            use_container_width=True
        )
        
        if submitted:
            try:
                # Create customer object
                customer = Customer(
                    unit_number=unit,
                    first_name=first_name,
                    last_name=last_name,
                    phone=phone,
                    email=email,
                    address=address,
                    city=city,
                    province=province,
                    postal_code=postal_code,
                    unit_type=selected_size,
                    monthly_rate=monthly_rate,
                    deposit_paid=deposit
                )
                
                # Store in session state
                st.session_state.rental_data = {
                    "customer": customer.model_dump(),
                    "unit": unit
                }
                st.rerun()
                
            except ValidationError as e:
                st.error(f"Validation Error: {str(e)}")
            except Exception as e:
                st.error(f"Error processing rental agreement: {str(e)}")