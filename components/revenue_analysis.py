import streamlit as st
import pandas as pd
import plotly.express as px

## Revenue Analysis
def get_revenue_analysis(df):
    st.subheader("Revenue Analysis")
    with st.container(border=True):
        payment_status = pd.DataFrame({
            'Status': ['Current', 'Late/Locked Out', 'In Auction'],
            'Count': [
                len(df[df['Balance'] == 0]),
                len(df[df['Status'].isin(['late', 'locked_out'])]),
                len(df[df['Status'] == 'auction'])
            ]
        })
        
        payment_fig = px.pie(
            payment_status,
            values='Count',
            names='Status',
            title="Payment Status Distribution"
        )
        st.plotly_chart(payment_fig, use_container_width=True)