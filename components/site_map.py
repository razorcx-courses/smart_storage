import streamlit as st

def get_site_map():
    st.subheader("Storage Facility Site Map")
    with st.container(border=True):
        site_map = "./assets/storage_units_sitemap.png"
        st.image(
            site_map,
            caption="Storage Facility Layout",
            use_container_width=True
        )