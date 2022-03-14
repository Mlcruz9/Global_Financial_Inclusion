
from pickle import TRUE
import streamlit as st
from plotly.offline import init_notebook_mode, iplot, plot
import plotly.express as px
import plotly as py
init_notebook_mode(connected=True)
import plotly.graph_objs as go
from sklearn.datasets import load_iris, load_boston
import matplotlib.pyplot as plt
import statsmodels.api as sm
import seaborn as sns
import pandas as pd
import numpy as np
import plotly.express as px

from variables import df, df2017, df2014, df2011

import warnings
warnings.filterwarnings("ignore")


# HOME

def home():
    
    st.title('La digitalización de las finanzas: una oportunidad para reducir la pobreza')

    st.subheader('Análisis exploratorio de datos \n \n Análisis del Global Findex: Base de datos sobre la inclusión financiera en el mundo \n\n Elaborado por Gonzalo Villalón Fornés ')
    st.image('boat-market-marquee-1600x900.jpg', caption='La educación financiera capacita a las personas, reduciendo situaciones de vulnerabilidad y dependencia')
    st.markdown('*El presente trabajo analiza los datos aportados por Global Findex sobre los niveles de desbancarización en el mundo, \
        con un énfasis especial en los parámetros comunes de aquellos países donde está creciendo la inclusión financiera. \
        Un análisis inicial de los resultados en los distintos años (2011, 2014, 2017) indica una clara tendencia a la \
        expansión de servicios financieros formales de forma sistemática en todas las regiones geográficas estudiadas. \
        Una observación más precisa encuentra pruebas a favor de la hipótesis de que la digitalización ha \
        supuesto un avance firme hacia una mayor accesibilidad de herramientas financieras en zonas remotas. No obstante, \
        para lograr una expansión de servicios financieros a las poblaciones más vulnerables, es indispensable compaginar estos \
        esfuerzos con educación financiera, de tal modo que les garantice el acceso a herramientas financieras que brinden las dosis \
        correctas de disciplina, seguridad, flexibilidad e incentivos.*')

    st.header('Una oportunidad histórica, y una responsabilidad')
    st.subheader('La digitalización se presenta como una oportunidad para lograr medios financieros \
            al alcance de las comunidades más remotas y menos pudientes')
    st.write('Porcentaje de población bancarizada en el mundo (Global Findex - 2017):')
    bar_orth = st.checkbox('Incluir nombres de los países sobre el mapa')
    
    if bar_orth:
        fig_orth = px.scatter_geo(df2017, lon='Longitude (average)', lat='Latitude (average)', color='Economic status',
                        hover_name='Account (% age 15+)', 
                        size='Account (% age 15+)', 
                         text='Entity',
                        #  animation_frame="Year",
                        projection="orthographic"
                        )
        fig_orth.show()
        st.plotly_chart(fig_orth)
    
    else:
        fig_orth_1 = px.scatter_geo(df2017, lon='Longitude (average)', lat='Latitude (average)', color='Economic status',
                        hover_name='Account (% age 15+)', 
                        size='Account (% age 15+)', 
                        #  text='Entity',
                        #  animation_frame="Year",
                        projection="orthographic"
                        )
        fig_orth_1.show()
        st.plotly_chart(fig_orth_1)

    with st.expander('Descripción'):
        st.write('En este mapa se puede apreciar el porcentaje de personas bancarizadas por país. El tamaño de cada burbuja está en proporción \
            al porcentaje de bancarización. En cuanto al color de las burbujas, se ha optado por cuatro colores que distingue según el nivel de\
            renta entre ingresos altos ("high income"), medio altos ("upper middle income"), medo bajos ("lower middle income") \
            e ingresos bajos ("low income"), acorde a la clasificación del Banco Mundial.')

    st.write('De un simple vistazo se puede apreciar una correlación positiva entre el porcentaje de población bancarizada y el nivel económico \
        de cada país, por ambas variables a día de hoy están correlacionadas. No obstante, el acceso a instrumentos financieros debe ser \
        independiente al nivel de ingresos, pues no se trata de la cantidad de recursos de los que dispone una familia, si no de la calidad en su gestión.')

    st.subheader('¿Por qué la inclusión financiera debe ser una prioridad mundial para aliviar la pobreza?')
    st.markdown('Para los hogares bajo el umbral de la pobreza, la vida financiera está generalmente marcada por la incertidumbre. \
        Los ingresos que generan son pequeños y, a menudo, irregulares e impredecibles. \
        Además, la mayoría de sus socios financieros no son tan fiables como les gustaría. Cuando la necesidad aprieta, \
        es posible que los prestamistas no tengan fondos para prestar en ese preciso momento, o que quien custodia el dinero no \
        puedan devolver sus ahorros. Los clubes de ahorro, tan comunes en zonas remotas, pueden disolverse debido a una mala gestión, \
        malentendidos o accidentes que les suceden a los miembros. El dinero custodiado en casa se puede perder, robar o desperdiciar \
        en gastos triviales. La población más vulnerable merece algo mejor. **¿Podría ser, entonces, que la digitalización acerque servicios financieros \
        confiables, lo que supondría el primer servicio globalmente confiable del que puedan servirse los pobres del mundo?**')
    st.write('Una estrategia a nivel nacional para garantizar que cada individuo tenga acceso una cuenta bancaria podría ser el \
        primer paso hacia un sector de servicios financieros inclusivo. Promover el alcance de una cuenta bancaria, incluso si no \
        ayudara a los hogares más excluídos a pedir prestado, seguramente mejoraría su acceso a un lugar seguro para ahorrar y una forma \
        más sencilla y económica de gestionar los ingresos y gastos.')
    st.write('Ante esta importancia de una inclusión financiera global, hasta esta última decada no ha sido posible su logro debido \
        al alto coste del desarrollo de una infraestructura física bancaria, cuyo coste se aleja del estilo de vida, el nivel de ingresos, \
        y los flujos de efectivo de la población con rentas más impredecibles e irregulares. Sin embargo, la digitalización se presenta \
        como una oportunidad para lograr servicios financieros adecuados para lidiar con estos flujos de ingresos bajos e irregulares \
         (Daryl Collins, 2008).')
    st.markdown('Collins, D., Morduch, J., Rutherford, S., Ruthven, O. (2008). *Portfolios of the Poor: How the World\'s Poor Live on $2 a Day*. Princeton, NJ: Princeton University Press.')    
    
    with st.expander('¿Sabías qué....? '): 
        st.write('El Banco Graamen es una institución microfinanciera que comenzó otorgando pequeños créditos a la población desbancarizada de menores ingresos. \
            El Banco Mundial estudió el impacto de la inclusión financiera promovida por este banco, concluyendo que un 55% de las personas \
            que recibieron el microcrédito salieron del umbral de la pobreza.')
    
    st.subheader('Global Findex')
    with st.expander('¿Cuál es la base del presente análisis?'): 
        st.write('La base de datos Global Findex supone la recogida de información más completa \
        a nivel mundial sobre cómo los mayores de 15 años ahorran, solicitan préstamos, realizan pagos, gestionan el riesgo y \
        cómo atienden financieramente ante emergencias. \n\n Cabe señalar que el objetivo de estos \
        esfuerzos de investigación es favorecer un conocimiento más profundo sobre las distintas estrategias financieras \
        que utilizan las personas a lo largo del mundo.')
    with st.expander('¿A quién agradecemos la disponibilidad de los datos sobre la inclusión financiera global?'): 
        st.write('La base de datos Global Findex es un recurso desarrollado por \
            el equipo de Global Findex bajo el respaldo del Grupo de Investigaciones sobre Desarrollo \
            del Banco Mundial y de la Fundación Bill y Melinda Gates, con la colaboración de Gallup, Inc..')
    with st.expander('¿Cómo han sido recogidos los datos del Global Findex?'): 
        st.write('Tras este recurso hay un trabajo muy elaborado en el que han participado más de 150,000 personas mayores de 15 años \
            , representando una muestra significativa a nivel nacional en más de 148 países. Los datos han sido recogidos en el\
            2011, 2014 y 2017, y están centrados en lograr una comprension mayor sobre las situaciones de vulnerabilidad \
            financiera en el mundo, de tal modo que sirva tanto a gobiernos como a la iniciativa privada como marco para la acción.')
        st.write('El informe del año 2017 incluye como novedad cuestiones sobre tecnología digital, teléfonos móviles e internet, aspectos \
            esenciales en la inclusión financiera.')
    with st.expander('¿Dónde puedo encontrar la base de datos Global Findex?'): 
        st.write('Demirgüç-Kunt, Asli, Leora Klapper, Dorothe Singer, Saniya Ansar, and Jake Hess. 2018. The Global \
            Findex Database 2017: Measuring Financial Inclusion and the Fintech Revolution. Washington, D.C: Banco Mundial.')
        st.write('Base de datos accesible en: https://globalfindex.worldbank.org/index.php/#data_sec_focus.')

    
    st.subheader('Datos utilizados para el presente análisis')
    with st.expander('Otros datos utilizados en el análisis:'):
        st.write('Se han consultado las siguientes bases de datos:\n\
- Acceso a electricidad en el mundo. Incluye datos de 1990 a 2019. Unidad de medida: porcentaje de población por país (incluye 170 países). Fuente: Banco Mundial (World Development Indicators - World Bank (2021.07.30)). Extraído de https://data.worldbank.org/indicator/EG.ELC.ACCS.ZS.\n\
- Acceso a la educación en el mundo. Se incluyen dos datasets, distinguiendo el acceso a la educación por parte de hombres adultos y de mujeres adultas. Datos del Banco Mundial, facilitados por un usuario de GitHub: https://github.com/cllocc/DAND_project_2 (los datos sin tratar están accesibles en https://databank.worldbank.org/EdStats_Indicators_Report/id/c755d342#).\n\
- Ratio de alfabetismo en el mundo. Incluye datos de mayores de 15 años, en porcentaje de población por país. Son datos proporcionados por UNICEF con fecha de abril del año 2021. Extraído de https://data.unicef.org/topic/education/learning-and-skills/.\n\
- Acceso global a internet. Son datos del año 2017, expresados en porcentaje de población por país. Son datos proporcionados por la ONU, y tratados por https://data.worldbank.org/indicator/IT.NET.USER.ZS.\n\
- Acceso a teléfonos móviles. Son datos del año 2018, expresados en porcentaje de población por país. Extraído de https://data.worldbank.org/indicator/IT.CEL.SETS.P2. Hay más información al respecto en https://www.itu.int/en/ITU-D/Statistics/Pages/stat/default.aspx.\n\
- Datos de población mundial por país. Se extraaen del Banco Mundial. Accesibles en: https://data.worldbank.org/indicator/SP.POP.TOTL.\n\
- Datos sobre la posición geográfica de los países: https://gist.githubusercontent.com/tadast/8827699/raw/3cd639fa34eec5067080a61c69e3ae25e3076abb/countries_codes_and_coordinates.csv')
        st.write('Para acceder al dataframe tratado, consultar en: https://github.com/gonzalovf1996/Global_Financial_Inclusion')



