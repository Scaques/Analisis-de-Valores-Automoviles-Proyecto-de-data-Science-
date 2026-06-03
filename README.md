# Sistema de Tasación Inteligente de Vehículos Usados (Chile)

Este proyecto implementa un pipeline completo de Ciencia de Datos para recolectar, limpiar, analizar y modelar información del mercado automotriz en Chile. Utiliza un algoritmo de Machine Learning (*Random Forest*) para predecir el valor comercial de un vehículo basándose en sus características clave: año, kilometraje y marca.

## Arquitectura del Proyecto

El proyecto está diseñado siguiendo una estructura modular y limpia, separando la ingesta de datos, el análisis exploratorio y el modelado predictivo:

```text
proyecto-data-science/
├── data/
│   ├── raw/                  # Datos crudos generados/extraídos
│   └── processed/            # Datos limpios y normalizados para ML
├── notebooks/
│   ├── 1_cleaning_and_eda.ipynb  # Limpieza de datos y visualización analítica
│   └── 2_model_training.ipynb    # Entrenamiento y evaluación del modelo
├── src/
│   └── scraper.py            # Módulo de simulación e ingesta de datos
├── .gitignore                # Filtro de archivos para el repositorio
└── requirements.txt          # Dependencias del proyecto
```

## Tecnologías Utilizadas
Lenguaje: Python 3.10+

Manipulación de Datos: Pandas, NumPy

Visualización: Matplotlib, Seaborn

Machine Learning: Scikit-Learn (Pipelines, RandomForestRegressor, OneHotEncoder)

Entorno: Jupyter Lab / VS Code Notebooks

## Fases del Desarrollo
### 1. Ingesta y Simulación de Datos (src/scraper.py)
 Módulo encargado de generar una base de datos de 1,000 registros que emula las imperfecciones reales del mercado chileno (valores nulos, texto mal formateado, presencia de emojis 🔥 y variaciones en la declaración de 			unidades como Km o kms).
### 2. Limpieza y Análisis Exploratorio - EDA (notebooks/1_cleaning_and_eda.ipynb)
* Normalización de Texto: Eliminación de caracteres especiales y estandarización de nombres de marcas.
* Casteo de Datos: Conversión de cadenas de texto de precios ($12.500.000) y kilometrajes a variables numéricas puras.
* Análisis Visual: Estudio de la curva de depreciación de los vehículos según su año e impacto del kilometraje mediante gráficos legibles en escalas monetarias de millones de pesos (CLP).
### 3. Entrenamiento del Modelo (notebooks/2_model_training.ipynb)
* Estrategia Robustez: Uso de ColumnTransformer y Pipeline para aislar el preprocesamiento (One-Hot Encoding para variables categóricas) y evitar la fuga de datos (Data Leakage).
* Validación: División del dataset en 80% entrenamiento y 20% pruebas (Train/Test Split).
* Algoritmo: Ensamble de árboles de decisión (RandomForestRegressor).
  
## Resultados y Métricas
El modelo base arrojó las siguientes métricas de evaluación en el conjunto de datos de prueba (datos que la IA nunca vio durante el entrenamiento):
* Coeficiente de Determinación ($R^2$): 0.63 (El modelo explica el 63% de la variabilidad de los precios del mercado simulado).
* Error Absoluto Medio (MAE): Permite cuantificar en pesos chilenos la desviación promedio de las predicciones frente a los valores reales de tasación.

## Ejemplo de Uso (Tasación Interactiva)
El pipeline final permite ingresar un vehículo arbitrario y obtener una estimación comercial inmediata:
* Entrada: Toyota, Año 2018, 85.000 Km.
* Resultado del Modelo: Tasación automatizada en pesos chilenos basada en tendencias de depreciación calculadas.

## Próximos Pasos para Optimización (Roadmap)
Para escalar el proyecto hacia un entorno de producción con un $R^2$ superior, se contemplan las siguientes mejoras técnicas:
1. Ajuste de Hiperparámetros: Implementar GridSearchCV para optimizar la estructura interna de los árboles del Random Forest.
2. Modelos Avanzados: Evaluar algoritmos de Gradient Boosting como XGBoost o LightGBM.
3. Nuevas Características: Incorporar el modelo específico del auto (ej: Swift vs Grand Vitara) y la región geográfica de venta para capturar dinámicas locales de oferta y demanda.

## Cómo Ejecutar el Proyecto Localmente
1. Clonar el repositorio:
```text
git clone https://github.com/Scaques/proyecto-data-science.git
cd proyecto-data-science
```

2. Configurar el entorno virtual e instalar dependencias:
```text
python -m venv .venv
.venv\Scripts\Activate.ps1   # En Windows (PowerShell)
pip install -r requirements.txt
```

3. Generar los datos base:
```text
python src/scraper.py
```

4. Abrir los cuadernos de trabajo:
```text
jupyter lab
```
Ejecutar en orden 1_limpieza.ipynb y luego 2_entrenamiento_modelo.ipynb.
