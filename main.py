from fastapi import FastAPI
import pandas as pd
from sklearn.neighbors import NearestNeighbors
import re

app = FastAPI()

# Para leer el archivo parquet
categories = pd.read_parquet('API/categories.parquet')

@app.get("/")
def welcome():
    return {'descripción':'El objetivo de esta API es principalmete mostrar los resultados de un modelo de recomedación:',
            'def obtener_recomendaciones(producto_id : str)':'Dado un codigo de producto de Amazon (de las categorías Home_and_Kitchen, Arts_Crafts_and_Sewing, Appliances, AMAZON_FASHION y All_Beauty) devuelve una lista de recomendación de 5 productos de la misma categoría, de alta calificación y de precio similar.'}

@app.get('/obtener_recomendaciones/{producto_id}')
def obtener_recomendaciones(producto_id : str):
    producto_id = producto_id.lower()
    # Identificar la categoria del producto
    categoria = None
    for i in range(len(categories)):
        if categories['asin'][i] == producto_id:
            categoria = categories['category'][i]
            break
    
    # Identificar el nombre del archivo y abrirlo
    if categoria == None:
        return "Producto no encontrado en el conjunto de datos."
    
    nombre_archivo = f"API/{categoria}_data.parquet"
    archivo = pd.read_parquet(nombre_archivo)

    # Convertir las columnas de texto (categoría) a números usando codificación one-hot
    encoded = pd.get_dummies(archivo, columns=['category'])

    # Seleccionar las características para el modelo (todas except 'asin' y 'overall')
    features = encoded.drop(['asin', 'overall', 'product'], axis=1)

    # Normalizar las características para asegurar que todas tengan el mismo peso
    from sklearn.preprocessing import MinMaxScaler
    scaler = MinMaxScaler()
    features_scaled = scaler.fit_transform(features)

    # Inicializar el modelo de KNeighbors
    knn = NearestNeighbors(n_neighbors=6)  # Se establece en 6 para obtener los 5 vecinos más cercanos (incluyendo el propio artículo)

    # Ajustar el modelo
    knn.fit(features_scaled)

    # Verificar si el producto_id está presente en el DataFrame original
    if producto_id in encoded['asin'].values:
        # Encuentra los vecinos más cercanos
        producto_idx = encoded[encoded['asin'] == producto_id].index[0]
        distancia, indice = knn.kneighbors(features_scaled[producto_idx].reshape(1, -1))

        # Obtiene los índices de los vecinos (excluyendo el producto de referencia)
        indices_vecinos = indice.squeeze()[1:]

        # Filtra los vecinos por mejor calificación y menor precio
        vecinos_filtrados = archivo.iloc[indices_vecinos].sort_values(by=['overall', 'price']).head(5)
        vecinos_filtrados = vecinos_filtrados.reset_index(drop=True)
        vecinos_filtrados.index = vecinos_filtrados.index + 1

        for i in range(len(vecinos_filtrados)):
            return vecinos_filtrados['product']
    else:
        return "Producto no encontrado en el conjunto de datos."