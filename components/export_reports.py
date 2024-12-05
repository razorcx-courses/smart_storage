import streamlit as st

# Export Options
def export_reports(df):
    st.subheader("Export Reports")
    with st.container(border=True):
        report_type = st.selectbox(
            "Select Report Type",
            ["All Units", "Available Units", "Late Payments", "Units in Auction"]
        )
        if st.button("Generate Report"):
            if report_type == "All Units":
                report_df = df
            elif report_type == "Available Units":
                report_df = df[df['Status'] == 'available']
            elif report_type == "Late Payments":
                report_df = df[df['Status'].isin(['late', 'locked_out'])]
            else:
                report_df = df[df['Status'] == 'auction']
                
            st.download_button(
                label="Download Report",
                data=report_df.to_csv(index=False),
                file_name=f"{report_type.lower().replace(' ', '_')}_{datetime.now().strftime('%Y%m%d')}.csv",
                mime="text/csv"
            )