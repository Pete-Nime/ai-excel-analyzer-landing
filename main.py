import streamlit as st
import pandas as pd

st.set_page_config(page_title="Maintenance Report Analyzer", layout="wide")

st.title("🔧 Maintenance Report Analyzer")

uploaded_file = st.file_uploader("Upload your maintenance Excel file", type=["xlsx", "xls", "csv"])
if uploaded_file:
    try:
        df = pd.read_excel(uploaded_file) if uploaded_file.name.endswith(('.xlsx', '.xls')) else pd.read_csv(uploaded_file)
        st.success("✅ File uploaded successfully!")
        st.subheader("📋 Raw Data")
        st.dataframe(df)

        st.subheader("🛠 Summary Insights")
        st.write(f"Total Records: {len(df)}")
        if 'Issue Type' in df.columns:
            st.write(df['Issue Type'].value_counts())

        if 'Status' in df.columns:
            st.write(df['Status'].value_counts())

    except Exception as e:
        st.error(f"❌ Failed to process file: {e}")
