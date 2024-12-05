import streamlit as st
import plotly.graph_objects as go

def calculate_unit_stats(df, data):
    # Create figure
    fig = go.Figure()
    
    # Calculate stats for each unit type
    unit_stats = []
    for unit_type in data['Size']:
        units = df[df['Unit Type'] == unit_type]
        rented_units = units[units['Status'] == 'rented']
        
        # Get the index using boolean indexing instead
        monthly_rate = data.loc[data['Size'] == unit_type, 'Monthly_Rate'].iloc[0]
        
        stats = {
            'Unit Type': unit_type,
            'Total Units': len(units),
            'Rented Units': len(rented_units),
            'Monthly Rate': monthly_rate
        }
        unit_stats.append(stats)
    
    # Create bars for unit counts (moved outside the loop)
    fig.add_trace(go.Bar(
        name='Total Units',
        x=[stat['Unit Type'] for stat in unit_stats],
        y=[stat['Total Units'] for stat in unit_stats],
        text=[f"{stat['Total Units']}" for stat in unit_stats],
        textposition='auto',
        marker_color='#444',
        yaxis='y'
    ))
    
    fig.add_trace(go.Bar(
        name='Rented Units',
        x=[stat['Unit Type'] for stat in unit_stats],
        y=[stat['Rented Units'] for stat in unit_stats],
        text=[f"{stat['Rented Units']}" for stat in unit_stats],
        textposition='auto',
        marker_color='#2196F3',
        yaxis='y'
    ))
    
    # Add line for monthly rates
    fig.add_trace(go.Scatter(
        name='Monthly Rate',
        x=[stat['Unit Type'] for stat in unit_stats],
        y=[stat['Monthly Rate'] for stat in unit_stats],
        text=[f"${rate:.2f}" for rate in [stat['Monthly Rate'] for stat in unit_stats]],
        mode='lines+markers+text',
        marker_color='#4CAF50',
        textposition='top center',
        yaxis='y2'
    ))
    
    # Update layout
    fig.update_layout(
        title='Unit Distribution and Monthly Rates',
        barmode='overlay',
        height=500,
        yaxis=dict(
            title='Number of Units',
            side='left'
        ),
        yaxis2=dict(
            title='Monthly Rate ($)',
            side='right',
            overlaying='y',
            tickformat='$,.0f'
        ),
        legend=dict(
            orientation='h',
            yanchor='bottom',
            y=1.02,
            xanchor='right',
            x=1
        )
    )

    return fig

# Display the chart
def get_unit_distribution(df, data):
    st.subheader("Unit Distribution and Rates Analysis")
    with st.container(border=True):
        unit_stats_fig = calculate_unit_stats(df, data)
        st.plotly_chart(unit_stats_fig, use_container_width=True)