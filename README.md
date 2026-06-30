# 🚀 End-to-End AWS Data Pipeline: Data Lake Ingestion & Crypto Analytics

![AWS](https://img.shields.io/badge/AWS-%23232F3E.svg?style=for-the-badge&logo=amazon-aws&logoColor=white)
![Apache Spark](https://img.shields.io/badge/Apache%20Spark-F15A24?style=for-the-badge&logo=apachespark&logoColor=white)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![SQL](https://img.shields.io/badge/sql-003B57?style=for-the-badge&logo=sqlite&logoColor=white)

## 📝 Descripción del Proyecto
Este repositorio contiene una solución de **Ingeniería de Datos Serverless** robusta e integral implementada en Amazon Web Services (AWS). El objetivo del pipeline es automatizar el ciclo de vida completo de los datos financieros: desde la ingesta de un dataset histórico de mercado de Bitcoin (BTC) en formato plano (CSV) proveniente de Kaggle, pasando por su transformación distribuida mediante la abstracción visual de PySpark en AWS Glue Studio, hasta su optimización en almacenamiento columnar (Parquet) para consultas analíticas avanzadas de alta velocidad y bajo costo en Amazon Athena.

---

## 💼 Escenario de Negocio
Una plataforma de corretaje (*brokerage*) de criptomonedas requiere centralizar el histórico de transacciones de mercado de Bitcoin con el fin de que su equipo de analistas financieros ejecute reportes de volatilidad, calcule variaciones de precios y detecte tendencias operativas. 

Ejecutar estas consultas analíticas pesadas directamente sobre los sistemas transaccionales en vivo afectaría críticamente el rendimiento de la aplicación hacia los clientes. Por lo tanto, se diseñó este **Data Lake** desacoplado para asegurar la escalabilidad, la gobernanza y la eficiencia analítica del negocio.

---

## 🏗️ Arquitectura del Sistema

El flujo de datos se diseñó bajo el marco de buena arquitectura de AWS (*AWS Well-Architected Framework*), desacoplando por completo el almacenamiento del cómputo:

1. **Capa de Ingesta (Raw Zone):** El archivo crudo original (`BTC-Daily.csv`) se deposita en la ruta de aterrizaje inicial dentro de un bucket de Amazon S3.

<img width="1279" height="753" alt="image" src="https://github.com/user-attachments/assets/e4a31999-e116-4920-ad7e-990a2aafbe4c" />

3. **Capa de Catálogo:** Un AWS Glue Crawler escanea de forma automática la zona cruda para inferir el esquema y registrar los metadatos en el AWS Glue Data Catalog (`fintech_db`).
4. **Capa de Procesamiento (ETL):** Un AWS Glue Job ejecuta la lógica de negocio encargada del casteo explícito de tipos (forzando métricas financieras a `Double`), limpieza de nulos y renombrado de columnas con caracteres especiales, traduciendo las acciones visuales a un script nativo de PySpark.
5. **Capa de Almacenamiento (Processed Zone):** Los datos transformados se escriben nuevamente en Amazon S3 comprimidos en formato columnar **Parquet (Snappy)**.
6. **Capa de Consumo y Analítica:** Se utiliza un segundo Crawler para catalogar la capa optimizada y permitir que el equipo de negocio explote los datos mediante consultas estructuradas de alto rendimiento vía SQL en **Amazon Athena**.

---

## 📁 Estructura Recomendada del Repositorio

```text
├── data/
│   └── BTC-Daily.csv          # Muestra representativa del dataset histórico crudo
├── scripts/
│   └── glue_etl_job.py        # Script PySpark/Spark SQL generado por AWS Glue Job
├── sql/
│   └── athena_queries.sql     # Consultas analíticas ejecutadas en la capa de consumo
├── images/
│   ├── s3_bucket.png          # Evidencia del almacenamiento crudo y procesado en S3
│   ├── glue_pipeline.png      # Captura del historial de ejecución (SUCCEEDED) en Glue
│   └── athena_results.png     # Resultados exitosos de la consulta SQL final de Bitcoin
└── README.md                  # Documentación principal del proyecto
