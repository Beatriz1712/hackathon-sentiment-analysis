# 📊 Análisis de Sentimientos en Opiniones de Clientes Proyecto de Ciencia de Datos 

## 📌 Descripción del proyecto

Este proyecto implementa un modelo de clasificación supervisada para realizar análisis de sentimientos sobre opiniones de clientes (reseñas, comentarios y encuestas de satisfacción).

El objetivo es ayudar a áreas como Atención al Cliente, Marketing y Operaciones a entender rápidamente la percepción del cliente, clasificando los textos en tres categorías:

- ✅ Positivo
- ➖ Neutro
- ❌ Negativo

## 🎯 Objetivo

Desarrollar un pipeline de Procesamiento de Lenguaje Natural (NLP) que permita:

- Limpiar y preprocesar texto en español

- Transformar texto en variables numéricas mediante TF-IDF

- Entrenar un modelo supervisado de clasificación

- Evaluar el desempeño con métricas estándar

- Serializar el modelo para su reutilización

## 🧠 Tipo de problema
El principial reto que aborda este proyecto es la predicción de sentimientos a partir de texto no estructurado en español, utilizando técnicas de procesamiento de lenguaje natural y aprendizaje supervisado.

De igual forma consideramos que se necesitan dos modelos diferentes ya que las palabaras y expresiones que indican sentimientos positivos, negativos o neutros pueden variar significativamente según el lenguaje.


## 📁 Estructura del proyecto

hackathon-sentiment-analysis
- resources
  - base_datos_tweets_ingles.csv
- models
  - modelo_sentimiento_español.pkl
  - modelo_sentimiento_ingles.pkl
  - tfidf_vectorizer_español.pkl
  - tfidf_vectorizer_ingles.pkl
  - pipeline_sentimiento_español.pkl
  - pipeline_sentimiento_ingles.pkl
- datascience
  - notebooks
    - Notebook_modelo_español.ipynb
    - Notebook_modelo_ingles.ipynb
- README.md


## 🗃️ CONJUNTO DE DATOS

### Conjunto de datos para modelo en español
Los datos utilizados para entrenar al modelo en español provienen de  [Hugging Face](https://huggingface.co/datasets/alexcom/analisis-sentimientos-textos-turisitcos-mx-polaridad/viewer/default/train?p=5). Esta base de datos contine opiniones de clientes en español sobre el servicio en de la industria turística en México, etiquetadas con una reseña del 1 al 5, estas puntuaciones se agruparon en las tres categorías de sentimiento anteriormente mencionadas de la siguiente manera:

- Positivo: puntuaciones 4 y 5
- Neutro: puntuación 3  
- Negativo: puntuaciones 1 y 2

La distribución de clases en el conjunto de datos es la siguiente:
- Positivo: 72% 
- Neutro: 14%
- Negativo: 14%


### Conjunto de datos para modelo en inglés
El conjunto de datos que se utilizo para el entrenamiento del modelo en inglés proviene de [Kaggle](https://www.kaggle.com/datasets/crowdflower/twitter-airline-sentiment). Este conjunto de datos contiene opiniones de clientes en inglés sobre aerolíneas, además de una columna de las etiquetas del sentimiento las cuales son positive, negative y neutral. 

La distribución de las clases del conjunto de datos es la siguiente:
- Positivo: 16%
- Neutro: 21%
- Negativo: 63%


## 🔍 EXPLORACIÓN Y LIMPIEZA DE DATOS (EDA)
Se realizó una exploración inicial del conjunto de datos para entender su estructura y calidad. Se identificaron y manejaron los siguientes aspectos:
- Valores nulos o faltantes
- Distribución de clases
- Formato de texto

## 🧹PREPROCESAMIENTO DE TEXTO
El texto se preprocesó mediante las siguientes técnicas:
1. Conversión a minúsculas
2. Eliminación de puntuación y caracteres especiales
3. Eliminación de stopwords en español e inglés
4. Tokenización
5. Eliminación de palabras irrelevantes o muy frecuentes
6. Eliminación de URLs y menciones

De igual forma para la base de datos en inglés se realizó una lematización para reducir las palabras a su forma base.

## 🔢 VECTORIZACIÓN DE TEXTO (TF-IDF)

El texto limpio se transformó en variables numéricas mediante TF-IDF (Term Frequency – Inverse Document Frequency), utilizando:

- Unigramas y bigramas
- Normalización L2
- Suavizado IDF
- Eliminación de términos muy frecuentes y muy raros.


## 🤖 Modelos utilizados
En ambos casos se probaron dos modelos:
- Regresión Logística
- Multinomial Naive Bayes

Se seleccionó el modelo de Regresión Logística para ambos idiomas debido a su mejor desempeño en las métricas evaluadas.


## 📈 EVALUACIÓN DEL MODELO
El modelo fue evaluado usando las siguientes métricas:

- Exactitud (Accuracy)
- Precisión (Precision)
- Sensibilidad (Recall)
- Puntuación F1

Además, se utilizó un informe de clasificación para analizar el desempeño por clase.

Estas métricas permitieron validar la efectividad del modelo en la clasificación de sentimientos en opiniones de clientes.

Las métricas obtenidas en el conjunto de prueba del modelo en español fueron:
- Exactitud: 75.5%
- Precisión: 77.6%
- Sensibilidad: 75.5%
- F1-Score: 76.2%


Las métricas obtenidas en el conjunto de prueba del modelo en inglés fueron:
- Exactitud: 88.1%
- Precisión: 89.3%
- Sensibilidad: 88.1%
- F1-Score: 88.6%

## 💾 SERIALIZACIÓN DEL MODELO

Para permitir su reutilización en producción, se serializaron:

- El modelo entrenado
- El vectorizador TF-IDF
- Un pipeline completo (TF-IDF + modelo)

*Se utilizó la librería joblib.

## ⚙️ TECNOLOGIAS Y LIBRERIAS UTILIZADAS

- Python 3
- Pandas
- Numpy
- nltk
- scikit-learn
- matplotlib 
- seaborn
- joblib
- re
- Jupyter Notebook
- Hugging Face Datasets
- Kaggle
