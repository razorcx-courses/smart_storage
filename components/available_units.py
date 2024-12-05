import streamlit as st

def get_all_available_units(df):
        # Display Available Units List
    st.subheader("Available Units")
    with st.container(border=True):
        # Filter for available units
        available_df = df[df['Status'] == 'available'].copy()
        
        # Sort by Unit Type and Unit Number
        available_df['Sort_Unit'] = available_df['Unit'].str.replace('A', '.5').astype(float)
        available_df = available_df.sort_values(['Unit Type', 'Sort_Unit'])
        
        # Drop the temporary sorting column
        available_df = available_df.drop('Sort_Unit', axis=1)
        
        # Apply styling to the dataframe
        def style_status(val):
            colors = {
                'available': 'color: black; background-color: rgba(76, 175, 80, 0.7)'
            }
            return colors.get(val.lower(), '')

        # Create styled dataframe
        styled_df = available_df.style.apply(
            lambda x: [style_status(v) if i == available_df.columns.get_loc('Status') else '' 
                    for i, v in enumerate(x)], axis=1
        )
        
        # Display the styled dataframe
        st.dataframe(
            styled_df,
            hide_index=True,
            use_container_width=True,
            column_config={
                "Unit": st.column_config.TextColumn("Unit", width="small"),
                "Status": st.column_config.TextColumn("Status", width="small"),
                "Unit Type": st.column_config.TextColumn("Unit Type", width="medium"),
                "Monthly Rate": st.column_config.NumberColumn(
                    "Monthly Rate",
                    width="small",
                    format="$%.2f"
                )
            }
        )