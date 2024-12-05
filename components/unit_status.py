import streamlit as st
import plotly.express as px

def get_unit_status(df):
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Unit Status")
        color_map = {
            'auction': '#FFEB3B',      # Yellow
            'available': '#4CAF50',    # Green
            'late': '#FF9800',         # Orange
            'locked_out': '#FF0000',   # Red
            'moving_out': '#2196F3',   # Blue
            'rented': '#2196F3',       # Blue
            'unavailable': '#9E9E9E'   # Gray
        }
                
        with st.container(border=True):
            status_fig = px.bar(
                df['Status'].value_counts(),
                title="Unit Status Distribution",
                color=df['Status'].value_counts().index,
                labels={'value': 'Count', 'index': 'Status'},
                color_discrete_map=color_map
            )
            st.plotly_chart(status_fig)

    with col2:
        st.subheader("Unit Types")

        with st.container(border=True):
            type_fig = px.pie(
                df,
                names='Unit Type',
                title="Unit Types Distribution",
            )
            st.plotly_chart(type_fig)