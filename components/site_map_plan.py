import streamlit as st
import pandas as pd
import plotly.graph_objects as go

def get_site_map_plan():
    # Load the unit coordinates and status data
    units_coords = pd.read_csv('data/site-map.csv')
    units_status = pd.read_csv('data/units-list.csv')

    # Ensure proper column names
    units_coords = units_coords.rename(columns={'unit': 'Unit'})

    # Convert Unit column to string in both dataframes to handle units with 'A' suffix
    units_coords['Unit'] = units_coords['Unit'].astype(str)
    units_status['Unit'] = units_status['Unit'].astype(str)

    # Merge the data
    units_data = pd.merge(units_coords, units_status[['Unit', 'Status']], on='Unit', how='left')

    # Define color mapping (lowercase keys for consistency)
    color_mapping = {
        'auction': 'yellow',
        'available': 'green',
        'late': 'blue',
        'lien': 'orange',
        'locked_out': 'red',
        'moving_out': 'pink',
        'pending': 'beige',
        'pre-lien': 'orange',
        'rented': 'blue',
        'reserved': 'lightblue',
        'unavailable': 'darkgray'
    }

    # Create the plot
    fig = go.Figure()

    # Add squares for each unit
    for _, unit in units_data.iterrows():
        fig.add_shape(
            type="rect",
            x0=unit['x'], 
            y0=unit['y'],
            x1=unit['x'] + 1, 
            y1=unit['y'] + 1,
            fillcolor=color_mapping[unit['Status'].lower()],
            line=dict(color='black', width=1),
        )
        
        # Add unit numbers as text - using str() directly without int() conversion
        fig.add_annotation(
            x=unit['x'] + 0.5,
            y=unit['y'] + 0.5,
            text=str(unit['Unit']),  # Remove the int() conversion
            showarrow=False,
            font=dict(size=8)
        )

    # Update layout
    fig.update_layout(
        showlegend=False,
        plot_bgcolor='white',
        width=1000,
        height=600,
        xaxis=dict(
            range=[-1, 50],
            showgrid=False,
            zeroline=False,
            showticklabels=False
        ),
        yaxis=dict(
            range=[-1, 15],
            showgrid=False,
            zeroline=False,
            showticklabels=False,
            scaleanchor='x',
            scaleratio=1
        )
    )

    st.title('Storage Unit Map')
    st.plotly_chart(fig)

    # Add legend
    st.write("## Legend")
    cols = st.columns(len(color_mapping))
    for i, (status, color) in enumerate(color_mapping.items()):
        with cols[i]:
            st.markdown(
                f'<div style="background-color: {color}; padding: 10px; '
                f'text-align: center; border: 1px solid black;">{status}</div>',
                unsafe_allow_html=True
            )