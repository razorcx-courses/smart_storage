import streamlit as st
import pandas as pd

def get_unit_details(df):
    st.subheader("Unit Details")
    if not df.empty:
        with st.container(border=True):
            # Custom sorting function for unit numbers
            def unit_sort_key(x):
                # Convert unit number to string and handle 'A' suffix
                unit_str = str(x)
                if unit_str.endswith('A'):
                    # For units with 'A', use decimal (e.g., 26A becomes 26.5)
                    return float(unit_str[:-1]) + 0.5
                return float(unit_str)

            # Convert unit numbers and sort them
            unit_numbers = sorted(df['Unit'].unique(), key=unit_sort_key)
            
            selected_unit = st.selectbox("Select Unit Number", unit_numbers)
            
            if selected_unit:
                unit_info = df[df['Unit'] == selected_unit]
                if not unit_info.empty:
                    col1, col2 = st.columns(2)
                    with col1:
                        st.write(f"**Status:** {unit_info['Status'].iloc[0]}")
                        st.write(f"**Unit Type:** {unit_info['Unit Type'].iloc[0]}")
                        if pd.notna(unit_info['Customer'].iloc[0]):
                            st.write(f"**Customer:** {unit_info['Customer'].iloc[0]}")
                    with col2:
                        if pd.notna(unit_info['Balance'].iloc[0]):
                            st.write(f"**Balance:** ${unit_info['Balance'].iloc[0]}")
                        if 'Cell Phone' in unit_info.columns and pd.notna(unit_info['Cell Phone'].iloc[0]):
                            st.write(f"**Phone:** {unit_info['Cell Phone'].iloc[0]}")
            else:
                st.warning("No data available")