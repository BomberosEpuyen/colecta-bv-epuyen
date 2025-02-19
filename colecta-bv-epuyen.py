import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Cargar datos desde Google Sheets
url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vQk8k95jGvq2xP5m5KDw_6TeNHw79mxqUf_2Pek0HHUAGwT49IhSE16aVddy3lnhrqIwXQp34XqttZ2/pub?gid=0&single=true&output=csv"
df = pd.read_csv(url)

# Definir la meta
meta = 75600000  # Costo total para equipar a 33 bomberos
meta_parcial = 54000000  # Punto donde cambia a naranja

# Calcular total recaudado
total_recaudado = df["monto recaudado"].sum()

# Mostrar datos en la app
st.title("Bomberos Voluntarios de Epuyen")
st.title("Avance de la Colecta")

# Mostrar monto recaudado vs meta
st.markdown(
    f"""
    ### 🎯 **Objetivo:** ${meta:,.0f}  
    ### 💰 **Recaudado:** ${total_recaudado:,.0f} ({porcentaje_recaudado:.2f}%)
    """,
    unsafe_allow_html=True
)

# Crear gráfico de barra de progreso
fig, ax = plt.subplots(figsize=(8, 1.5))

# Determinar colores según el avance
if total_recaudado <= meta_parcial:
    ax.barh(["Progreso"], [total_recaudado], color="green", label="Recaudado")
    ax.barh(["Progreso"], [meta - total_recaudado], left=[total_recaudado], color="red", label="Faltante")
else:
    # Parte verde hasta la meta parcial
    ax.barh(["Progreso"], [meta_parcial], color="green")
    # Parte naranja desde la meta parcial hasta el total recaudado
    ax.barh(["Progreso"], [total_recaudado - meta_parcial], left=[meta_parcial], color="orange")
    # Parte roja (lo que falta hasta la meta final)
    ax.barh(["Progreso"], [meta - total_recaudado], left=[total_recaudado], color="red")

# Formatear ejes
ax.set_xlim(0, meta)
ax.set_xlabel("Monto recaudado")
ax.set_xticks([0, meta * 0.25, meta * 0.50, meta * 0.75, meta])
ax.set_xticklabels(["0%", "25%", "50%", "75%", "100%"])
ax.grid(axis="x", linestyle="--", alpha=0.5)

# Ocultar leyenda para evitar cuadro interno
#ax.get_legend().remove()

# Mostrar gráfico en Streamlit
st.pyplot(fig)

# Espacio en blanco
st.markdown("<br>", unsafe_allow_html=True)

# Texto final con contacto y redes sociales
st.markdown(
    """
    **Asociación de Bomberos Voluntarios de Epuyen**  
    Colecta 2025 destinada a la compra de un **Autobomba Forestal 4X4**.  
     **Email de contacto:** [comisiondirectivabvepuyen@gmail.com](mailto:comisiondirectivabvepuyen@gmail.com)  
     **Colaborá aquí:** Alias: **bomberosepuyen**  
     **Seguinos en redes sociales:**  
    - Instagram: [@bomberos_Epuyen](https://www.instagram.com/bomberos_epuyen/?igsh=MXUxNTZiMTVkdjZyeA%3D%3D#)  
    - Facebook: [Bomberos Voluntarios Epuyen](https://www.facebook.com/share/15U5CUYpP8/)  
    """,
    unsafe_allow_html=True
)


