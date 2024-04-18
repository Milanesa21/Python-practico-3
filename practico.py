from pandas import pandas as pd


# Carga de datos
data_frame = pd.read_csv('edades-30Alumnos2.csv')

#Funcion de analisis matematico
def analisis_matematico(data_frame):
    #cumea la suma
    data_frame["Fi"] = data_frame["fi"].cumsum()
    data_frame["ri"] = data_frame["fi"] / data_frame["fi"].sum()
    #cumea la frecuencia porcentual simple
    data_frame["Ri"] = (data_frame["ri"].cumsum())
    data_frame["pi%"] = data_frame["ri"] * 100
    #cumea la frecuencia porcentual acumulada
    data_frame["Pi%"] = (data_frame["pi%"].cumsum())
    
    # Print de los calculos hechos
    print(data_frame)
    data_frame.to_clipboard()

#Llamada a la funcion
analisis_matematico(data_frame)