import streamlit as st
import plotly.graph_objects as go

def calculate_actual_vs_potential_income(df, data):
        # Create mapping of unit types to monthly rates
        rate_mapping = dict(zip(data['Size'], data['Monthly_Rate']))
        
        # Initialize dictionaries for actual and potential income
        actual_income = {}
        potential_income = {}
        
        for unit_type in data['Size']:
            # Count units by type and status
            type_units = df[df['Unit Type'] == unit_type]
            rented_units = len(type_units[type_units['Status'] == 'rented'])
            total_units = len(type_units)
            
            # Calculate incomes
            monthly_rate = rate_mapping[unit_type]
            actual_income[unit_type] = rented_units * monthly_rate
            potential_income[unit_type] = total_units * monthly_rate

        # Create figure
        fig = go.Figure()
        
        # Add potential income bars
        fig.add_trace(go.Bar(
            name='Potential Income',
            x=list(potential_income.keys()),
            y=list(potential_income.values()),
            text=[f'${v:,.2f}' for v in potential_income.values()],
            textposition='auto',
            marker_color='#444',
            hovertemplate='Potential Income: $%{y:,.2f}<extra></extra>'
        ))
        
        # Add actual income bars
        fig.add_trace(go.Bar(
            name='Actual Income',
            x=list(actual_income.keys()),
            y=list(actual_income.values()),
            text=[f'${v:,.2f}' for v in actual_income.values()],
            textposition='auto',
            marker_color='#2196F3',
            hovertemplate='Actual Income: $%{y:,.2f}<extra></extra>'
        ))

        # Update layout
        fig.update_layout(
            title='Actual vs Potential Monthly Income by Unit Type',
            xaxis_title='Unit Type',
            yaxis_title='Monthly Income ($)',
            height=500,
            barmode='overlay',
            yaxis=dict(tickformat='$,.0f'),
            bargap=0.2,
            legend=dict(
                orientation='h',
                yanchor='bottom',
                y=1.02,
                xanchor='right',
                x=1
            )
        )
        
        total_actual = sum(actual_income.values())
        total_potential = sum(potential_income.values())
        unrealized_income = total_potential - total_actual
        
        return fig, total_actual, total_potential, unrealized_income
    
def get_income_potential(df, data):
    # Display the chart and metrics
    income_fig, total_actual, total_potential, unrealized = calculate_actual_vs_potential_income(df, data)
    st.subheader("Income Potential Analysis")
    with st.container(border=True):
        col1, col2 = st.columns([3,1])
        with col1:
            st.plotly_chart(income_fig, use_container_width=True, key="Income_Potential_Analysis")
        with col2:
            st.metric(
                "Actual Monthly Income",
                f"${total_actual:,.2f}",
                help="Income from currently rented units"
            )
            st.metric(
                "Potential Monthly Income",
                f"${total_potential:,.2f}",
                help="Income if all units were rented"
            )
            st.metric(
                "Unrealized Income",
                f"${unrealized:,.2f}",
                help="Monthly income lost due to vacancies and non-paying customers",
                delta=f"-${unrealized:,.2f}",
                delta_color="inverse"
            )