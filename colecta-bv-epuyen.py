import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Cargar datos desde Google Sheets
url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vQk8k95jGvq2xP5m5KDw_6TeNHw79mxqUf_2Pek0HHUAGwT49IhSE16aVddy3lnhrqIwXQp34XqttZ2/pub?output=csv"
df = pd.read_csv(url)

# Definir la meta
meta = 75600000  # Costo total para equipar a 33 bomberos
umbral_naranja = 54000000  # Punto donde cambia de verde a naranja

# Calcular total recaudado
total_recaudado = df["monto recaudado"].sum()
porcentaje_recaudado = (total_recaudado / meta) * 100
bomberos_equipados = (total_recaudado / meta) * 33  # Conversión a cantidad de bomberos

# Mostrar datos en la app
st.title("Avance de la Colecta")

# Mostrar monto recaudado vs meta
st.markdown(
    f"""
    ### 🎯 **Objetivo:** ${meta:,.0f}  
    ### 💰 **Recaudado:** ${total_recaudado:,.0f} ({porcentaje_recaudado:.2f}%)
    """,
    unsafe_allow_html=True
)

# Crear gráfico de barra de progreso con comparación
fig, ax = plt.subplots(figsize=(8, 2))

if total_recaudado <= umbral_naranja:
    ax.barh(["Recaudado"], [total_recaudado], color="green", label="Recaudado")
    ax.barh(["Recaudado"], [meta - total_recaudado], left=[total_recaudado], color="red", label="Faltante")
else:
    ax.barh(["Recaudado"], [umbral_naranja], color="green", label="Recaudado hasta 54M")
    ax.barh(["Recaudado"], [total_recaudado - umbral_naranja], left=[umbral_naranja], color="orange", label="Recaudado extra")
    ax.barh(["Recaudado"], [meta - total_recaudado], left=[total_recaudado], color="red", label="Faltante")

# Barra extra para representar la meta total como referencia
ax.barh(["Objetivo"], [meta], color="gray", alpha=0.3, label="Meta Total")

# Formatear ejes
ax.set_xlim(0, meta)
ax.set_xlabel("Monto recaudado")
ax.set_xticks([0, meta * 0.25, meta * 0.50, meta * 0.75, meta])
ax.set_xticklabels(["0%", "25%", "50%", "75%", "100%"])
ax.legend()
ax.grid(axis="x", linestyle="--", alpha=0.5)

# Mostrar gráfico en Streamlit
st.pyplot(fig)

# Espacio en blanco
st.markdown("<br>", unsafe_allow_html=True)

# Texto final con contacto y redes sociales
st.markdown(
    """
    **Asociación de Bomberos Voluntarios de Epuyen**  
    Colecta 2025 destinada a la compra de un **Autobomba Forestal 4X4**.  
    📧 **Email de contacto:** [comisiondirectivabvepuyen@gmail.com](mailto:comisiondirectivabvepuyen@gmail.com)  
    💳 **Colaborá aquí:** Alias: **bomberosepuyen**  
    📲 **Seguinos en redes sociales:**  
    - Instagram: [@bomberos_Epuyen](https://www.instagram.com/bomberos_epuyen/?igsh=MXUxNTZiMTVkdjZyeA%3D%3D#)  
    - Facebook: [Bomberos Voluntarios Epuyen](https://www.facebook.com/share/15U5CUYpP8/)  
    """,
    unsafe_allow_html=True
)


