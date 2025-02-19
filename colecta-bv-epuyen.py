import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Cargar datos desde Google Sheets
url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vQk8k95jGvq2xP5m5KDw_6TeNHw79mxqUf_2Pek0HHUAGwT49IhSE16aVddy3lnhrqIwXQp34XqttZ2/pub?gid=0&single=true&output=csv"
df = pd.read_csv(url)

# Definir la meta
meta = 75600000  # Costo total para equipar a 33 bomberos
meta_parcial = 54000000  # Punto donde cambia a amarillo

# Calcular total recaudado y porcentaje
total_recaudado = df["monto recaudado"].sum()
porcentaje_recaudado = (total_recaudado / meta) * 100

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

# Crear gráfico de barra de progreso con degradado
fig, ax = plt.subplots(figsize=(8, 1.5))

if total_recaudado < meta_parcial:
    # Verde hasta el monto recaudado, rojo en lo que falta
    ax.barh(["Progreso"], [total_recaudado], color="green")
    ax.barh(["Progreso"], [meta - total_recaudado], left=[total_recaudado], color="red")
else:
    # Crear un degradado de amarillo a rojo
    num_segments = 20  # Número de segmentos de color
    step = (meta - meta_parcial) / num_segments  # División en segmentos
    colors = np.linspace(0, 1, num_segments)  # Gradiente de color

    start_x = 0  # Inicio de la barra

    for i, color_value in enumerate(colors):
        # Interpolar color de amarillo a rojo
        color = (1, 1 - color_value, 0)  # (Rojo, Verde, Azul) -> Amarillo a Rojo
        segment_width = step if (start_x + step) <= total_recaudado else (total_recaudado - start_x)

        # Dibujar segmento solo si está dentro del monto recaudado
        if segment_width > 0:
            ax.barh(["Progreso"], [segment_width], left=[start_x], color=color)

        start_x += step  # Mover al siguiente segmento

    # Si aún falta dinero, dibujar la parte roja
    if total_recaudado < meta:
        ax.barh(["Progreso"], [meta - total_recaudado], left=[total_recaudado], color="red")

# Formatear ejes
ax.set_xlim(0, meta)
ax.set_xlabel("Monto recaudado")
ax.set_xticks([0, meta * 0.25, meta * 0.50, meta * 0.75, meta])
ax.set_xticklabels(["0%", "25%", "50%", "75%", "100%"])
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
    - Instagram: [@bomberos_Epuyen](https://www.instagram.com/bomberos_epuyen/)  
    - Facebook: [Bomberos Voluntarios Epuyen](https://www.facebook.com/share/15U5CUYpP8/)  
    """,
    unsafe_allow_html=True
)

# Imagen centrada
st.markdown("<p style='text-align: center;'>", unsafe_allow_html=True)
st.image("350984528_1907305209646034_7762816327577734180_n.jpg", caption="Bomberos Voluntarios de Epuyén", width=200)
st.markdown("</p>", unsafe_allow_html=True)

