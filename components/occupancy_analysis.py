import streamlit as st
import pandas as pd
import plotly.graph_objects as go

# Create occupancy trend visualization
def get_occupancy_analysis(df):
    st.subheader("Occupancy Analysis")
    with st.container(border=True):
        col1, col2 = st.columns(2)
        
        with col1:
            # Create donut chart for unit occupancy status
            occupancy_fig = go.Figure(data=[go.Pie(
                labels=df['Status'].value_counts().index,
                values=df['Status'].value_counts().values,
                hole=.4,
                marker_colors=['#4169E1', '#2E7D32', '#FF0000', '#FFEB3B', 
                            '#9E9E9E', '#2196F3', '#FF9800']
            )])
            occupancy_fig.update_layout(title="Unit Status Distribution")
            st.plotly_chart(occupancy_fig, use_container_width=True)
        
        with col2:
            # Calculate occupancy metrics by unit type
            unit_type_stats = pd.DataFrame({
                'Unit Type': df['Unit Type'].unique(),
                'Total': [len(df[df['Unit Type'] == ut]) for ut in df['Unit Type'].unique()],
                'Occupied': [len(df[(df['Unit Type'] == ut) & (df['Status'] == 'rented')]) 
                            for ut in df['Unit Type'].unique()]
            })
            unit_type_stats['Occupancy Rate'] = (unit_type_stats['Occupied'] / 
                                            unit_type_stats['Total'] * 100).round(1)
            
            st.dataframe(
                unit_type_stats,
                column_config={
                    "Unit Type": st.column_config.TextColumn("Unit Type"),
                    "Total": st.column_config.NumberColumn("Total Units"),
                    "Occupied": st.column_config.NumberColumn("Occupied Units"),
                    "Occupancy Rate": st.column_config.NumberColumn(
                        "Occupancy Rate",
                        format="%.1f%%"
                    )
                },
                hide_index=True
            )