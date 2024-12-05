import streamlit as st
from services.data_loader import load_data

def create_sidebar():
    # df = pd.read_csv("Units-List.csv")
    st.sidebar.title("Smart Storage Centre")
    with st.expander("Uplodad Data"):
        # st.sidebar.header("Upload Data")
        st.session_state.uploaded_file = st.sidebar.file_uploader(
            "Upload Storage Units CSV file",
            type=['csv'],
            help="Upload your storage units data in CSV format"
        )
        
        st.session_state.units_list = load_data(st.session_state.uploaded_file)
    
    df = st.session_state.units_list
    
    if not df.empty:
        st.sidebar.header("Quick Stats")
        total_units = len(df)
        occupied_units = len(df[df['Status'] == 'rented'])
        occupancy_rate = (occupied_units / total_units) * 100

        with st.sidebar:
            col1, col2 = st.columns(2)
            with col1:
                with st.container(border=True):
                    st.metric("Total Units", total_units)
            with col2:
                with st.container(border=True):
                    st.metric("Occupied Units", occupied_units)
            
            with st.container(border=True):
                st.metric("Occupancy Rate (Paying Customers)", f"{occupancy_rate:.1f}%")