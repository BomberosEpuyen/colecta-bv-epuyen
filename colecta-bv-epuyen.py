import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Cargar datos desde Google Sheets
url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vQk8k95jGvq2xP5m5KDw_6TeNHw79mxqUf_2Pek0HHUAGwT49IhSE16aVddy3lnhrqIwXQp34XqttZ2/pub?gid=0&single=true&output=csv"
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

# Crear gráfico de barra de progreso
fig, ax = plt.subplots(figsize=(8, 1.5))

if total_recaudado <= umbral_naranja:
    # Si aún no llegó al umbral, todo es verde
    ax.barh(["Progreso"], [total_recaudado], color="green", label="Recaudado")
    ax.barh(["Progreso"], [meta - total_recaudado], left=[total_recaudado], color="red", label="Faltante")
else:
    # Parte verde hasta el umbral
    ax.barh(["Progreso"], [umbral_naranja], color="green", label="Recaudado hasta 54M")
    # Parte naranja desde el umbral hasta el total recaudado
    ax.barh(["Progreso"], [total_recaudado - umbral_naranja], left=[umbral_naranja], color="orange", label="Recaudado extra")
    # Parte roja faltante hasta la meta
    ax.barh(["Progreso"], [meta - total_recaudado], left=[total_recaudado], color="red", label="Faltante")

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

    los valores en la grafica pueden sufir demora de cara, la meta total representa el valor de 70.000 USD 
    """,
    unsafe_allow_html=True
)

)
