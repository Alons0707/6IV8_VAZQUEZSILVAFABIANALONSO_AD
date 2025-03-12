import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#Configuración de estilo
sns.set_style("whitegrid")

#Cargar datos
df = pd.read_csv('EjercicioPython/csv/housing.csv')

#Función para calcular estadísticas
def calcular_estadisticas(df, columna):
    if columna not in df:
        raise ValueError(f"La columna '{columna}' no está en el dataset")
    
    return {
        'Media': df[columna].mean(),
        'Mediana': df[columna].median(),
        'Moda': df[columna].mode()[0] if not df[columna].mode().empty else None,
        'Rango': df[columna].max() - df[columna].min(),
        'Varianza': df[columna].var(),
        'Desviación Estándar': df[columna].std()
    }

#Calcular estadísticas
columna_objetivo = 'median_house_value'
estadisticas = calcular_estadisticas(df, columna_objetivo)

#Mostrar estadísticas
df_estadisticas = pd.DataFrame([estadisticas])
print("Estadísticas de la columna:", columna_objetivo)
print(df_estadisticas)

#Crear tabla de frecuencias
df_frecuencias = df[columna_objetivo].value_counts().sort_index().reset_index()
df_frecuencias.columns = [columna_objetivo, 'Frecuencia']

print("\nTabla de Frecuencias:")
print(df_frecuencias)

#Histograma
columnas_grafico = ['median_house_value', 'total_bedrooms', 'population']
columnas_disponibles = [col for col in columnas_grafico if col in df.columns]

if columnas_disponibles:
    plt.figure(figsize=(10, 6))
    
    #Graficas
    for col in columnas_disponibles:
        sns.histplot(df[col].dropna(), bins=30, kde=True, label=col, alpha=0.5)
    
    #Línea del promedio
    media_mhv = estadisticas['Media']
    plt.axvline(media_mhv, color='red', linestyle='--', linewidth=2, label=f'Promedio: {media_mhv:.2f}')
    
    #Configuración del gráfico
    plt.title('Comparación de Histogramas')
    plt.xlabel('Valor')
    plt.ylabel('Frecuencia')
    plt.legend()
    plt.show()
else:
    print("No hay columnas disponibles para graficar")
