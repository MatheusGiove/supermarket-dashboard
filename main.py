import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Supermarket Dashboard",
    page_icon="🛒",
    layout="wide",
)

df = pd.read_csv("data/supermarket_sales.csv", sep=";",
                decimal=",", index_col=0, parse_dates=["Date"])


# Criando o filtro de mês
df["Month"] = df["Date"].apply(lambda x: f"{str(x.year)}-{x.month}")
month = st.sidebar.selectbox("Mês:", df["Month"].unique())
df_filtered = df[df["Month"] == month]



# Criando o layout da página
col1, col2 = st.columns(2)
col3, col4, col5 = st.columns(3)



# Faturamento por dia e por cidade
fig_date = px.bar(df_filtered, x="Date", y="Total",
                color="City", title="Faturamento por dia")
col1.plotly_chart(fig_date, use_container_width=True)



# Faturamento por produto
fig_prod = px.bar(df_filtered, x="Date", y="Product line",
                color="City", title="Faturamento por produto", orientation="h")
col2.plotly_chart(fig_prod, use_container_width=True)



# Faturamento por cidade
city_total = df_filtered.groupby("City")["Total"].sum().reset_index()
fig_city = px.bar(city_total, x="City", y="Total", title="Faturamento por filial")
col3.plotly_chart(fig_city, use_container_width=True)



# Faturamento por tipo de pagamento
fig_payment = px.pie(df_filtered, values="Total", names="Payment", title="Faturamento por tipo de pagamento")
col4.plotly_chart(fig_payment, use_container_width=True)



# Avaliação média por cidade
city_avg = df_filtered.groupby("City")["Rating"].mean().reset_index()
fig_rating = px.bar(city_avg, x="City", y="Rating", title="Avaliação média por cidade")
col5.plotly_chart(fig_rating, use_container_width=True)
