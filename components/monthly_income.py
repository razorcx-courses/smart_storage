import streamlit as st
import plotly.graph_objects as go

# Calculate monthly income per unit type
def calculate_monthly_income(df, data):
    # Filter for rented units only (exclude auction, locked_out, etc)
    rented_units = df[df['Status'] == 'rented']
    
    # Create mapping of unit types to monthly rates
    rate_mapping = dict(zip(data['Size'], data['Monthly_Rate']))
    
    # Calculate total income per unit type
    income_by_type = {}
    for unit_type in data['Size']:
        units_count = len(rented_units[rented_units['Unit Type'] == unit_type])
        monthly_rate = rate_mapping[unit_type]
        total_income = units_count * monthly_rate
        income_by_type[unit_type] = total_income

    # Create figure
    fig = go.Figure()
    fig.add_trace(go.Bar(
        x=list(income_by_type.keys()),
        y=list(income_by_type.values()),
        text=[f'${v:,.2f}' for v in income_by_type.values()],
        textposition='auto',
        marker_color='#2196F3'
    ))

    # Update layout
    fig.update_layout(
        title='Monthly Income by Unit Type',
        xaxis_title='Unit Type',
        yaxis_title='Monthly Income ($)',
        height=400,
        showlegend=False,
        yaxis=dict(tickformat='$,.0f'),
        bargap=0.2
    )
    
    return fig, sum(income_by_type.values())

def get_monthly_income(df, data):
    # Display the chart
    income_fig, total_monthly_income = calculate_monthly_income(df, data)
    st.subheader("Monthly Income Analysis")
    with st.container(border=True):
        col1, col2 = st.columns([3,1])
        with col1:
            st.plotly_chart(income_fig, use_container_width=True)
        with col2:
            st.metric(
                "Total Monthly Income",
                f"${total_monthly_income:,.2f}",
                help="Based on currently rented units"
            )