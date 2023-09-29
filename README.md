# Amazon-Reviews

## Alcance
En nuestra consultora de análisis de datos, nos hemos embarcado en la ambiciosa tarea de mejorar la satisfacción de los clientes de Amazon. Para lograr este objetivo, hemos desarrollado un modelo de recomendación avanzado basado en datos históricos. Este informe ofrece una visión integral de nuestra participación en este proyecto, destacando los recursos tecnológicos que hemos aplicado para alcanzar nuestras metas.

Nuestra misión se centra en mejorar la experiencia de compra de los clientes de Amazon, aprovechando datos históricos y análisis avanzado. Nos enfrentamos al desafío de entender las preferencias y necesidades de los clientes para ofrecerles recomendaciones personalizadas y relevantes.

## Obtención de los datos
Se nos fue entregado un conjunto de 58 archivos, que comprenden 24 tablas junto con sus respectivos archivos de metadatos. Estos fueron tomados de: https://drive.google.com/drive/folders/1KT0-qPYJmlr6w2o41sjJlPXCZ3SkHbN0

## Objetivos:

* Análisis Exhaustivo: En este proyecto, hemos realizado un análisis profundo de los datos históricos de los clientes con el objetivo de comprender los patrones de comportamiento y preferencias. Es importante tener en cuenta que el análisis que presentamos hasta ahora es una instantánea y puede estar sujeto a modificaciones a medida que avanza el proyecto y surgen nuevas necesidades.

* Modelo Predictivo: Implementaremos un modelo predictivo basado en machine learning para predecir las futuras preferencias de los clientes y anticiparnos a sus necesidades.

* Recomendaciones Personalizadas: Utilizando algoritmos de recomendación y análisis de datos, crearemos un sistema que ofrece sugerencias de productos adaptadas a cada cliente, maximizando así su satisfacción y fidelidad.

  ### NOTA:

  Para garantizar el seguimiento de nuestros objetivos, hemos establecido un sistema estructurado en nuestro equipo de trabajo. Hemos implementado un tablero en Trello y un diagrama de Gantt para organizar nuestras tareas y plazos. Esta estrategia nos permite mantener el proyecto en curso de manera organizada y estable, asegurando un progreso constante y significativo.
  
  Pueden acceder a estos recursos a través de los siguientes enlaces:

  Trello: https://trello.com/b/Kgi5pWaL/ftdata14

  Diagrama de Gannt: https://docs.google.com/spreadsheets/d/1dcGiQUqLDPKduMvMLM2_R9wrHaRnFCkA0q8Ig_fmWsU/edit#gid=279598197

## Recursos Tecnológicos:

* Lenguajes de Programación: Utilizamos Python y R para el análisis de datos y la implementación de algoritmos de machine learning.

* Herramientas de Visualización: Empleamos bibliotecas como Matplotlib y Seaborn para visualizar los datos y los resultados del modelo.

* Frameworks de Machine Learning: Implementaremos nuestro modelo utilizando bibliotecas como TensorFlow y Scikit-Learn para el entrenamiento y la evaluación del modelo.

* Bases de Datos: Implementaremos tanto bases de datos relacionales como no relacionales para almacenar y acceder a grandes volúmenes de datos históricos de clientes. Además, vamos a incorporar técnicas de carga incremental para gestionar eficientemente nuestros recursos y optimizar el rendimiento del sistema.

## Restricciones y Consideraciones:
El objetivo primordial de nuestro proyecto es desarrollar un modelo de recomendación que permita a los usuarios encontrar los productos de su preferencia, al mismo tiempo que contribuye al aumento de las ventas en Amazon. Sin embargo, es crucial tener en cuenta que la efectividad de este modelo está estrechamente vinculada a la calidad de los productos ofrecidos. A pesar de que podemos recomendar productos con altas calificaciones de calidad, no podemos prever imprevistos que puedan surgir en cualquier momento, como problemas con el proveedor o cambios en la calidad de los productos ofrecidos. La atención constante a estos factores es esencial para garantizar la satisfacción continua de los clientes y mantener la integridad del sistema de recomendación.

## Análisis de los datos 
Durante el análisis exhaustivo de los conjuntos de datos seleccionados, fue necesario investigar la distribución de las calificaciones de los productos en Amazon. Además, identificamos los meses con mayor potencial para las compras en el sitio web. También exploramos la relación entre la calificación de los productos y sus precios, así como la variación de precios en diferentes categorías. Es importante señalar que, debido a la cantidad de datos disponibles, optamos por analizar una muestra representativa de cinco categorías de productos para cada análisis.

Para profundizar en lo mencionado anteriormente, examinemos la distribución de calificaciones por categoría (recordando que esto se hizo con una muestra de 5 categorías). Se observa que la gran mayoría de los productos vendidos en Amazon tienen una calificación de 5 estrellas. No obstante, es importante señalar que también existe un número significativo de calificaciones de 4 estrellas o menos.

La baja calificación de los productos puede deberse a varios factores, como la calidad del producto, problemas en el proceso de envío, discrepancias en tamaño o color, entre otros aspectos. Por esta razón, nuestro trabajo al desarrollar el sistema de recomendación es mitigar estos riesgos al seleccionar los productos recomendados.

![Image text](https://github.com/leidy7hernandez/Siniestros-Viales/blob/d48e2d3ae80a5e504060f7fec08bcde26afc252e/Imagenes/Tasa%20anual%20de%20Homicidios%20Viales.png)

## Equipo Responsable:
Analista de Datos: Paul Andre Jauregui Arbieto
Científicos de Datos: Alejandro Fabian Manrrique, Leidy Fernanda Hernandez Navarrete
Ingenieros de Datos: Lautaro Ismael Paniagua, Marcelo Luis Alberto Peralta
