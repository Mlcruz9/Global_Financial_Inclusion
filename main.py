
import streamlit as st
import pandas as pd
from functions import home, avances_digitales, mujer, educacion, tendencias_digitales, bancarizacion, conclusion

# Creamos la configuración de la página, y el título
st.set_page_config(page_title='Incertidumbre y digitalización', layout='wide', page_icon='chart_with_upwards_trend')

menu = st.sidebar.selectbox(label='Seleccione una opción:', options=('Home', 'Rasgos generales', 'Prioridades a día de hoy', 'Conclusión'))

if menu == 'Home':
    home()

if menu == 'Rasgos generales':

    st.header('La expansión de opciones financieras en el mundo')
    st.write('La última década ha visto un aumento considerable de la población bancarizada a nivel mundial, alcanzando los niveles más \
        altos en la historia. A pesar de que la globalización unió el mercado mundial hace ya más de 100 años, el alcance de \
        herramientas financieras fiables y escalables no ha sido una opición global hasta que la digitalización ha abierto vías que han \
        lanzado la escalabilidad de estos instrumentos a las regiones más remotas.')
    rasgos = st.radio(label='Miremos a los datos, distingamos por regiones:', options=('Bancarización: en un vistazo', 'Avances derivados de la digitalización'))

    if rasgos == 'Bancarización: en un vistazo':
        bancarizacion()

    if rasgos == 'Avances derivados de la digitalización':
        avances_digitales()


if menu == 'Prioridades a día de hoy':

    st.header('Prioridades a día de hoy')
    st.write('La digitalización representa una oportunidad global para ofrecer servicios financieros que aporten estabilidad a los \
        hogares y reduzcan la vulnerabilidad. A pesar de los avances en la última década, es necesario poner el foco en poblaciones \
        con mayor situación de dependencia para lograr una mayor autonomía y libertad.')
    tendencias_digitales()
    prioridad = st.radio(label='Poblaciones estratégicas:', options=('Mujer', 'Población con menor acceso a la educación'))
    
    if prioridad == 'Mujer':
        mujer()

    if prioridad == 'Población con menor acceso a la educación':
        educacion()

if menu == 'Conclusión':
    conclusion()

