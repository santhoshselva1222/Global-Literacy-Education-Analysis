
import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Global Literacy & Education Trends",
    layout="wide"
)

@st.cache_data
def load_data():
    return pd.read_excel("global_education_featured.xlsx")

df = load_data()

st.title("GLOBAL LITERACY & EDUCATION TRENDS")
st.subheader("An Analytical Study | 1990–2020")

st.sidebar.header("Filters")

countries = ["All Countries"] + sorted(
    df["Entity"].dropna().unique().tolist()
)

country = st.sidebar.selectbox("Select Country", countries)

if country != "All Countries":
    df = df[df["Entity"] == country]

years = sorted(df["Year"].dropna().unique())
selected_years = st.sidebar.slider(
    "Select Year Range",
    int(min(years)),
    int(max(years)),
    (int(min(years)), int(max(years)))
)

df = df[
    (df["Year"] >= selected_years[0]) &
    (df["Year"] <= selected_years[1])
]

col1, col2, col3 = st.columns(3)

col1.metric(
    "Average GDP Per Capita",
    f"{df['GDP_Per_Capita'].mean():,.2f}"
)

col2.metric(
    "Average Literacy Rate",
    f"{df['Literacy_Rate'].mean():.2f}%"
)

col3.metric(
    "Average Years of Schooling",
    f"{df['Average_Years_Schooling'].mean():.2f}"
)

st.subheader("Year-wise Average GDP Per Capita")
st.line_chart(
    df.groupby("Year")["GDP_Per_Capita"].mean()
)

st.subheader("Year-wise Average Literacy Rate")
st.line_chart(
    df.groupby("Year")["Literacy_Rate"].mean()
)

st.subheader("Year-wise Average Years of Schooling")
st.line_chart(
    df.groupby("Year")["Average_Years_Schooling"].mean()
)

st.subheader("Year-wise Youth Literacy Gender Gap")
st.line_chart(
    df.groupby("Year")["Literacy_Gender_Gap"].mean()
)

st.caption("Data Source: Our World in Data")
