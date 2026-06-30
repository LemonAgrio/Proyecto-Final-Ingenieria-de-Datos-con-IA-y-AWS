<img width="1279" height="799" alt="image" src="https://github.com/user-attachments/assets/a1575797-e6a5-4fec-b606-d07b48462f20" /># 🚀 End-to-End AWS Data Pipeline: Data Lake Ingestion & Crypto Analytics

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

<img width="1279" height="799" alt="image" src="https://github.com/user-attachments/assets/21859252-9f4b-42ed-8c72-0da089b7766d" />


2. **Capa de Catálogo:** Un AWS Glue Crawler escanea de forma automática la zona cruda para inferir el esquema y registrar los metadatos en el AWS Glue Data Catalog (`fintech_db`).

<img width="1279" height="799" alt="image" src="https://github.com/user-attachments/assets/fc372ee7-b3e6-490f-8d44-09825f8ae2b7" />

<img width="1279" height="799" alt="image" src="https://github.com/user-attachments/assets/174cace9-993b-417e-968e-ca0953be7433" />

<img width="1279" height="799" alt="image" src="https://github.com/user-attachments/assets/6663b966-b1cb-4408-b965-9b46863c0dab" />

<img width="1279" height="799" alt="image" src="https://github.com/user-attachments/assets/9ff1a7a4-a84a-40ef-bffd-9535b216a3e2" />

<img width="1279" height="799" alt="image" src="https://github.com/user-attachments/assets/3212aa4b-78e2-4725-8da2-a0760035e10b" />

<img width="1278" height="799" alt="image" src="https://github.com/user-attachments/assets/61f2d3d0-f410-4d45-8c10-1ca8be325611" />

<img width="1278" height="707" alt="image" src="https://github.com/user-attachments/assets/bfbefaaa-c40c-4cf3-8c5d-0135e24a51fa" />

2.1 **Capa de catálogo:** Se creo un crawler "processed" con la finalidad de ailar el entorno,automatizar el descubrimiento de esquemas sobre el almacenamiento columnar "PARQUET", esto permitirá que amazon athena exponga la tabla optimizada, limpia y tipada correctamente, sin interferir con el historico de la carpeta (raw)

<img width="1279" height="799" alt="image" src="https://github.com/user-attachments/assets/19814b3e-956f-4d29-9a5b-9be2fe4b6a57" />

<img width="1279" height="799" alt="image" src="https://github.com/user-attachments/assets/a656dfde-2756-4d0f-833b-e12ffa40b5fa" />

<img width="1279" height="799" alt="image" src="https://github.com/user-attachments/assets/41b11659-86f0-4cd9-86bf-ebb97a54417d" />

<img width="1277" height="799" alt="image" src="https://github.com/user-attachments/assets/41491455-4a10-4479-aaf0-e62fe940813b" />

<img width="1279" height="799" alt="image" src="https://github.com/user-attachments/assets/6248d2bb-7e7f-4bb3-b258-aa4d526040d9" />

3. **Capa de Procesamiento (ETL):** Un AWS Glue Job ejecuta la lógica de negocio encargada del casteo explícito de tipos (forzando métricas financieras a `Double`), limpieza de nulos y renombrado de columnas con caracteres especiales, traduciendo las acciones visuales a un script nativo de PySpark.

<img width="1279" height="799" alt="image" src="https://github.com/user-attachments/assets/291c8684-7880-4c6d-adb3-326ddff756c7" />

<img width="1279" height="799" alt="image" src="https://github.com/user-attachments/assets/d32566eb-86b5-43bc-9809-d8980d09abef" />

<img width="1279" height="799" alt="image" src="https://github.com/user-attachments/assets/dde87941-2f0d-4788-9f45-a26a37c4f1d1" />


4. **Capa de Almacenamiento (Processed Zone):** Los datos transformados se escriben nuevamente en Amazon S3 comprimidos en formato columnar **Parquet (Snappy)**.

<img width="1279" height="799" alt="image" src="https://github.com/user-attachments/assets/e23103f1-d69a-4a71-add6-9ebd73b0fb52" />


<img width="1279" height="799" alt="image" src="https://github.com/user-attachments/assets/012491a1-7e18-4036-b17f-4d9acb48116b" />


5. **Capa de Consumo y Analítica:** Se utiliza un segundo Crawler para catalogar la capa optimizada y permitir que el equipo de negocio explote los datos mediante consultas estructuradas de alto rendimiento vía SQL en **Amazon Athena**.

<img width="1279" height="799" alt="image" src="https://github.com/user-attachments/assets/cdedb8ad-f51e-422c-af14-49a39b36d56d" />