# RASGOS GENERALES

def bancarizacion():

    st.subheader('Así ha sido el crecimiento de la bancarización en el mundo en la última década:')
    tipo_map_nat = st.select_slider(
        'Selecciona año a visualizar',
        options=['año 2011', 'año 2014', 'año 2017'])
   
    if tipo_map_nat == 'año 2011':
        st.write('Población (%, +15 años) bancarizada en el año 2011')
        st.write('Promedio mundial por país: ', round(df2011['Account (% age 15+)'].mean()*100,2), '%')
        fig_nat_11 = px.scatter_geo(df2011, lon='Longitude (average)', lat='Latitude (average)', 
                            # color='Economic status',
                            hover_name='Entity', 
                            size='Account (% age 15+)', 
                            #  text='Entity',
                            #  animation_frame="Year",
                            projection="natural earth"
                            )
        fig_nat_11.show()
        st.plotly_chart(fig_nat_11)            
        
    if tipo_map_nat == 'año 2014':
        st.write('Población (%, +15 años) bancarizada en el año 2014')
        st.write('Promedio mundial por país: ', round(df2014['Account (% age 15+)'].mean()*100,2), '%')
        fig_nat_14 = px.scatter_geo(df2014, lon='Longitude (average)', lat='Latitude (average)', 
                    # color='Economic status',
                     hover_name='Entity', 
                     size='Account (% age 15+)', 
                    #  text='Entity',
                    #  animation_frame="Year",
                     projection="natural earth" # projection="orthographic"
                     )
        fig_nat_14.show()
        st.plotly_chart(fig_nat_14)            

    if tipo_map_nat == 'año 2017':
        st.write('Población (%, +15 años) bancarizada en el año 2017')
        st.write('Promedio mundial por país: ', round(df2017['Account (% age 15+)'].mean()*100,2), '%')
        fig_nat_17 = px.scatter_geo(df2017, lon='Longitude (average)', lat='Latitude (average)', 
                            # color='Economic status',
                            hover_name='Entity', 
                            size='Account (% age 15+)', 
                            #  text='Entity',
                            #  animation_frame="Year",
                            projection="natural earth"
                            )
        fig_nat_17.show()
        st.plotly_chart(fig_nat_17)   
    
    # Descripción general del crecimiento de la bancarización en la última década
    st.write('Los resultados de los datos aportados por el Global Findex revelan que en el año 2017 el 69% de adultos tenían acceso a una cuenta \
        bancaria en el mundo (promedio de bancarización por país de 62%), lo que supone 18 puntos porcentuales más que en el año 2011, cuando la media mundial \
        del número de adultos con acceso a cuenta bancaria era de 51% (promedio de bancarización por país de 47%).\n\nEs relevante observar \
        las estadísticas a nivel país, el cual nos permite aprender de las estrategias de bancarización seguidas por cada unidad política.')

    st.subheader('Crecimiento anual por región')
    st.image('FS-china-boy-on-bike-780.jpg', caption='La expansión de internet ha facilitado el acceso a servicios financieros en zonas remotas')


    # Descripción crecimiento anual por regiones
    st.write('Crecimiento de la población bancarizada por región:')
    st.text('- África subsahariana: 22.57% de su población se ha bancarizado en la última década')
    st.text('- Europa del Este y centro asiático (excluyendo países de renta alta): 19.03% de su población se ha bancarizado en la última década')
    st.text('- Sur asiático: 17.5% de su población se ha bancarizado en la última década')
    st.text('- Latinoamérica y el Caribe (excluyendo países de renta alta): 15.08% de su población se ha bancarizado en la última década')
    st.text('- Oriente Medio y norte de África: 12.65% de su población se ha bancarizado en la última década')
    st.text('- Asia del este y Pacífico: 11.17% de su población se ha bancarizado en la última década')
    st.text('- Países de rentas altas: 7.77% de su población se ha bancarizado en la última década')
    #print(round( df2017[df['Region']=='Middle East & North Africa (excluding high income)']['Account (% age 15+)'].mean()*100 - df2011[df['Region']=='Middle East & North Africa (excluding high income)']['Account (% age 15+)'].mean()*100,2))

    fig_supoer_reg = px.histogram(df, x="Region", y='Account (% age 15+)',hover_name = "Entity", color='Region',
            histfunc='avg',
            animation_frame= 'Year')
    fig_supoer_reg.update_layout(transition = {'duration': 2000})
    fig_supoer_reg.show()
    st.plotly_chart(fig_supoer_reg) 

    st.write('El crecimiento es significativo en cada una de las regiones del mundo. Por ello, esta evidencia apoya la hipótesis de que \
        la década anterior se caracterizó por un crecimiento elevado de las opciones financieras, coincidiendo con un crecimiento \
        de la digitalización en el mundo de una forma sin precedentes.')




