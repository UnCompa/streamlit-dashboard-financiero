import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(
  page_title="Dashboard Financiero",
  page_icon=":bar_chart:",
  layout="wide"
)

data = pd.read_csv("data.csv")

df = pd.DataFrame(data)

df['Balance'] = df['Ingresos'] - df['Egresos']

st.title("Dashboard Financiero Mensual")

col1, col2, col3 = st.columns(3)

col1.metric("Ingreso Total", f"${df['Ingresos'].sum():,.2f}")
col2.metric("Egreso Total", f"${df['Egresos'].sum():,.2f}")
col3.metric("Balance Total", f"${df['Balance'].sum():,.2f}")

st.subheader("Detalles Mensuales")

fig, ax = plt.subplots()
ax.plot(df["Mes"], df["Ingresos"], label="Ingresos", marker='o')
ax.plot(df["Mes"], df["Egresos"], label="Egresos", marker='o')
ax.plot(df["Mes"], df["Balance"], label="Balance", marker='o')
ax.legend()
st.pyplot(fig)

st.subheader("📊 Distribución de gastos")
categorias = ["Comida", "Transporte", "Entretenimiento", "Otros"]
valores = [300, 150, 200, 100]

fig2, ax2 = plt.subplots()
ax2.pie(valores, labels=categorias, autopct="%1.1f%%", startangle=90)
st.pyplot(fig2)