# EDA_Premier_League

Este repositorio contiene un análisis exploratorio de datos (EDA) de la temporada 2023/2024 de la Premier League. El objetivo principal es investigar estadísticas relevantes que influyen en la clasificación final de los equipos y evaluar la rentabilidad de ciertos mercados de apuestas deportivas, basándonos en los datos analizados.

## Contenido del Proyecto

El análisis se realiza principalmente en el archivo `main.ipynb`, y el repositorio está estructurado de la siguiente manera:

### Archivos y Carpetas

- **`main.ipynb`**: Notebook principal donde se realiza el análisis de datos de la temporada 2023/2024.  
  - Se analizan estadísticas como:
    - Rendimiento local y visitante.
    - Golaverage.
    - Número de goles marcados y recibidos.
    - Número de tiros y su efectividad.
    - Correlaciones entre estadísticas y puntos o clasificación final.
  - Evaluación de la rentabilidad en mercados de apuestas deportivas como:
    - Victoria local, empate o victoria visitante.  
    - Más de 2.5 goles.

- **Carpeta `src/`**:
  - **`data/`**: Contiene los datasets analizados en el proyecto.
  - **`img/`**: Imágenes generadas durante el análisis.
  - **`utils/`**: Archivos con las funciones utilizadas en el análisis.
  - **`notebooks/`**: Otros notebooks relacionados con el análisis.

## Objetivos del Análisis

1. Identificar correlaciones entre las estadísticas de los equipos y su desempeño en la clasificación final.
2. Evaluar la efectividad y rentabilidad de ciertos mercados de apuestas deportivas utilizando las estadísticas recopiladas.

## Cómo Usar Este Repositorio

1. **Clona el repositorio**:  

   git clone https://github.com/juanjofdez92/EDA_Premier_League.git  

2. **Instala las dependencias necesarias**:
   - Asegúrate de tener Python instalado y las librerías como `pandas`, `numpy`, `matplotlib`, y `seaborn`.  

3. **Ejecuta el Notebook principal**:
   - Abre `main.ipynb` en Jupyter Notebook, Jupyter Lab, o cualquier entorno compatible y ejecuta las celdas.

4. **Explora los resultados**:
   - Los resultados visuales y conclusiones están disponibles en el notebook principal, mientras que los datos procesados se encuentran en la carpeta `src/data`.

## Resultados Principales

- **Estadísticas y Correlaciones**:
  - El rendimiento como local es mayor que el rendimiento como visitante.  
  - El *goal average* es buen predictor de los posibles puntos obtenidos.  
  - Los tiros totales y la puntería (*tiros a puerta / tiros totales*) son mucho más importantes que la efectividad (*goles / tiros a puerta*).

- **Análisis de Mercados de Apuestas**:
  - Tiene rentabilidad apostar a los mejores equipos como local cuando juegan en casa.  
  - También tiene algo de rentabilidad apostar a los equipos como local, en general, pero no muy significativa.  
  - Los equipos que encajan más goles tienen mejor rentabilidad en el mercado de más de 2.5 goles que los equipos que marcan más goles.  

## Próximos Pasos

- Ampliar el análisis a otras temporadas para verificar consistencias en los hallazgos.  
- Incluir análisis de nuevos mercados de apuestas deportivas.  

## Contribuciones

¡Contribuciones y sugerencias son bienvenidas! Si encuentras algún error o tienes ideas para mejorar el análisis, no dudes en abrir un issue o enviar un pull request.