def avances_digitales():

    st.subheader('La digitalización de las finanzas: respuesta ante la exclusión financiera en el mundo')
    st.write('Es lógico pensar que la infraestructura de servicios financieros existente debe fijarse en lugares más conectados \
        y de mejores instituciones para ofrecer estos servicios. No obstante, es la población con pronósticos más inciertos y \
        menor acceso a servicios financieros la que más necesidad tiene de estos. De hecho, los datos proporcionados por el Global Index\
        indican que en zonas más remotas ha aumentado su bancarización considerablemente gracias a nuevas tecnologías.')

    st.image('IMG_0420_rdax_782x521s.jpg', caption='Las herramientas de pago móvil están estrechamente relacionadas al aumento de la inclusión financiera a poblaciones aisladas')

    st.subheader('La expansión de servicios financieros tecnológicos durante la década pasada ha supuesto un proceso de transformaciones en la gestión de las finanzas del hogar.')  
    
    st.write('Tanto la expansión del uso de internet como de la telefonía móvil está totalmente relacionada con los niveles de \
        población bancarizada en cada una de las regiones del mundo.')
    tipo_giint = st.select_slider('Relación entre los niveles bancarización y...',
                options=['Uso de internet', 'Tenencia de dispositivos móviles'])
    if tipo_giint == 'Uso de internet':
        fig_0 = px.scatter(
            df2017[['Region','Entity','Individuals using the Internet (% of population)','Access to electricity (% of population)','Cell phones (per 100 people)','Account (% age 15+)', 'Population']],
            x='Account (% age 15+)',
            y='Individuals using the Internet (% of population)',
            title='Relación entre el acceso a internet y el acceso a instrumentos financieros, por país',
            size='Population',
                size_max=70,
                trendline='ols',
                trendline_scope='overall', # trace
                hover_name='Entity',
                color='Region')
        fig_0.show()
        st.plotly_chart(fig_0)

    if tipo_giint == 'Tenencia de dispositivos móviles':
        fig_2 = px.scatter(
            df2017[['Region','Entity','Individuals using the Internet (% of population)','Access to electricity (% of population)','Cell phones (per 100 people)','Account (% age 15+)', 'Population']],
            x='Account (% age 15+)',
            y='Cell phones (per 100 people)',
            title='Relación entre la tenencia de dispositivos móviles y el acceso a instrumentos financieros, por país',
            size='Population',
                size_max=70,
                trendline='ols',
                trendline_scope='overall', 
                hover_name='Entity',
                color='Region')
        fig_2.show()
        st.plotly_chart(fig_2)

    
    st.write('¿Quién utiliza nuevas tecnologías de pago móvil? Cabe señalar que el Global Index clasifica como tecnologías de pago móvil \
    aquellos instrumentos que permite a la pobación desbancarizada utilizar sus teléfonos móviles como cuentas bancarias: para depositar, \
    retirar y transferir dinero con su teléfono. Las personas también pueden usar sistemas móviles para pagar facturas de servicios \
    públicos y pagar bienes en tiendas comerciales. Por ello, es razonable que estos servicios de pago en dispositivos móviles estén más \
    presentes en zonas rurales al cubrir población no bancarizada.')

    # Se muestra dos gráficos (una imagen): uso internet, y accounts:
    fig_in_acc = plt.figure(figsize=(15, 4))
    fig_in_acc, axs = plt.subplots(nrows=1, ncols=2, sharey=True)
    sns.regplot(x="Account (% age 15+)",
                y="Individuals using the Internet (% of population)",
                data=df,
                ax=axs[0])
    sns.regplot(x="Mobile money account (% age 15+) ",
                y="Individuals using the Internet (% of population)",
                data=df,
                ax=axs[1])
    st.pyplot(fig_in_acc)   
    ind_int = st.checkbox('Ver crecimiento del uso de internet por nivel de ingresos nacional en la última década')
    if ind_int:
        # Se imprime por pantalla gráfico de barras del crecimiento del uso de internet
        fig_int = sns.catplot(x="Year",
                        y="Individuals using the Internet (% of population)",
                        hue="Economic status",
                        kind="bar",
                        data=df,
                        ci=None)
        st.pyplot(fig_int) 
        st.write('Resulta revelador ver que las personas que tienen tecnologías de pago móvil son aquellas que menos acceso a internet tienen.\
        Esta correlación respalda la idea de que la digitalización es una oportunidad para ofrecer servicios financieros a las áreas \
        más remotas y así reducir la vulnerabilidad ante las emergenicas e incertidumbres, eventos más comunes en la población más vulnerable.')
    
    st.write('La expansión de internet a nivel global también está impulsando nuevos canales de servicios financieros. No obstante, \
        la tecnología móvil permite llevar servicios financieros básicos a zonas más desconectadas, donde hay menor acceso a internet \
        e incluso menor número de dispositivos móviles. Esto se debe a la creatividad de muchas iniciativas que brindan servicios \
        financieros básicos a la población más vulnerable y remota. Por esta razón estos servicios de pago móvil se orientan a \
        poblaciones con menor número de dispositivos móviles.') 
    # Se muestra dos gráficos (una imagen): uso de teléfonos móviles y número de cuentas
    fig_cell_acc = plt.figure(figsize=(15, 4))
    fig_cell_acc, axs = plt.subplots(nrows=1, ncols=2, sharey=True)
    sns.regplot(x="Account (% age 15+)",
                y="Cell phones (per 100 people)",
                data=df,
                ax=axs[0])
    sns.regplot(x="Mobile money account (% age 15+) ",
                y="Cell phones (per 100 people)",
                data=df,
                ax=axs[1])
    st.pyplot(fig_cell_acc)
    st.write('NOTA: El eje y muestra el porcentaje de teléfonos móviles en la población. Oscila entre 0.00 y 2.0 (0% y 200%), ya que es común que una persona tenga \
    más de un dispositivo móvil. Como a lo largo de todas las estadísticas, solamente se contabilizan a personas mayores de 15 años.')
    ind_cell = st.checkbox('Ver crecimiento del uso de dispositivos móviles por nivel de ingresos nacional en la última década')
    if ind_cell:
        # Se imprime por pantalla gráfico de barras del crecimiento del uso de dispositivos móviles
        fig_cell = sns.catplot(x="Year",
                        y="Cell phones (per 100 people)",
                        hue="Economic status",
                        kind="bar",
                        data=df,
                        ci=None)
        st.pyplot(fig_cell) 

    st.header('Expansión de la bancarización digital frente a la institucional por regiones:')
    fig_dig = go.Figure(data=[go.Histogram(
                name='Financial institution account',
                x=df['Region'],
                y=df['Financial institution account (% age 15+) '],
                offsetgroup=0,
                histfunc='avg'),
            go.Histogram(
                name='Mobile money account',
                x=df['Region'],
                y=df['Mobile money account (% age 15+) '],
                offsetgroup=1,
                histfunc='avg')],
        layout=go.Layout(
            title="Porcentaje de bancarización por región, ya sea institucional o digital",
            yaxis_title='Account (% age 15+)'))
    fig_dig.update_layout(transition = {'duration': 2000})
    fig_dig.show()
    st.plotly_chart(fig_dig)
    st.write('Llama la atención que la región donde más se ha extendido la bancarización digital en zonas remotas es en África sub-sahariana,\
        que es la región con menor número de banacarización institucional. Por otro lado, Oriente Medio y el norte de África es una zona \
        donde apenas ha penetrado esta tecnología, a pesar de ser la segunda región con menor población bancarizada institucionalmente.') 

    with st.expander('Caso de estudio: M-PESA'):
        st.write('Kenia implementó en el año 2007 un programa de servicios de pago y de banca por medio de dispositivos móviles \
            - M-PESA, el cual estaba operado por la compañía de telefonía móvil Safaricom. El funcionamiento era muy sencillo: \
            ofrecía a sus clientes la posibilidad de tener una cuenta transaccional básica que utiliza el número de teléfono \
            móvil como número de cuenta.')
        st.write('El alcance de esta herramienta ha sido exponencial, pues una población que apenas \
            tenía acceso a los servicios financieros de la banca formal, en el año 2017 ya contaba con una tasa de bancarización móvil del \
            69% de su población mayor de 15 años.')


