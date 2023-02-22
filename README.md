# **Data Engineering Lifecycle with Google Cloud Platform**

![Google Cloud](https://img.shields.io/badge/GoogleCloud-%234285F4.svg?style=for-the-badge&logo=google-cloud&logoColor=white)  ![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white) ![Apache Kafka](https://img.shields.io/badge/Apache%20Kafka-000?style=for-the-badge&logo=apachekafka)  ![Postgres](https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white)  ![Terraform](https://img.shields.io/badge/terraform-%235835CC.svg?style=for-the-badge&logo=terraform&logoColor=white)  ![Prefect](https://img.shields.io/badge/Prefect-%23ffffff.svg?style=for-the-badge&logo=prefect&logoColor=white)

This repository contains a sample data engineering lifecycle that uses Google Cloud Platform and tools such as Google Storage:Data Lake, BigQuery, Terraform, Docker, SQL, Prefect, dbt, Spark, and Kafka. This README file describes the workflow and the tools used in the project.
Workflow

## **Proposed Architecture**
---
![Architect Diagram](https://github.com/keincoffee/de_course/blob/main/images/architecture/arch_2.png?raw=true)
---
---
## **Data Engineering Lifecycle**

### **1. Data ingestion**

The data ingestion phase involves ingesting data from various sources and loading it into the Data Lake. The Data Lake is a centralized repository that stores all the raw data. In this phase, we use Kafka for real-time data streaming and batch ingestion using Google Cloud Storage.

### **2. Data storage**

The Data Lake stores all the raw data in its original format. The data can be stored in various formats such as JSON, CSV, Avro, or Parquet. Google Cloud Storage is used as the storage medium for the Data Lake.

### **3. Data processing**

In the data processing phase, we use tools like Spark to process and transform the data stored in the Data Lake. Spark is a fast and powerful framework for distributed processing of large datasets. We can use Spark to clean, enrich, and transform the data.

### **4. Data modeling**

In the data modeling phase, we use dbt to build data models on top of the processed data. dbt is a popular tool used for data modeling, where we define the relationships between different tables and create a star schema for analytics.

### **5. Data warehousing**

The data warehousing phase involves loading the data into BigQuery, a serverless data warehouse. We can use SQL to query the data and perform ad-hoc analysis.

### **6. Data orchestration**

In the data orchestration phase, we use Prefect to orchestrate the entire data engineering pipeline. Prefect is a modern workflow orchestration tool that allows us to define complex workflows as code.

### **7. Infrastructure as Code**

To manage the infrastructure, we use Terraform. Terraform is an open-source infrastructure as code tool that enables us to define, deploy, and manage infrastructure on Google Cloud Platform.

### **8. Containerization**

Finally, we containerize the entire data engineering pipeline using Docker. Docker enables us to create reproducible and portable environments for our data engineering workflow.
Tools Used

    - Google Cloud Storage: Storage medium for the Data Lake.
    - BigQuery: Serverless data warehouse for data warehousing.
    - Terraform: Infrastructure as code tool for managing the infrastructure.
    - Docker: Containerization tool for creating reproducible and portable environments.
    - SQL: Querying language for data warehousing and ad-hoc analysis.
    - Prefect: Workflow orchestration tool for defining complex workflows as code.
    - dbt: Data modeling tool for building data models on top of the processed data.
    - Spark: Distributed processing framework for processing and transforming data.
    - Kafka: Streaming and batch ingestion tool for ingesting data from various sources.

## **Conclusion**
---

This repository provides an overview of a data engineering lifecycle that uses various tools provided by Google Cloud Platform. By following this workflow, we can build a scalable, robust, and maintainable data engineering pipeline that can handle large volumes of data efficiently.
