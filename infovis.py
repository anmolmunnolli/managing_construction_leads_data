import streamlit as st
import pandas as pd
import plotly.express as px

@st.cache_data
def load_data():
    file_path = 'construction_companies.csv'  
    df = pd.read_csv(file_path)
    return df

df = load_data()

# Sidebar Filters
st.sidebar.header("Author: Anmol Munnolli (ID: 2001404468)")
st.sidebar.header("Filters")
selected_year = st.sidebar.slider("Select Year", int(df["founded_year"].min()), int(df["founded_year"].max()), int(df["founded_year"].max()))
filtered_df = df[df["founded_year"] <= selected_year]

# Geospatial Heatmap
st.subheader("Lead Distribution Map")
fig_map = px.scatter_mapbox(filtered_df, lat="latitude", lon="longitude", hover_name="company_name", 
                            color_discrete_sequence=["red"], zoom=3, mapbox_style="open-street-map")
st.plotly_chart(fig_map)

# Temporal Trend Line Chart
st.subheader("Leads Over Time")
time_series = df.groupby("founded_year").size().reset_index(name="lead_count")
fig_time = px.line(time_series, x="founded_year", y="lead_count", markers=True, title="Lead Generation Trend")
st.plotly_chart(fig_time)

st.write("### Insights")
st.write("- The geospatial heatmap shows high lead concentrations in specific regions.")
st.write("- The temporal trend line reveals growth trends in lead generation over the years.")