# Prioridades a día de hoy

def tendencias_digitales():

    disp_dens = st.checkbox('Ver disparidades dentro de cada región')
    if disp_dens:
        st.write('Para obtener una perspectiva más profunda sobre la desigudaldad interna en el nivel de bancarización por regiones, se muestra un diagrama de densidad \
            por cada una de las regiones económicas. El sudeste asiático es la región geográfica que más disparidades presenta de acceso \
            financiero, seguido de Latinoamérica y el Caribe, regiones que deben ser priorizadas a día de hoy.')
        tipo_dist_reg = st.select_slider(
            'Selecciona región económica a visualizar',
            options=['South Asia', 'Sub-Saharan Africa (excluding high income)', 'Europe & Central Asia (excluding high income)', 'Latin America & Caribbean (excluding high income)', 'East Asia & Pacific (excluding high income)', 'Middle East & North Africa (excluding high income)', 'High income'])
            
        if tipo_dist_reg == 'South Asia':
            st.write('Distribution of the population with an account in South Asia in the last decade')
            plt.figure(figsize=(12,8))
            fig_tipo_dist_reg_sa = sns.kdeplot(df[df['Region'] == 'South Asia']['Account (% age 15+)'], 
                color="green", label='South Asia', shade=True)
            plt.xlim(0,1)
            st.pyplot(fig_tipo_dist_reg_sa.figure) 
            with st.expander('Dentro de esta región económica el Banco Mundial clasifica los siguientes países'):
                st.write(tuple(df[df['Region']=='South Asia']['Entity'].unique()))
                st.write('Nota: es posible que algún país esté clasificado en dos regiones, al haber evolucionado sus indicadores \
                    y haber entrado en la clasificación de país de altos ingresos.')

        if tipo_dist_reg == 'Sub-Saharan Africa (excluding high income)':
            st.write('Distribution of the population with an account in Sub-Saharan Africa (excluding high income) in the last decade')
            plt.figure(figsize=(12,8))
            fig_tipo_dist_reg_sba = sns.kdeplot(df[df['Region'] == 'Sub-Saharan Africa (excluding high income)']['Account (% age 15+)'], 
                color="brown", label='Sub-Saharan Africa (excluding high income)', shade=True)
            st.pyplot(fig_tipo_dist_reg_sba.figure)
            with st.expander('Dentro de esta región económica el Banco Mundial clasifica los siguientes países'):
                st.write(tuple(df[df['Region']=='Sub-Saharan Africa (excluding high income)']['Entity'].unique()))
                st.write('Nota: es posible que algún país esté clasificado en dos regiones, al haber evolucionado sus indicadores \
                    y haber entrado en la clasificación de país de altos ingresos.') 

        if tipo_dist_reg == 'Europe & Central Asia (excluding high income)':
            st.write('Distribution of the population with an account in Europe & Central Asia (excluding high income) in the last decade')
            plt.figure(figsize=(12,8))
            fig_tipo_dist_reg_eca = sns.kdeplot(df[df['Region'] == 'Europe & Central Asia (excluding high income)']['Account (% age 15+)'], 
                color="blue", label='Europe & Central Asia (excluding high income)', shade=True)
            st.pyplot(fig_tipo_dist_reg_eca.figure) 
            with st.expander('Dentro de esta región económica el Banco Mundial clasifica los siguientes países'):
                st.write(tuple(df[df['Region']=='Europe & Central Asia (excluding high income)']['Entity'].unique()))
                st.write('Nota: es posible que algún país esté clasificado en dos regiones, al haber evolucionado sus indicadores \
                    y haber entrado en la clasificación de país de altos ingresos.')

        if tipo_dist_reg == 'Latin America & Caribbean (excluding high income)':
            st.write('Distribution of the population with an account in Latin America & Caribbean (excluding high income) in the last decade')
            plt.figure(figsize=(12,8))
            fig_tipo_dist_reg_la = sns.kdeplot(df[df['Region'] == 'Latin America & Caribbean (excluding high income)']['Account (% age 15+)'], 
                color="orange", label='Latin America & Caribbean (excluding high income)', shade=True)
            st.pyplot(fig_tipo_dist_reg_la.figure) 
            with st.expander('Dentro de esta región económica el Banco Mundial clasifica los siguientes países'):
                st.write(tuple(df[df['Region']=='Latin America & Caribbean (excluding high income)']['Entity'].unique()))
                st.write('Nota: es posible que algún país esté clasificado en dos regiones, al haber evolucionado sus indicadores \
                    y haber entrado en la clasificación de país de altos ingresos.')

        if tipo_dist_reg == 'East Asia & Pacific (excluding high income)':
            st.write('Distribution of the population with an account in East Asia & Pacific (excluding high income) in the last decade')
            plt.figure(figsize=(12,8))
            fig_tipo_dist_reg_eap = sns.kdeplot(df[df['Region'] == 'East Asia & Pacific (excluding high income)']['Account (% age 15+)'], 
                color="red", label='East Asia & Pacific (excluding high income)', shade=True)
            st.pyplot(fig_tipo_dist_reg_eap.figure) 
            with st.expander('Dentro de esta región económica el Banco Mundial clasifica los siguientes países'):
                st.write(tuple(df[df['Region']=='East Asia & Pacific (excluding high income)']['Entity'].unique()))
                st.write('Nota: es posible que algún país esté clasificado en dos regiones, al haber evolucionado sus indicadores \
                    y haber entrado en la clasificación de país de altos ingresos.')

        if tipo_dist_reg == 'Middle East & North Africa (excluding high income)':
            st.write('Distribution of the population with an account in Middle East & North Africa (excluding high income) in the last decade')
            plt.figure(figsize=(12,8))
            fig_tipo_dist_reg_mea = sns.kdeplot(df[df['Region'] == 'Middle East & North Africa (excluding high income)']['Account (% age 15+)'], 
                color="yellow", label='Middle East & North Africa (excluding high income)', shade=True)
            st.pyplot(fig_tipo_dist_reg_mea.figure) 
            with st.expander('Dentro de esta región económica el Banco Mundial clasifica los siguientes países'):
                st.write(tuple(df[df['Region']=='Middle East & North Africa (excluding high income)']['Entity'].unique()))
                st.write('Nota: es posible que algún país esté clasificado en dos regiones, al haber evolucionado sus indicadores \
                    y haber entrado en la clasificación de país de altos ingresos')

        if tipo_dist_reg == 'High income':
            st.write('Distribution of the population with an account in High income economies in the last decade')
            plt.figure(figsize=(12,8))
            fig_tipo_dist_reg_hi = sns.kdeplot(df[df['Region'] == 'High income']['Account (% age 15+)'], 
                color="black", label='High income', shade=True)
            st.pyplot(fig_tipo_dist_reg_hi.figure) 
            with st.expander('Dentro de esta región económica el Banco Mundial clasifica los siguientes países'):
                st.write(tuple(df[df['Region']=='High income']['Entity'].unique()))
                st.write('Nota: es posible que algún país esté clasificado en dos regiones, al haber evolucionado sus indicadores \
                        y haber entrado en la clasificación de país de altos ingresos')


