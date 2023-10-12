from fastapi import FastAPI
import pandas as pd
from sklearn.neighbors import NearestNeighbors
import re
from sklearn.preprocessing import MinMaxScaler

app = FastAPI()

# Para leer el archivo parquet
categories = pd.read_parquet('API/categories.parquet')

# Crear un diccionario para buscar la categoría por asin
categoria_por_asin = dict(zip(categories['asin'], categories['category']))

# Cargar y preprocesar los datos una vez fuera de la función
categorias = set(categories['category'])
archivos_por_categoria = {}

for categoria in categorias:
    nombre_archivo = categoria + "_data.parquet"
    archivo = pd.read_parquet(nombre_archivo)
    encoded = pd.get_dummies(archivo, columns=['category'])
    features = encoded.drop(['asin', 'overall', 'product'], axis=1)
    scaler = MinMaxScaler()
    features_scaled = scaler.fit_transform(features)
    knn = NearestNeighbors(n_neighbors=6)
    knn.fit(features_scaled)
    archivos_por_categoria[categoria] = {
        "archivo": archivo,
        "encoded": encoded,
        "knn": knn,
        "features_scaled": features_scaled
    }

@app.get("/")
def welcome():
    return {'descripción':'El objetivo de esta API es principalmete mostrar los resultados de un modelo de recomedación:',
            'def obtener_recomendaciones(producto_id : str)':'Dado un codigo de producto de Amazon (de las categorías Home_and_Kitchen, Arts_Crafts_and_Sewing, Appliances, AMAZON_FASHION y All_Beauty) devuelve una lista de recomendación de 5 productos de la misma categoría, de alta calificación y de precio similar.'}

@app.get('/obtener_recomendaciones/{producto_id}')
def obtener_recomendaciones(producto_id):
    producto_id = producto_id.lower()
    categoria = categoria_por_asin.get(producto_id)
    if categoria is None:
        return "Producto no encontrado en el conjunto de datos."

    archivo = archivos_por_categoria[categoria]["archivo"]
    encoded = archivos_por_categoria[categoria]["encoded"]
    features_scaled = archivos_por_categoria[categoria]["features_scaled"]
    knn = archivos_por_categoria[categoria]["knn"]

    if producto_id in encoded['asin'].values:
        producto_idx = encoded[encoded['asin'] == producto_id].index[0]
        distancia, indice = knn.kneighbors(features_scaled[producto_idx].reshape(1, -1))
        indices_vecinos = indice.squeeze()[1:]
        vecinos_filtrados = archivo.iloc[indices_vecinos].sort_values(by=['overall', 'price']).head(5)
        vecinos_filtrados = vecinos_filtrados.reset_index(drop=True)
        vecinos_filtrados.index = vecinos_filtrados.index + 1
        return vecinos_filtrados
    else:
        return "Producto no encontrado en el conjunto de datos."