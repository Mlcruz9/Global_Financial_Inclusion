
import os
import pandas as pd

# Se definen nuestros datasets
df = pd.read_csv(r'datasets/indices_financieros.csv')
'''-----------------------------
Dataset que corresponde a un 'merge' y posterior adaptación de seis fuentes de datos recogidas por el Banco Mundial:
    - Global Findex
    - Uso de internet en la población
    - Uso de dispositivos móviles por la población
    - Disponibilidad de electricidad para la población
    - Ratio de analfabetismo en el mundo
    - Latitudes y longitudes de países

-----------------------------'''

df2017 = pd.read_csv(r'datasets/indices_2017.csv')
'''-----------------------------
Selección de datos específicos del año 

-----------------------------'''

df2014 = pd.read_csv(r'datasets/indices_2014.csv')
'''-----------------------------
Dataset que corresponde a un 'merge' de cinco fuentes distintas:
- World Bank
    - Global Findex
    - Uso de internet en la población
    - Uso de dispositivos móviles por la población
    - Disponibilidad de electricidad para la población
    - Ratio de analfabetismo en el mundo

-----------------------------'''


df2011 = pd.read_csv(r'datasets/indices_2011.csv')