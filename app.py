import os
import streamlit as st
import pandas as pd
import plotly.express as px
from google.cloud import bigquery

st.set_page_config(page_title="Global Education Dashboard", layout="wide")
st.title("🎓 Education Performance Tracker")

project_id = os.getenv("GCP_PROJECT_ID", "tactile-anthem-485519-v6")
client = bigquery.Client(project=project_id)

@st.cache_data
def load_data():
    # Points to your brand new dbt-transformed table!
    query = "SELECT * FROM `tactile-anthem-485519-v6.production.wide_education`"
    return client.query(query).to_dataframe()

df = load_data()

# Tile 1: Bar Chart
st.subheader("Global Literacy Rates")
fig_bar = px.bar(df.sort_values("literacy_rate", ascending=False).head(20), 
                 x="country_name", y="literacy_rate", color="literacy_rate")
st.plotly_chart(fig_bar, use_container_width=True)

# Tile 2: Line Chart
st.subheader("Spending Trends")
selected = st.selectbox("Select Country", df['country_name'].unique())
country_df = df[df['country_name'] == selected]
st.line_chart(country_df.set_index('year')['govt_expenditure'])