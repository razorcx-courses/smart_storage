import streamlit as st
import pandas as pd
from sidebar.sidebar import create_sidebar
from dialogs.rental import create_new_rental
from components.unit_status import get_unit_status
from components.financial_overview import get_financial_overview
from components.income_potential import get_income_potential
from components.export_reports import export_reports
from components.unit_details import get_unit_details
from components.site_map import get_site_map
from components.unit_rates import get_storage_rates
from components.unit_availability import get_unit_availability
from components.complete_units_list import get_units_list
from components.available_units import get_all_available_units
from components.available_units_by_type import get_available_units_by_type
from components.occupancy_analysis import get_occupancy_analysis
from components.revenue_analysis import get_revenue_analysis
from components.monthly_income import get_monthly_income
from components.unit_distribution import get_unit_distribution
# from components.site_map_plan import get_site_map_plan

from components.collapse import collapse

st.set_page_config(page_title="Storage Facility Dashboard", layout="wide")

if "uploaded_file" not in st.session_state:
    st.session_state.uploaded_file = None
if "units_list" not in st.session_state:
    st.session_state.units_list = pd.DataFrame()
if "unit_specs" not in st.session_state:
    st.session_state.unit_specs = pd.DataFrame()
    
create_sidebar()
    
st.title("Storage Facility Dashboard")

df = st.session_state.units_list

st.session_state.unit_specs = pd.read_csv("./data/unit-specs.csv")
data = st.session_state.unit_specs

# --- Test Components ---
# collapse()

# --- WIP ----
# Main app code
# if "rental_data" not in st.session_state:
#     if st.button("New Rental Agreement"):
#         create_new_rental()
# else:
#     # Process the rental data
#     rental_data = st.session_state.rental_data
# --- WIP ----

# Create DataFrame for unit rates
rates_df = pd.DataFrame(data)
    
if not df.empty:
    get_unit_status(df)
    get_financial_overview(df)
    get_income_potential(df, data)
    col1_report, col2_report = st.columns([2,2])
    with col1_report:
        export_reports(df)
    with col2_report:
        get_unit_details(df)
    get_site_map()
    get_storage_rates(data)
    get_unit_availability(df, data)
    get_units_list(df)
    get_all_available_units(df)
    get_available_units_by_type(df)
    get_occupancy_analysis(df)
    get_revenue_analysis(df)
    get_monthly_income(df, data)
    get_unit_distribution(df, data)
    # get_site_map_plan() # this only sort of worked.  used o1-preview to create csv site plan coordinates.
    
else:
    st.info("Upload a CSV file to view the dashboard")
    


