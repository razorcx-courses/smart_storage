import streamlit as st
import pandas as pd

def load_data(uploaded_file):
    try:
        if uploaded_file is not None:
            # Read CSV file from uploaded file
            df = pd.read_csv(uploaded_file)
            df['Unit'] = df['Unit'].astype(str)
            
            # Handle Balance column
            if 'Balance' in df.columns:
                df['balance'] = df['Balance'].astype(str).replace(r'[\$,]', '', regex=True)
                df['balance'] = pd.to_numeric(df['balance'], errors='coerce').fillna(0)
            
            return df
        else:
            return pd.DataFrame()
    except Exception as e:
        st.error(f"Error loading data: {str(e)}")
        return pd.DataFrame()
