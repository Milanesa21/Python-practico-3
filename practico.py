from pandas import pandas as pd


# Carga de datos
data_frame = pd.read_csv('edades-30Alumnos2.csv')

#Funcion de analisis matematico
def analisis_matematico(data_frame):
    
    #Verifica si el data_frame esta vacio
    if data_frame.empty:
        print("El data_frame esta vacio, no se pueden realizar analisis")
        return
    
    #Verifica si las columnas necesarias existen en el data_frame
    requires_columns = ["fi"]
    if not all (column in data_frame.columns for column in requires_columns):
        print("El data_frame no tiene las columnas necesarias para realizar el analisis")
        return
    
    #Realiza los calculos si pasa las validaciones
    data_frame["Fi"] = data_frame["fi"].cumsum()
    data_frame["ri"] = data_frame["fi"] / data_frame["fi"].sum()
    data_frame["Ri"] = (data_frame["ri"].cumsum())
    data_frame["pi%"] = data_frame["ri"] * 100
    data_frame["Pi%"] = (data_frame["pi%"].cumsum())
    
    # Print de los calculos hechos
    print(data_frame)
    #Copia al portapapeles los calculos
    data_frame.to_clipboard()

#Llamada a la funcion
analisis_matematico(data_frame)