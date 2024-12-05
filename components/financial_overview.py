import streamlit as st
import plotly.express as px

# Financial Overview
def get_financial_overview(df):
    st.subheader("Financial Overview")
    with st.container(border=True):
        col3, col4 = st.columns([3,2])

        with col3:
            if 'balance' in df.columns:
                outstanding_balance = df[df['balance'] > 0]['balance'].sum()
                st.metric("Total Outstanding Balance", f"${outstanding_balance:,.2f}", delta_color="inverse")
                
                # Color mapping for different statuses
                color_map = {
                    'auction': '#FFEB3B',      # Yellow
                    'available': '#4CAF50',    # Green
                    'late': '#FF9800',         # Orange
                    'locked_out': '#FF0000',   # Red
                    'moving_out': '#2196F3',   # Blue
                    'rented': '#2196F3',       # Blue
                    'unavailable': '#9E9E9E'   # Gray
                }
                
                balance_by_status = df.groupby('Status')['balance'].sum().reset_index()
                balance_fig = px.bar(
                    balance_by_status,
                    x='Status',
                    y='balance',
                    title="Outstanding Balance by Status",
                    labels={'balance': 'Total Balance', 'Status': 'Status'},
                    color='Status',
                    color_discrete_map=color_map
                )
                
                balance_fig.update_traces(
                    texttemplate='$%{y:,.2f}',
                    textposition='auto',
                )
                
                balance_fig.update_layout(
                    showlegend=True,
                    height=400,
                    yaxis_title="Balance ($)",
                    xaxis_title="Status",
                    # plot_bgcolor='white',
                    bargap=0.2
                )
                
                st.plotly_chart(balance_fig, use_container_width=True)

        with col4:
            st.subheader("Units with Outstanding Balance")
            if 'balance' in df.columns:
                outstanding_df = df[df['balance'] > 0][['Unit', 'Status', 'balance']].sort_values('balance', ascending=False)
                
                # Format the balance column as currency
                outstanding_df['balance'] = outstanding_df['balance'].apply(lambda x: f"${x:,.2f}")
                
                # Define the color styling function with black text and 70% opacity backgrounds
                def style_status(val):
                    colors = {
                        'auction': 'color: black; background-color: rgba(255, 235, 59, 0.7)',    # FFEB3B with 70% opacity
                        'available': 'color: black; background-color: rgba(76, 175, 80, 0.7)',   # 4CAF50 with 70% opacity
                        'late': 'color: black; background-color: rgba(255, 152, 0, 0.7)',        # FF9800 with 70% opacity
                        'locked_out': 'color: black; background-color: rgba(255, 0, 0, 0.7)',    # FF0000 with 70% opacity
                        'moving_out': 'color: black; background-color: rgba(33, 150, 243, 0.7)', # 2196F3 with 70% opacity
                        'rented': 'color: black; background-color: rgba(33, 150, 243, 0.7)',     # 2196F3 with 70% opacity
                        'unavailable': 'color: black; background-color: rgba(158, 158, 158, 0.7)' # 9E9E9E with 70% opacity
                    }
                    return colors.get(val.lower(), '')

                # Apply styling to the dataframe
                styled_df = outstanding_df.style.apply(
                    lambda x: [style_status(v) if i == 1 else '' 
                            for i, v in enumerate(x)], axis=1
                )
                
                # Store styled dataframe in session state to maintain styling
                if 'styled_outstanding_df' not in st.session_state:
                    st.session_state.styled_outstanding_df = styled_df
                
                # Display the styled dataframe
                st.dataframe(
                    st.session_state.styled_outstanding_df,
                    hide_index=True,
                    use_container_width=True,
                    column_config={
                        "Unit": st.column_config.TextColumn("Unit", width="small"),
                        "Status": st.column_config.TextColumn("Status", width="small"),
                        "balance": st.column_config.TextColumn("Outstanding Balance", width="medium")
                    }
                )