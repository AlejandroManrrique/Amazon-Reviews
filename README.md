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

* Lenguajes de Programación: Utilizamos Python para el análisis de datos y la implementación de algoritmos de machine learning.
* Herramientas de Visualización: Empleamos bibliotecas como Matplotlib y Seaborn para visualizar los datos y los resultados del modelo.
* Google Cloud: Empleamos Google Cloud para el almacenamiento de datos y la ejecución de consultas en BigQuery, lo que nos permite acceder y procesar grandes conjuntos de datos de manera eficiente.
* Google Kubernetes Engine (GKE): Utilizamos Google Kubernetes Engine para gestionar el entorno de desarrollo y la ejecución de nuestros modelos de manera eficiente, aprovechando las capacidades de la capa gratuita de servicio de Google Cloud.
* Frameworks de Machine Learning: Implementaremos nuestro modelo utilizando bibliotecas como TensorFlow y Scikit-Learn para el entrenamiento y la evaluación del modelo.
* Bases de Datos: Implementaremos tanto bases de datos relacionales como no relacionales para almacenar y acceder a grandes volúmenes de datos históricos de clientes. Además, vamos a incorporar técnicas de carga incremental para gestionar eficientemente nuestros recursos y optimizar el rendimiento del sistema.

## Restricciones y Consideraciones:
El objetivo primordial de nuestro proyecto es desarrollar un modelo de recomendación que permita a los usuarios encontrar los productos de su preferencia, al mismo tiempo que contribuye al aumento de las ventas en Amazon. Sin embargo, es crucial tener en cuenta que la efectividad de este modelo está estrechamente vinculada a la calidad de los productos ofrecidos. A pesar de que podemos recomendar productos con altas calificaciones de calidad, no podemos prever imprevistos que puedan surgir en cualquier momento, como problemas con el proveedor o cambios en la calidad de los productos ofrecidos. La atención constante a estos factores es esencial para garantizar la satisfacción continua de los clientes y mantener la integridad del sistema de recomendación.

## Análisis de los datos 
Durante el análisis exhaustivo de los conjuntos de datos seleccionados, fue necesario investigar la distribución de las calificaciones de los productos en Amazon. Además, identificamos los meses con mayor potencial para las compras en el sitio web. También exploramos la relación entre la calificación de los productos y sus precios, así como la cantidad de compras en diferentes rangos de precio. Es importante señalar que, debido a la cantidad de datos disponibles, optamos por analizar una muestra representativa de cinco categorías de productos para cada análisis.

Para profundizar en lo mencionado anteriormente, examinemos la distribución de calificaciones por categoría (recordando que esto se hizo con una muestra de 5 categorías). Se observa que la gran mayoría de los productos vendidos en Amazon tienen una calificación de 5 estrellas. No obstante, es importante señalar que también existe un número significativo de calificaciones de 4 estrellas o menos.

La baja calificación de los productos puede deberse a varios factores, como la calidad del producto, problemas en el proceso de envío, discrepancias en tamaño o color, entre otros aspectos. Por esta razón, nuestro trabajo al desarrollar el sistema de recomendación es mitigar estos riesgos al seleccionar los productos recomendados.