def mujer():
    
    st.subheader('La exclusión financiera de la mujer es diferente a la del hombre')
    st.write('Para poder lograr poner al alcance servicios financieros efectivos y que sirvan a la sociedad, es necesario \
    comprender el modo en que la exclusión financiera de la mujer se diferencia de la del hombre. Resulta necesario \
    establecer estrategias que reduzcan la vulnerabilidad de la mujer, especialmente de la mujer con menor \
    nivel de educación, debido a su vulnerabilidad ante emergencias. En términos estadísticos la mujer tiene más dependecia de \
    familiares y personas próximas ante emergencias.')

    
    st.image(r'es_oif_la-dona-martin-chiesa_12_2016.jpg')

    st.write('El acceso a servicios financieros entre hombres y mujeres, aunque dispar por 3 puntos porcentuales \
        globalmente y una diferencia mayor por regiones, requiere de una examinación más cercana en el uso de los servivios, ya que \
        si solamente nos fijamos en la titularidad de las cuentas bancarias podremos llegar a conclusiones sesgadas ante los problemas \
        derivados de la exclusión financiera.')

    hm_ck = st.checkbox('Ver diferencias de acceso a instrumentos financieros entre hombre y mujer por región:')
    if hm_ck:
        # Bancarización hombre-mujer
        tipo_bar = st.select_slider(
            'Selecciona año a visualizar',
            options=['Acceso a cuenta bancaria','Acceso a cuenta bancaria en institución financiera', 'Bancarización por medio de tecnologías de pago móvil'])
        
        if tipo_bar == 'Acceso a cuenta bancaria':
            st.write('Acceso a cuenta bancaria')
            st.write('Promedio de la última década')
            fig_hm_11 = go.Figure( data=[go.Histogram(
                        name="Male",
                        x=df2011['Region'],
                        y=df2011['Account, male (% age 15+)'],
                        offsetgroup=0,
                        histfunc='avg'),
                    go.Histogram(
                        name="Female",
                        x=df2011['Region'],
                        y=df2011["Account, female (% age 15+)"],
                        offsetgroup=1,
                        histfunc='avg')],
                layout=go.Layout(
                    title="Porcentaje de bancarización general por región",
                    yaxis_title='Account (% age 15+)'))
            fig_hm_11.update_layout(transition = {'duration': 2000})
            fig_hm_11.show()
            st.plotly_chart(fig_hm_11)  

        if tipo_bar == 'Acceso a cuenta bancaria en institución financiera':
            st.write('Acceso a cuenta bancaria en institución financiera')
            st.write('Promedio de la última década')
            fig_hm_14 = go.Figure( data=[go.Histogram(
                        name="Male",
                        x=df2014['Region'],
                        y=df2014['Financial institution account,male(% age 15+) '],
                        offsetgroup=0,
                        histfunc='avg'),
                    go.Histogram(
                        name="Female",
                        x=df2014['Region'],
                        y=df2014['Financial institution account,female(% age 15+) '],
                        offsetgroup=1,
                        histfunc='avg')],
                layout=go.Layout(
                    title="Porcentaje de bancarización en institución financiera por región",
                    yaxis_title='Account (% age 15+)'))
            fig_hm_14.update_layout(transition = {'duration': 2000})
            fig_hm_14.show()
            st.plotly_chart(fig_hm_14)
            with st.expander('¿Qué se entiende por poseer una cuenta bancaria en una institución financiera?'):
                st.write('Cuenta en una institución financiera denota el porcentaje de encuestados que informan tener una cuenta \
                    (por sí mismos o junto con otra persona) en un banco u otro tipo de institución financiera.')

        if tipo_bar == 'Bancarización por medio de tecnologías de pago móvil':
            st.write('Bancarización por medio detecnologías de pago móvil')
            st.write('Promedio de la última década')
            fig_hm_gl = go.Figure( data=[go.Histogram(
                        name="Male",
                        x=df['Region'],
                        y=df['Mobile money account, male  (% age 15+) '],
                        offsetgroup=0,
                        histfunc='avg'),
                    go.Histogram(
                        name="Female",
                        x=df['Region'],
                        y=df['Mobile money account, female (% age 15+) '],
                        offsetgroup=1,
                        histfunc='avg')],
                layout=go.Layout(
                    title="Porcentaje de bancarización móvil por región",
                    yaxis_title='Account (% age 15+)'))
            fig_hm_gl.update_layout(transition = {'duration': 2000})
            fig_hm_gl.show()
            st.plotly_chart(fig_hm_gl) 
            with st.expander('¿Qué se entiende por poseer una cuenta bancaria por medio detecnologías de pago móvil?'):
                st.write('Global Index clasifica como tecnologías de pago móvil aquellos instrumentos que permite a la pobación \
                    desbancarizada utilizar sus teléfonos móviles como cuentas bancarias: para depositar, retirar y transferir dinero con su teléfono.')

    st.write('Mujeres de áreas rurales tienen mayor dependencia por su limitado acceso a información sobre cómo \
        lidiar con servicios financieros en constante evolución, especialmente cuando es digital. También es propio considerar \
        los ratios de analfabetismo en un medio financiero generalmente en lengua inglesa. Sin embargo, los datos de titularidad de \
        cuenta bancaria en tecnología móvil (orientada a áreas remotas con limitado acceso a internet), no presentan evidencias de \
        un mayor ratio de inclusión de la mujer. Por ende, es necesario prestar especial atención a las diferencias entre hombres y mujeres \
        a la hora de gestionar las finanzas personales o del hogar.')

    st.subheader('Diferencias y similitudes al lidiar con emergencias')
    st.write('Global Index recoge el porcentaje de encuestados que informan que, en caso de emergencia, es muy posible que obtengan el 5% \
        del Producto Nacional Bruto (PNB) per cápita en moneda local en el próximo mes. Se muestra el porcentaje de encuestados que informan \
        que, en caso de emergencia, es muy posible para ellos lograr dicha cantidad.')

    df['planeta'] = '' # Para que todos los países tengan una variable en común
    fig_hm_diff = go.Figure()
    fig_hm_diff.add_trace(go.Violin(x=df['Region'],
                            y=df['Coming up with emergency funds: possible, male (% age 15+) '],
                            legendgroup='M', scalegroup='M', name='M',
                            line_color='blue'))

    fig_hm_diff.add_trace(go.Violin(x=df['Region'],
                            y=df['Coming up with emergency funds: possible, female (% age 15+) '],
                            legendgroup='F', scalegroup='F', name='F',
                            line_color='brown') )

    fig_hm_diff.update_traces(box_visible=True, meanline_visible=True)
    fig_hm_diff.update_layout(violinmode='group', title_text='Población a la que le es posible lograr fondos de emergencia en menos de un mes (% age 15+)')
    fig_hm_diff.show()
    st.plotly_chart(fig_hm_diff)

    st.write('La media de mujeres que pueden conseguir dicha cantidad "muy posiblemente" es 8 puntos porcentuales menor que al de hombres. \
    Una observación de la distribución más a fondo permite apreciar que la diferencia aumenta si nos fijamos en el percentil 25% tanto de hombres \
    como de mujeres, con un diferencia de 12% inferior para esta última, en una posición más vulnerable ante las emergenicas.')

    st.subheader('Estrategias para lograr fondos de emergencia')
    st.write('Poniendo el foco en las estrategias que emplean tanto hombres como mujeres para conseguir recursos en caso de emergencia, \
    las entrevistas llevadas a cabo por Global Findex concluyen que apenas hay diferencias a la hora de pedir crédito o utilizar ahorro o venta de activos entre hombres y mujeres. \
    Sin embargo, encontramos que los hombres tienen una mayor opción de conseguir la cantidad de la emergencia trabajando (11% de puntos \
    porcentuales de diferencia). Por otro lado, las mujeres tienen mayor opciones de acudir a familiares o personas próximas para \
    conseguir los recursos necesarios en una emergencia.')
    hm_str_ck = st.select_slider('Estrategias de conseguir fondos de emergencia',
            options=['Acudiendo a familiares y amigos', 'Ahorros', 'Solicitando crédito', 'Trabajando', 'Vendiendo bienes'])
    if hm_str_ck == 'Acudiendo a familiares y amigos':
        df['planeta'] = '' # Para que todos los países tengan una variable en común
        fig_hm_ff = go.Figure()
        fig_hm_ff.add_trace(go.Violin(x=df['planeta'],
                                y=df['Main source of emergency funds: family or friends, male  (% able to raise funds, age 15+)'],
                                legendgroup='M', scalegroup='M', name='M',
                                line_color='blue'))
        fig_hm_ff.add_trace(go.Violin(x=df['planeta'],
                                y=df['Main source of emergency funds: family or friends, female  (% able to raise funds, age 15+)'],
                                legendgroup='F', scalegroup='F', name='F',
                                line_color='brown') )
        fig_hm_ff.update_traces(box_visible=True, meanline_visible=True)
        fig_hm_ff.update_layout(violinmode='group', title_text='Lograr fondos de emergencia acudiendo a familiares y personas próximas (% age 15+)')
        fig_hm_ff.show()
        st.plotly_chart(fig_hm_ff)
        st.write('Aunque es lo más común y presenta muchas ventajas, solicitar fondos informalmente a familiares y personas próximas \
        no siempre es fácil. Muchos préstamos sin intereses obligan a devolver el favor. Además, Solicitar préstamos a varias personas \
        para hacer frente a una emergencia puede ser una fuente de estrés y vergüenza.')
    if hm_str_ck == 'Ahorros':
        df['planeta'] = '' # Para que todos los países tengan una variable en común
        fig_hm_ah = go.Figure()
        fig_hm_ah.add_trace(go.Violin(x=df['planeta'],
                                y=df['Main source of emergency funds: savings, male  (% able to raise funds, age 15+) '],
                                legendgroup='M', scalegroup='M', name='M',
                                line_color='blue'))
        fig_hm_ah.add_trace(go.Violin(x=df['planeta'],
                                y=df['Main source of emergency funds: savings, female (% able to raise funds, age 15+) '],
                                legendgroup='F', scalegroup='F', name='F',
                                line_color='brown') )
        fig_hm_ah.update_traces(box_visible=True, meanline_visible=True)
        fig_hm_ah.update_layout(violinmode='group', title_text='Lograr fondos de emergencia por medio de ahorros (% age 15+)')
        fig_hm_ah.show()
        st.plotly_chart(fig_hm_ah)
    if hm_str_ck == 'Solicitando crédito':
        df['planeta'] = '' # Para que todos los países tengan una variable en común
        fig_hm_cr = go.Figure()
        fig_hm_cr.add_trace(go.Violin(x=df['planeta'],
                                y=df['Main source of emergency funds: loan from a bank, employer, or private lender, male  (% able to raise funds, age 15+) '],
                                legendgroup='M', scalegroup='M', name='M',
                                line_color='blue'))
        fig_hm_cr.add_trace(go.Violin(x=df['planeta'],
                                y=df['Main source of emergency funds: loan from a bank, employer, or private lender, female (% able to raise funds, age 15+) '],
                                legendgroup='F', scalegroup='F', name='F',
                                line_color='brown') )
        fig_hm_cr.update_traces(box_visible=True, meanline_visible=True)
        fig_hm_cr.update_layout(violinmode='group', title_text='Lograr fondos de emergencia por medio de créditos (% age 15+)')
        fig_hm_cr.show()
        st.plotly_chart(fig_hm_cr)
    if hm_str_ck == 'Trabajando':
        df['planeta'] = '' # Para que todos los países tengan una variable en común
        fig_hm_tr = go.Figure()
        fig_hm_tr.add_trace(go.Violin(x=df['planeta'],
                                y=df['Main source of emergency funds: money from working, male  (% able to raise funds, age 15+) '],
                                legendgroup='M', scalegroup='M', name='M',
                                line_color='blue'))
        fig_hm_tr.add_trace(go.Violin(x=df['planeta'],
                                y=df['Main source of emergency funds: money from working, female (% able to raise funds, age 15+) '],
                                legendgroup='F', scalegroup='F', name='F',
                                line_color='brown') )
        fig_hm_tr.update_traces(box_visible=True, meanline_visible=True)
        fig_hm_tr.update_layout(violinmode='group', title_text='Lograr fondos de emergencia trabajando (% age 15+)')
        fig_hm_tr.show()
        st.plotly_chart(fig_hm_tr)
    if hm_str_ck == 'Vendiendo bienes':
        df['planeta'] = '' # Para que todos los países tengan una variable en común
        fig_hm_sa = go.Figure()
        fig_hm_sa.add_trace(go.Violin(x=df['planeta'],
                                y=df['Main source of emergency funds: sale of assets , male (% able to raise funds, age 15+) '],
                                legendgroup='M', scalegroup='M', name='M',
                                line_color='blue'))
        fig_hm_sa.add_trace(go.Violin(x=df['planeta'],
                                y=df['Main source of emergency funds: sale of assets, female  (% able to raise funds, age 15+) '],
                                legendgroup='F', scalegroup='F', name='F',
                                line_color='brown') )
        fig_hm_sa.update_traces(box_visible=True, meanline_visible=True)
        fig_hm_sa.update_layout(violinmode='group', title_text='Lograr fondos de emergencia vendiendo bienes (% age 15+)')
        fig_hm_sa.show()
        st.plotly_chart(fig_hm_sa)


