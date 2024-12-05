import streamlit as st

def get_available_units_by_type(df):
    st.subheader("Available Units By Unit Type")
    with st.container(border=True):
        
        # Filter for available units
        available_df = df[df['Status'] == 'available'].copy()
        
        # Create columns for each unit type
        col1, col2, col3, col4 = st.columns(4)
        
        # Define unit types
        unit_types = [
            '4x8 - 32sq-ft (4 x 8)',
            '6.5x8 - 52sq-ft (6.5 x 8)',
            '10x8 - 80sq-ft (10 x 8)',
            '20x8 - 160sq-ft (20 x 8)'
        ]
        
        # Define monthly rates
        monthly_rates = {
            '4x8 - 32sq-ft (4 x 8)': 99.00,
            '6.5x8 - 52sq-ft (6.5 x 8)': 109.00,
            '10x8 - 80sq-ft (10 x 8)': 139.00,
            '20x8 - 160sq-ft (20 x 8)': 169.00
        }
        
        # Style function for available units
        def style_available(val):
            return 'color: black; background-color: rgba(76, 175, 80, 0.7)'
        
        # Display each unit type in its own column
        for col, unit_type in zip([col1, col2, col3, col4], unit_types):
            with col:
                # Filter for specific unit type
                type_df = available_df[available_df['Unit Type'] == unit_type].copy()
                
                # Sort by unit number
                type_df['Sort_Unit'] = type_df['Unit'].str.replace('A', '.5').astype(float)
                type_df = type_df.sort_values('Sort_Unit')
                
                # Add monthly rate
                type_df['Monthly Rate'] = monthly_rates[unit_type]
                
                # Select and rename columns
                display_df = type_df[['Unit', 'Status', 'Monthly Rate']].copy()
                
                # Create styled dataframe
                styled_df = display_df.style.apply(
                    lambda x: ['background-color: rgba(76, 175, 80, 0.7)'] * len(x), axis=1
                )
                
                # Display unit type as header
                st.subheader(f"{unit_type.split(' - ')[0]}")
                
                # Display dataframe
                st.dataframe(
                    styled_df,
                    hide_index=True,
                    use_container_width=True,
                    column_config={
                        "Unit": st.column_config.TextColumn("Unit", width="small"),
                        "Status": st.column_config.TextColumn("Status", width="small"),
                        "Monthly Rate": st.column_config.NumberColumn(
                            "Rate",
                            width="small",
                            format="$%.2f"
                        )
                    }
                )