"""
Sesión 2 · Vectores y matrices — ¿Qué fruta es más parecida?
Computación Avanzada (ET0197) · Brayan Jiménez Ospina

Cada fruta se representa como un VECTOR de 3 características:
    [peso (g), diámetro (cm), dulzor (0-10)]
La fruta más parecida es la que está a MENOR DISTANCIA EUCLIDIANA del
vector que ingresa el usuario:
    d(a, b) = raíz( (a1-b1)² + (a2-b2)² + (a3-b3)² )

Actividad de clase: se agregó la PERA como nueva fruta conocida y se
calcula también la distancia entre la fruta del usuario y la pera.
"""

import math

import pandas as pd
import streamlit as st

st.title("🍎 ¿Qué fruta es más parecida?")

st.write("Introduce las características de una fruta.")

# Datos de la fruta que queremos analizar
peso = st.number_input("Peso (gramos)", value=180)
diametro = st.number_input("Diámetro (cm)", value=7.0)
dulzor = st.number_input("Dulzor (0 - 10)", value=8.0)

# Convertimos los datos en un vector
fruta_usuario = [peso, diametro, dulzor]

st.write("Vector de tu fruta:", fruta_usuario)

# Frutas conocidas: [peso (g), diámetro (cm), dulzor (0-10)]
manzana = [170, 7.0, 7]
banano = [120, 5.0, 9]
naranja = [200, 8.0, 6]
# NUEVA FRUTA (actividad de clase): una pera mediana pesa ~180 g,
# mide ~6.5 cm de diámetro en su parte más ancha y es bastante dulce.
pera = [180, 6.5, 8]

# Calculamos las distancias

distancia_manzana = math.sqrt(
    (fruta_usuario[0] - manzana[0])**2 +
    (fruta_usuario[1] - manzana[1])**2 +
    (fruta_usuario[2] - manzana[2])**2
)

distancia_banano = math.sqrt(
    (fruta_usuario[0] - banano[0])**2 +
    (fruta_usuario[1] - banano[1])**2 +
    (fruta_usuario[2] - banano[2])**2
)

distancia_naranja = math.sqrt(
    (fruta_usuario[0] - naranja[0])**2 +
    (fruta_usuario[1] - naranja[1])**2 +
    (fruta_usuario[2] - naranja[2])**2
)

# NUEVO: distancia entre la fruta del usuario y la pera
distancia_pera = math.sqrt(
    (fruta_usuario[0] - pera[0])**2 +
    (fruta_usuario[1] - pera[1])**2 +
    (fruta_usuario[2] - pera[2])**2
)

# Mostramos las distancias
st.subheader("Distancias")

st.write("🍎 Manzana:", distancia_manzana)
st.write("🍌 Banano:", distancia_banano)
st.write("🍊 Naranja:", distancia_naranja)
st.write("🍐 Pera:", distancia_pera)

# Buscamos la distancia menor (la pera ya participa en la comparación)
distancias = {
    "🍎 Manzana": distancia_manzana,
    "🍌 Banano": distancia_banano,
    "🍊 Naranja": distancia_naranja,
    "🍐 Pera": distancia_pera
}

# Gráfico de barras: entre más corta la barra, más parecida la fruta
st.bar_chart(pd.Series(distancias, name="Distancia"))

fruta_mas_parecida = min(distancias, key=distancias.get)

st.subheader("Resultado")

st.success(f"La fruta más parecida es: {fruta_mas_parecida}")

st.caption("Computación Avanzada · Sesión 2 · Brayan Jiménez Ospina")
