import streamlit as st
import pandas as pd
import plotly.graph_objects as go

def get_unit_availability(df, rates_df):
       # Add unit availability analysis
    st.subheader("Unit Availability")
    with st.container(border=True):
        size_availability = pd.DataFrame({
            'Size': rates_df['Size'],
            'Available': [
                len(df[df['Unit Type'] == size][df['Status'] == 'available'])
                for size in rates_df['Size']
            ],
            'Total': [
                len(df[df['Unit Type'] == size])
                for size in rates_df['Size']
            ]
        })

        # Create a mapping dictionary for unit types
        unit_type_mapping = {
            '4x8 - 32sq-ft (4 x 8)': rates_df['Size'][0],
            '6.5x8 - 52sq-ft (6.5 x 8)': rates_df['Size'][1],
            '10x8 - 80sq-ft (10 x 8)': rates_df['Size'][2],
            '20x8 - 160sq-ft (20 x 8)': rates_df['Size'][3]
        }

        # Calculate availability with exact string matching
        size_availability = pd.DataFrame({
            'Size': rates_df['Size'],
            'Available': [
                len(df[df['Unit Type'].str.strip() == size][df['Status'] == 'available'])
                for size in unit_type_mapping.keys()
            ],
            'Total': [
                len(df[df['Unit Type'].str.strip() == size])
                for size in unit_type_mapping.keys()
            ]
        })

        # Create availability chart
        avail_fig = go.Figure()

        # Add available units bar
        avail_fig.add_trace(go.Bar(
            name='Available',
            x=size_availability['Size'],
            y=size_availability['Available'],
            text=size_availability['Available'],
            textposition='auto',
            marker_color='#2E7D32'
        ))

        # Add total units bar
        avail_fig.add_trace(go.Bar(
            name='Total Units',
            x=size_availability['Size'],
            y=size_availability['Total'],
            text=size_availability['Total'],
            textposition='auto',
            marker_color='rgba(158, 158, 158, 0.5)'
        ))

        # Update layout
        avail_fig.update_layout(
            title='Unit Availability by Size',
            barmode='overlay',
            height=400,
            showlegend=True,
            xaxis_title="Unit Size",
            yaxis_title="Number of Units",
            bargap=0.2
        )

        st.plotly_chart(avail_fig)

        # Calculate potential revenue using the mapping
        potential_revenue = sum(
            df[df['Status'] == 'available']['Unit Type'].map(
                dict(zip(unit_type_mapping.keys(), rates_df['Monthly_Rate']))
            )
        )

    if not df.empty:
        with st.sidebar:
            with st.container(border=True):
                st.metric(
                "Potential Monthly Revenue from Available Units",
                f"${potential_revenue:,.2f}"
                )