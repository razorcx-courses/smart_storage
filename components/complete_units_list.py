import streamlit as st

def get_units_list(df):
    # Display full units list at bottom of page
    st.subheader("Complete Units List")
    # with st.container(border=True):
    # Define the color styling function
    def style_status(val):
        colors = {
            'auction': 'color: black; background-color: rgba(255, 235, 59, 0.7)',    
            'available': 'color: black; background-color: rgba(76, 175, 80, 0.7)',   
            'late': 'color: black; background-color: rgba(255, 152, 0, 0.7)',        
            'locked_out': 'color: black; background-color: rgba(255, 0, 0, 0.7)',    
            'moving_out': 'color: black; background-color: rgba(33, 150, 243, 0.7)', 
            'rented': 'color: black; background-color: rgba(33, 150, 243, 0.7)',     
            'unavailable': 'color: black; background-color: rgba(158, 158, 158, 0.7)'
        }
        return colors.get(val.lower(), '')

    # Clean up the DataFrame before displaying
    def clean_dataframe(df):
        # Drop duplicate Balance column if it exists
        if 'balance' in df.columns and 'Balance' in df.columns:
            df = df.drop('balance', axis=1)
        
        # Combine Phone columns if both exist
        if 'Phone' in df.columns and 'Cell Phone' in df.columns:
            # Use Cell Phone if available, otherwise use Phone
            df['Phone'] = df['Cell Phone'].fillna(df['Phone'])
            df = df.drop('Cell Phone', axis=1)
        
        return df

    # Clean the DataFrame before styling
    df = clean_dataframe(df)

    # Create a styled dataframe
    styled_df = df.style.apply(
        lambda x: [style_status(v) if i == df.columns.get_loc('Status') else '' 
                    for i, v in enumerate(x)], axis=1
    )

    # Configure and display the dataframe
    st.dataframe(
        styled_df,
        hide_index=True,
        use_container_width=True,
        column_config={
            "Unit": st.column_config.TextColumn("Unit", width="small"),
            "Status": st.column_config.TextColumn("Status", width="small"),
            "Unit Type": st.column_config.TextColumn("Unit Type", width="medium"),
            "Customer": st.column_config.TextColumn("Customer", width="medium"),
            "Phone": st.column_config.TextColumn("Phone", width="small"),
            "Email": st.column_config.TextColumn("Email", width="medium"),
            "Balance": st.column_config.NumberColumn(
                "Balance",
                width="small",
                format="$%.2f"
            )
        }
    )