def educacion():

    st.subheader('El principal motivo de la desbancarización es el analfabetismo financiero')    
    st.image('IMG_0199_rdax_782x521s.jpg', caption='El nivel de educación es un aspecto determinante en la gestión de servicios financieros')
    st.write('La incomprensión de los servicios financieros genera una situación de dependencia alta, ante la cual existe mayor vulnerabilidad \
    ante prestamistas que imponen tasas abusivas generando mayor desconfianza. Además, es común que servicios financieros en zonas remotas \
    estén disponibles en idiomas oficiales de un país, a veces no hablado ni leído en áreas remotas. La educación financiera debe ser \
    un aspecto indiscutible a tener en cuenta cuando se establecen prioridades y estrategias relativas a la inclusión financiera.')
    st.write('A continuación se muestra la relación entre el analfabetismo y la desbancarización:')
    bubb_ed = st.checkbox('Ver las tendencias diferenciadas por regiones')
    if bubb_ed:
        df['planeta'] = '' # Para que todos los países tengan una variable en común
        fig_ed_1 = px.scatter(
        df2017[['Region','Entity', 'Adult literacy rate (%)','Account (% age 15+)', 'Population']],
        x='Account (% age 15+)',
        y='Adult literacy rate (%)',
        title='Relación entre el analfabetismo y el acceso a instrumentos financieros, por país',
        size='Population',
            size_max=90,
            trendline='ols',
            trendline_scope='trace', # trendline_scope='trace' para ver por regiones
            hover_name='Entity',
            color='Region')
        fig_ed_1.show()
        st.plotly_chart(fig_ed_1)
    else:
        df['planeta'] = '' # Para que todos los países tengan una variable en común
        fig_ed = px.scatter(
        df2017[['Region','Entity', 'Adult literacy rate (%)','Account (% age 15+)', 'Population']],
        x='Account (% age 15+)',
        y='Adult literacy rate (%)',
        title='Relación entre el analfabetismo y el acceso a instrumentos financieros, por país',
        size='Population',
            size_max=90,
            trendline='ols',
            trendline_scope='overall', # trendline_scope='trace' para ver por regiones
            hover_name='Entity',
            color='Region')
        fig_ed.show()
        st.plotly_chart(fig_ed)

    st.write('La expansión de dispositivos móviles ha logrado acercar servicios financieros elementales a las zonas más remotas. \
        Sin embargo, es totalmente necesario que vaya de la mano de programas de educación financiera para lograr los objetivos de \
        inclusión, particularmente en las regiones de mayor analfabetismo. En el gráfico se puede apreciar las tendencias \
        por región, donde se aprecia que a menor nivel de analfabetismo por país, se reduce drásticamente la bancarización de \
        su población. Particularmente, África subsahariana y el sureste asiática son las regiones donde mayor impacto tendrán los \
        programas de educación financiera, seguidos de Oriente Medio y el norte de África así como de Latinoamérica y el Caribe.')

    st.write('Es común que las poblaciones con menos recursos se esfuercen mucho en la administración de fondos para gastos inesperados, \
        asegurándose de que haya dinero disponible cuando sea necesario. En países de rentas altas, la cartera de instrumentos financieros \
        de un hogar generalmente se administra sobre la base del riesgo y el rendimiento. En cambio, en poblaciones de rentas bajas \
        los servicios financieros deben ajustarse para que sea posible obtener fondos en las cantidades deseadas en los momentos deseados. \
        El dinero es escaso y su oferta es irregular, por lo que tratar con liquidez en momentos de estrés es esencial. El análisis \
        del flujo de efectivo (cómo manejan sus ingresos y gastos), en lugar del análisis del balance general (monto \
        monetario del que disponen), es cómo debe analizarse las situaciones de exclusión financiera.')

    st.subheader('Estrategias para lograr fondos de emergencia')
    st.write('Encontramos diferencias marcadas en la gestión de recursos financieros en funcion del nivel de educación, principal causa \
        de la exclusión financiera. Para la población que no ha alcanzado estudios de educación secundaria, su posibilidad de hacer frente \
        a una emergencia que suponga un capital del 5% del Producto Nacional Bruto (PNB) per cápita es 21 puntos porcentuales menor que \
        aquella población con educación secundaria o superior.')
    df['planeta'] = '' # Para que todos los países tengan una variable en común
    fig_ed_tt = go.Figure()
    fig_ed_tt.add_trace(go.Violin(x=df['planeta'],
                                y=df['Coming up with emergency funds: possible, primary education or less (% age 15+) '],
                                legendgroup='primary education or less', scalegroup='primary education or less', name='primary education or less',
                                line_color='green'))
    fig_ed_tt.add_trace(go.Violin(x=df['planeta'],   
                                y=df['Coming up with emergency funds: possible, secondary education or more (% age 15+) '],
                                legendgroup='secundary education or more', scalegroup='secundary education or more', name='secundary education or more',
                                line_color='black') )
    fig_ed_tt.update_traces(box_visible=True, meanline_visible=True)
    fig_ed_tt.update_layout(violinmode='group', title_text='Población a la que le es posible lograr fondos de emergencia en menos de un mes (% age 15+)')
    fig_ed_tt.show()
    st.plotly_chart(fig_ed_tt)
    st.write('La población menos educada (que no alcanzó la educación secundaria) tiene que trabajar más duro para administrar su \
        dinero y hacer frente a emergencias. Lo ideal es funcionar mediante el ahorro y el desahorro (es difícil encontrar vehículos \
        adecuados para ello pues solamente el 15% de los hogares pueden acudir a esta estrategia). Por ello, particularmente las poblaciones \
        con menor educación, acuden a familiares y personas próximas para conseguir fondos (estrategia utilizada por el 40% de \
        personas sin eduación secundaria), o a prestamistas (15% de la población general). A menudo pedir dinero es un trabajo arduo y puede \
        traer altos costes, incluyendo costes sociales y psicológicos a parte de económicos.')
    ed_str_ck = st.select_slider('Estrategias de conseguir fondos de emergencia',
            options=['Acudiendo a familiares y amigos', 'Ahorros', 'Solicitando crédito', 'Trabajando', 'Vendiendo bienes'])
    if ed_str_ck == 'Acudiendo a familiares y amigos':
        df['planeta'] = '' # Para que todos los países tengan una variable en común
        fig_ed_ff = go.Figure()
        fig_ed_ff.add_trace(go.Violin(x=df['planeta'],
                                    y=df['Main source of emergency funds: family or friends, primary education or less (% able to raise funds, age 15+)'],
                                    legendgroup='primary education or less', scalegroup='primary education or less', name='primary education or less',
                                    line_color='green'))
        fig_ed_ff.add_trace(go.Violin(x=df['planeta'],   
                                    y=df['Main source of emergency funds: family or friends, secondary education or more (% able to raise funds, age 15+)'],
                                    legendgroup='secundary education or more', scalegroup='secundary education or more', name='secundary education or more',
                                    line_color='black') )
        fig_ed_ff.update_traces(box_visible=True, meanline_visible=True)
        fig_ed_ff.update_layout(violinmode='group', title_text='Main source of emergency funds: family or friends (% able to raise funds, age 15+)')
        fig_ed_ff.show()
        st.plotly_chart(fig_ed_ff)
    if ed_str_ck == 'Ahorros':
        df['planeta'] = '' # Para que todos los países tengan una variable en común
        fig_ed_ck = go.Figure()
        fig_ed_ck.add_trace(go.Violin(x=df['planeta'],
                                    y=df['Main source of emergency funds: savings, primary education or less (% able to raise funds, age 15+) '],
                                    legendgroup='primary education or less', scalegroup='primary education or less', name='primary education or less',
                                    line_color='green'))
        fig_ed_ck.add_trace(go.Violin(x=df['planeta'],   
                                    y=df['Main source of emergency funds: savings, secondary education or more (% able to raise funds, age 15+) '],
                                    legendgroup='secundary education or more', scalegroup='secundary education or more', name='secundary education or more',
                                    line_color='black') )
        fig_ed_ck.update_traces(box_visible=True, meanline_visible=True)
        fig_ed_ck.update_layout(violinmode='group', title_text='Main source of emergency funds: savings (% able to raise funds, age 15+) ')
        fig_ed_ck.show()
        st.plotly_chart(fig_ed_ck)
    if ed_str_ck == 'Solicitando crédito':
        df['planeta'] = '' # Para que todos los países tengan una variable en común
        fig_ed_cr = go.Figure()
        fig_ed_cr.add_trace(go.Violin(x=df['planeta'],
                                    y=df['Main source of emergency funds: loan from a bank, employer, or private lender, primary education or less (% able to raise funds, age 15+) '],
                                    legendgroup='primary education or less', scalegroup='primary education or less', name='primary education or less',
                                    line_color='green'))
        fig_ed_cr.add_trace(go.Violin(x=df['planeta'],   
                                    y=df['Main source of emergency funds: loan from a bank, employer, or private lender, secondary education or more (% able to raise funds, age 15+) '],
                                    legendgroup='secundary education or more', scalegroup='secundary education or more', name='secundary education or more',
                                    line_color='black') )
        fig_ed_cr.update_traces(box_visible=True, meanline_visible=True)
        fig_ed_cr.update_layout(violinmode='group', title_text='Main source of emergency funds: loan from a bank, employer, or private lender (% able to raise funds, age 15+) ')
        fig_ed_cr.show()
        st.plotly_chart(fig_ed_cr)
    if ed_str_ck == 'Trabajando':
        df['planeta'] = '' # Para que todos los países tengan una variable en común
        fig_ed_tr = go.Figure()
        fig_ed_tr.add_trace(go.Violin(x=df['planeta'],
                                    y=df['Main source of emergency funds: money from working, primary education or less  (% able to raise funds, age 15+) '],
                                    legendgroup='primary education or less', scalegroup='primary education or less', name='primary education or less',
                                    line_color='green'))
        fig_ed_tr.add_trace(go.Violin(x=df['planeta'],   
                                    y=df['Main source of emergency funds: money from working, secondary education or more (% able to raise funds, age 15+) '],
                                    legendgroup='secundary education or more', scalegroup='secundary education or more', name='secundary education or more',
                                    line_color='black') )
        fig_ed_tr.update_traces(box_visible=True, meanline_visible=True)
        fig_ed_tr.update_layout(violinmode='group', title_text='Main source of emergency funds: money from working (% able to raise funds, age 15+) ')
        fig_ed_tr.show()
        st.plotly_chart(fig_ed_tr)
    if ed_str_ck == 'Vendiendo bienes':
        df['planeta'] = '' # Para que todos los países tengan una variable en común
        fig_ed_bn = go.Figure()
        fig_ed_bn.add_trace(go.Violin(x=df['planeta'],
                                    y=df['Main source of emergency funds: sale of assets, primary education or less (% able to raise funds, age 15+) '],
                                    legendgroup='primary education or less', scalegroup='primary education or less', name='primary education or less',
                                    line_color='green'))
        fig_ed_bn.add_trace(go.Violin(x=df['planeta'],   
                                    y=df['Main source of emergency funds: sale of assets, secondary education or more (% able to raise funds, age 15+) '],
                                    legendgroup='secundary education or more', scalegroup='secundary education or more', name='secundary education or more',
                                    line_color='black') )
        fig_ed_bn.update_traces(box_visible=True, meanline_visible=True)
        fig_ed_bn.update_layout(violinmode='group', title_text='Main source of emergency funds: sale of assets (% able to raise funds, age 15+) ')
        fig_ed_bn.show()
        st.plotly_chart(fig_ed_bn)

    st.write('Para las personas con menor nivel de educación financiera, los servicios financieros informales presentan varias ventajas \
        frente a la bancarización, pues están convenientemente al alcance de la mano. Usar el propio hogar como caja de ahorros \
        es lo más cómodo, y además no requiere de tratar con desconocidos (evitando una situación de dependencia a las personas\
        en una posición de desventaja). En las transacciones con vecinos, amigos y familiares, rara vez se requiere de contratos y papeleos, \
        un punto importante a considerar en poblaciones con altos ratios de analfabetismo, además de que son personas de una cultura similar. \
        Por último, los servicios informales a manudo están libres de coste financiero, e incluso cuando lo tienen, los términos pueden ser flexibles \
        y, a veces, el precio puede negociarse a la baja.')

    with st.expander('Caso de estudio: Q Mobile Cliente - Ahorrar para Aprender'):
        st.write('Q Mobile Cliente es una tecnología web móvil desarrollada por Savinco Social Finance, empresa social que ha compaginado \
            el desarrollo de servicios digitales de banca con programas de educación financiera, logrando la inclusión financiera de más de \
            25,000 personas en Ecuador y Perú por medio de la configuración de grupos de ahorro.')
        st.write('La tecnología web móvil permite medir el impacto, monitorear las transacciones financieras grupales y \
            controlar la calidad del proyecto, así como proporcionar escalabilidad al proyecto. Esta tecnología se compagina con la educación \
            financiera de los grupos focales de ahorro. \
            A este respecto, esta empresa social ha desarrollado durante la última década "Ahorra para Aprender", un programa de educación \
            práctica en el ahorro y su administración a través de grupos de confianza y el uso intensivo de tecnología móvil, con el fin \
            de mejorar la calidad de vida de las personas, a través de la inclusión financiera y el desarrollo de los negocios.')
        st.write('Su éxito reside en que ha logrado adaptarse a la flexibiliad que tienen los servicios financieros informales de la zona, \
            al mismo tiempo que aporta disciplina y fiabilidad, reduciendo la vulnerabilidad de poblaciones que se encontraban ajenas \
            a servicios finanieros formales.')


