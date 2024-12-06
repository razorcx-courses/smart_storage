import streamlit as st
from services.data_loader import load_data

def create_sidebar():
    with st.sidebar:
        st.title("Smart Storage Centre")
        with st.expander("Upload Data"):
            st.session_state.uploaded_file = st.file_uploader(
                "Upload Storage Units CSV file",
                type=['csv'],
                help="Upload your storage units data in CSV format"
            )
            
            st.session_state.units_list = load_data(st.session_state.uploaded_file)
            
            st.warning("Please upload a CSV file")
        
        df = st.session_state.units_list
        
        
        with st.expander("Quick Stats"):
            if not df.empty:
                total_units = len(df)
                occupied_units = len(df[df['Status'] == 'rented'])
                occupancy_rate = (occupied_units / total_units) * 100

                col1, col2 = st.columns(2)
                with col1:
                    with st.container(border=True):
                        st.metric("Total Units", total_units)
                with col2:
                    with st.container(border=True):
                        st.metric("Occupied Units", occupied_units)
                
                with st.container(border=True):
                    st.metric("Occupancy Rate (Paying Customers)", f"{occupancy_rate:.1f}%")
            else:
                st.warning("Please upload a CSV file")
