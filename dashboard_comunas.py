import streamlit as st
from PIL import Image
import time
#import SessionState

     

### Config
st.set_page_config(
    page_title="Comunas estudiantes Ingenieria y Ciencias, UDP",
    layout="wide"
)

### HEADER
st.title('Comunas de los colegios de los estudiantes de la Facultad de Ingenieria y Ciencias de la UDP, entre 2000 y 2016')

year_list = (x for x in range(2000,2017))


year_choice = st.sidebar.select_slider("Elige el año",options=year_list)
st.write('Mayor tamaño del circulo indica una mayor proporción de estudiantes que provienen de colegios de la comuna')
im = Image.open(f"mapa_comunas_{year_choice}.png")
st.image(im)






