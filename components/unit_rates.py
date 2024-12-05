import streamlit as st
import plotly.graph_objects as go

def get_storage_rates(rates_df):
    # Add Unit Rates section to dashboard
    st.subheader("Storage Unit Rates and Information")
    with st.container(border=True):
        col5, col6 = st.columns(2)

        with col5:
            # Create rate comparison chart
            rate_fig = go.Figure()
            rate_fig.add_trace(go.Bar(
                name='Monthly Rate',
                x=rates_df['Size'],
                y=rates_df['Monthly_Rate'],
                text=rates_df['Monthly_Rate'].apply(lambda x: f'${x:.2f}'),
                textposition='outside',
            ))
            rate_fig.add_trace(go.Bar(
                name='Annual Rate',
                x=rates_df['Size'],
                y=rates_df['Annual_Rate'],
                text=rates_df['Annual_Rate'].apply(lambda x: f'${x:.2f}'),
                textposition='auto',
            ))
            rate_fig.update_layout(
                title='Unit Rates by Size',
                barmode='group',
                height=400
            )
            st.plotly_chart(rate_fig)

        with col6:
            with st.container(border=True):
                # Create interactive unit size selector
                selected_size = st.selectbox(
                    "Select Unit Size for Details",
                    rates_df['Size']
                )
                
                # Display unit details
                unit_info = rates_df[rates_df['Size'] == selected_size].iloc[0]
                st.write("**Monthly Rate:**", f"${unit_info['Monthly_Rate']:.2f}")
                st.write("**Annual Rate:**", f"${unit_info['Annual_Rate']:.2f}")
                st.write("**Description:**")
                st.write(unit_info['Description'])
