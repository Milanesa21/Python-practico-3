from pandas import pandas as pd

# Carga de datos
data = {
    'Nombre': ['Villagra', 'Garcia', 'Piazza', 'Cuquejo', 'Barrientos', 'Meyer', 'Britez', 'Veron', 'Cespedes', 'Avalos', 'Mercado', 'Cubilla', 'Gomez', 'Bustos', 'Costadoni', 'Farias', 'Ruiz Diaz', 'Pedemonte', 'Aquino', 'Jara', 'Pietkiewicz', 'Fiore', 'Canepa', 'Stevens', 'Romero', 'Acuña', 'Acosta', 'Taquini', 'Mereles', 'Valdez'],
    'Edad': [19, 29, 19, 22, 23, 19, 30, 19, 19, 19, 20, 20, 20, 18, 22, 19, 34, 34, 21, 21, 22, 28, 29, 19, 20, 19, 25, 28, 21, 22]
}

data_frame = pd.DataFrame(data)

# Función de análisis matemático
def analisis_estadistico(data_frame):
    
    # Verifica si la columna 'Edad' existe en el data_frame
    if 'Edad' not in data_frame.columns:
        print("El data_frame no tiene la columna 'Edad' necesaria para realizar el análisis")
        return
    
    # Cuenta las edades repetidas y almacena los valores en la lista 'fi'
    fi = data_frame['Edad'].value_counts().sort_index().tolist()
    
    # Realiza los cálculos si 'fi' no está vacía
    if fi:
        # Creación de un nuevo data_frame para los cálculos
        calculations_df = pd.DataFrame({
            'Edad': range(min(data_frame['Edad']), min(data_frame['Edad']) + len(fi)),
            'fi': fi
        })
        
        # Realiza los cálculos si 'fi' no contiene valores nulos
        if calculations_df['Edad'].isnull.any() or not calculations_df['Edad'].dtype == int:
            print("La lista 'Edad' no puede contener valores nulos.")
            return
        
        # Realiza los cálculos estadísticos
        calculations_df["Fi"] = calculations_df["fi"].cumsum()
        calculations_df["ri"] = calculations_df["fi"] / calculations_df["fi"].sum()
        calculations_df["Ri"] = calculations_df["ri"].cumsum()
        calculations_df["pi%"] = calculations_df["ri"] * 100
        calculations_df["Pi%"] = calculations_df["pi%"].cumsum()
        
        # Print de los cálculos hechos
        print(calculations_df)
        
        # Copia al portapapeles los cálculos
        calculations_df.to_clipboard()
        
    else:
        print("No se encontraron edades para realizar el análisis.")

# Llamada a la función
analisis_estadistico(data_frame)
