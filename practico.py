from pandas import pandas as pd

# Carga de datos
data_frame = pd.read_csv('edades-30Alumnos2.csv')

# Función de análisis matemático
def analisis_matematico(data_frame):
    
    # Verifica si las columnas necesarias existen en el data_frame
    required_columns = ["fi"]
    if not all(column in data_frame.columns for column in required_columns):
        print("El data_frame no tiene las columnas necesarias para realizar el análisis")
        return
    
    # Verifica que la columna "fi" contenga solo valores numéricos
    if not data_frame["fi"].apply(lambda x: isinstance(x, (int))).all():
        print("La columna 'fi' debe contener solo valores numéricos.")
        return
    
    #Verifica que los datos sean 
    if data_frame['fi'].isna().any():
        print("La columna 'fi' no puede contener valores nulos.")
        return
    
    # Realiza los cálculos si pasa las validaciones
    data_frame["Fi"] = data_frame["fi"].cumsum()
    data_frame["ri"] = data_frame["fi"] / data_frame["fi"].sum()
    data_frame["Ri"] = data_frame["ri"].cumsum()
    data_frame["pi%"] = data_frame["ri"] * 100
    data_frame["Pi%"] = data_frame["pi%"].cumsum()
    
    # Print de los cálculos hechos
    print(data_frame)
    # Copia al portapapeles los cálculos
    data_frame.to_clipboard()

# Llamada a la función
analisis_matematico(data_frame)
