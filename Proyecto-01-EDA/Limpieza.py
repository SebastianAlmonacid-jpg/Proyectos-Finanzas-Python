import pandas as pd
import numpy as np

def limpieza_datos(df_entrada):
    df = df_entrada.copy()
    df = df.dropna(how='all') #eliminar las FILAS QUE ESTAN VACIAS
    df = df.dropna(axis=1,how='all') #eliminar las COLUMNAS QUE ESTAN VACIAS
    df = df.dropna(axis=1, thresh=int(len(df)*0.5)) #eliminar las COLUMNAS QUE ESTAN CON UN PORCENTAJE DE CELDAS VACIAS. (50%=0.5)
    df = df.drop_duplicates() #eliminar las FILAS QUE ESTAN DUPLICADAS
    df = df.loc[:,~df.columns.duplicated()]#eliminar las COLUMNAS DULPLICADAS
    df = df.fillna(0) #RELLENAR los valores nulos con 0
    df = df.reset_index(drop=True)  # Elimina el índice antiguo y crea uno nuevo (0, 1, 2...)
    return df

def conversión_sueldos(df_entrada):
    df = df_entrada.copy()
    #Limpiar espacios en blanco (por si hay)
    df['Sueldo Base'] = df['Sueldo Base'].astype(str).str.strip()
    #Reemplazar coma por punto
    df['Sueldo Base'] = df['Sueldo Base'].str.replace(',', '.', regex=False)
    #Convertir a numérico (float), poniendo errores='coerce' para poner NaN si no puede convertir
    df['Sueldo Base'] = pd.to_numeric(df['Sueldo Base'], errors='coerce')
    # Opcional: si quieres reemplazar los NaN por 0 (o cualquier valor)
    df['Sueldo Base'] = df['Sueldo Base'].fillna(0)
    # Opcional: si quieres redondear y pasar a int
    df['Sueldo Base'] = df['Sueldo Base'].round().astype(int)
    return df