![Image text](https://github.com/leidy7hernandez/Amazon-Reviews/blob/main/Imagenes/Distribuci%C3%B3n%20de%20Calificaciones%20por%20Categor%C3%ADa.png)

Queremos incrementar nuestras ventas en Amazon, por lo que resulta valioso entender en qué temporadas del año podemos aprovechar al máximo el sistema de recomendación que estamos desarrollando. El siguiente gráfico revela que los meses de Enero y Diciembre son los períodos en los que se realizan más compras en cada tipo de producto. Es importante señalar que esta conclusión se basa en la suposición de que el número de reseñas es equivalente al número de compras. Partimos de la premisa de que si un cliente deja una reseña, es porque ya ha adquirido el producto. Por esta razón, en el gráfico se muestra la cantidad de reviewerID (identificaciones de reseñas) en lugar de la cantidad de IDs de productos vendidos.

![Image text](https://github.com/leidy7hernandez/Amazon-Reviews/blob/main/Imagenes/Cantidad%20de%20reviews%20por%20mes.png)

Queremos que nuestro modelo de recomendación no solo aumente las ventas, sino también la satisfacción de los clientes. Para lograrlo, es crucial analizar cómo la calificación de los productos se comporta en relación con un factor que Amazon pueda controlar. Dado que tanto la calidad de los productos como las expectativas de los clientes están fuera de nuestro control, decidimos examinar la relación entre la calificación de los productos y su precio en la plataforma.

El siguiente gráfico muestra una tendencia interesante: los clientes tienden a otorgar una calificación de 5 estrellas a productos de bajo precio. Esto podría deberse a que sus expectativas eran moderadas debido al precio reducido, y al recibir el producto sin ninguna decepción, otorgan una calificación alta. Esta tendencia es algo que podemos aprovechar en nuestro modelo de recomendación.

![Image text](https://github.com/leidy7hernandez/Amazon-Reviews/blob/main/Imagenes/Gr%C3%A1fico%20de%20Dispersi%C3%B3n%20Price%20vs.%20Overall.png)v

Además, el gráfico también revela que no solo obtenemos una calificación de producto mejor a un precio más bajo, sino que también hay un aumento significativo en las ventas a precios más bajos. Dado que el modelo de negocio de Amazon implica obtener un porcentaje de cada venta en lugar de quedarse con el monto total, resulta mucho más beneficioso tener un gran volumen de ventas de productos asequibles en lugar de unas pocas ventas de productos costosos.

![Image text](https://github.com/leidy7hernandez/Amazon-Reviews/blob/main/Imagenes/Ventas%20en%20Relaci%C3%B3n%20al%20Precio%20por%20Rango.png)

## KPI's Planteados:

Basándonos en el análisis previamente presentado, hemos formulado KPIs estratégicos que pueden potenciar la posición de Amazon en el mercado, sin comprometer la satisfacción de nuestros clientes.

* Aumentar un 10% las ventas de productos con alta calificación pero bajo volumen de ventas: Esta estrategia se basa en la premisa de que los productos con muchas calificaciones positivas tienen un gran potencial de ventas. Al enfocarnos en estos artículos, esperamos aumentar nuestras ventas rápidamente.

* Incrementar las ventas de productos con bajo rendimiento, actualmente representando menos del 10% del total de ventas, para impulsar el crecimiento en el próximo semestre: Algunos productos no alcanzan su máximo potencial debido a limitaciones en su visibilidad. Al eliminar estas barreras, podemos hacer que estos productos sean más competitivos y, por ende, impulsar las ventas.

* Lograr un crecimiento del 15% en las ventas o recaudación de la categoría de menor rendimiento para el próximo año: Creemos firmemente en el potencial de todas las categorías de productos. Nuestra estrategia se centra en equilibrar las ventas y el interés del cliente en todas las categorías, evitando que alguna quede rezagada en nuestra plataforma de Amazon.

* Incrementar el volumen de ventas en un 3% mensual para los productos de bajo precio: Los productos con precios más bajos tienden a recibir mejores calificaciones. Aprovechamos esta tendencia para aumentar las ventas de estos artículos, beneficiándonos de su mayor satisfacción del cliente.

* Mejorar la satisfacción del cliente en cada categoría en un 10% anual: El objetivo principal es  convertir a Amazon en la principal plataforma mundial de compras. Para lograrlo, es esencial mantener altos niveles de satisfacción del cliente en todas las categorías. Evitar la concentración de la satisfacción en áreas específicas garantizará una amplia oferta de productos y una experiencia de compra positiva en todas las secciones de nuestro sitio, manteniendo nuestra competitividad a largo plazo.

## Conclusiones:
En resumen, nuestro objetivo es desarrollar un sistema de recomendación que beneficie tanto a Amazon como a sus clientes. La meta es mejorar las recomendaciones de productos de manera tan efectiva que se minimice la posibilidad de recibir calificaciones negativas. Creemos firmemente que al aumentar la satisfacción de los clientes, las ventas se incrementarán de forma significativa. Para alcanzar esta meta, aprovecharemos la tendencia de los clientes a comprar y calificar positivamente productos de menor valor. Además, daremos prioridad a los productos que ya cuentan con excelentes calificaciones, incorporándolos estratégicamente en nuestro sistema de recomendación. Estamos convencidos de que estas estrategias nos permitirán lograr un impacto positivo tanto en la experiencia del cliente como en el crecimiento de las ventas de Amazon.

## Equipo Responsable:
* Analista de Datos: Paul Andre Jauregui Arbieto
* Científicos de Datos: Alejandro Fabian Manrrique, Leidy Fernanda Hernandez Navarrete
* Ingenieros de Datos: Lautaro Ismael Paniagua, Marcelo Luis Alberto Peralta