def conclusion():
    st.title('Conclusión')
    st.write('La digitalización nos ofrece una oportunidad única, pero no es suficiente por sí sola para procurar una efectiva \
        bancarización accesible a todos: es necesario compaginarla con educación financiera.')
    st.image(r'03-three-fishermen-on-inle-lake-aerial.jpg')

    st.write('La última ha década ha supuesto un crecimiento global en la expansión de servicios financieros formales a poblaciones \
        sin bancarizar. Gran parte de este crecimiento viene de la mano del mayor alcance de internet. No obstante, en zonas \
        de escasa accesibilidad de internet se aprecia un auge de la banca a través de dispositivos digitales, lo que ha propulsado \
        la inclusión financiera en países más deprimidos económicamente.')
    st.write('No obstante, en cuanto al uso de herramientas financieras, el sector informal es el mejor proveedor \
        de herramientas financieras convenientes para las poblaciones más vulnerables financieramente hasta el momento. \
        Por tanto, el desafío para el sector formal es ofrecer servicios que logren un equilibrio entre flexibilidad y \
        conveniencia, así como de estabilidad y fiabilidad. Para ello, es indispensable acompasar herramientas orientadas a la \
        inclusión financiera - como la expansión de la banca digital - con la educación financiera.')
    st.write('En definitiva, es de vital importancia expandir servicios financieros a las poblaciones más vulnerables para lograr \
        una mayor estabilidad en la gestión de sus finanzas personales. La bancarización (formal o digital) no logre erradicar la \
        pobreza por sí sola, pero pueden hacer mucho al garantizar el acceso a herramientas financieras que brinden las dosis \
        correctas de disciplina, seguridad, flexibilidad e incentivos.')

    st.markdown('*Análisis elaborado por Gonzalo Villalón Fornés*') 
    st.write('LinkedIn: https://www.linkedin.com/in/gvillalonf/')

