# Global Crowdsourced Price Comparison Pipeline

## Problem Description

Understanding the cost of living across different countries is critical for economic research, 
policy-making, and development planning. However, comparing prices across countries is challenging 
due to differences in currencies, data formats, and data availability.

This project builds an end-to-end data engineering pipeline that ingests, cleans, and analyzes 
**crowdsourced household goods and services price data** from 4 countries — **South Africa, 
Philippines, Nigeria, and Brazil** — collected during a World Bank pilot study (December 2015 
to August 2016).

The pipeline answers the key question:
> **What is the average expenditure (in USD) for household goods and services across these countries, 
> and how do they compare?**

The source data covers **162 household good and service items** across categories including food, 
clothing, health, transport, education, and more. It contains over **1.2 million price observations** 
accompanied by rich metadata including GPS coordinates, timestamps, outlet identifiers, and brand information.

## Data Source
World Bank Crowdsourced Price Data Pilot  
https://datacatalog.worldbank.org/search/dataset/0042083

## Architecture
Source (World Bank) → Kestra (ingest) → GCS Bronze (raw CSV) → PySpark (clean) → GCS Silver (parquet) → BigQuery Silver → DBT (transform) → BigQuery Gold (analytical)

## Tools Used
- **Terraform** — GCP infrastructure provisioning (GCS buckets, BigQuery datasets)
- **Docker & Kestra** — workflow orchestration and data ingestion
- **PySpark** — data cleaning and transformation
- **Google Cloud Storage** — data lake (Bronze/Silver layers)
- **BigQuery** — data warehouse
- **DBT** — SQL transformations for Gold layer

## Setup

### Prerequisites
- Google Cloud account with billing enabled
- Docker & Docker Compose
- Python 3.12+
- Terraform

### Getting Started
1. Clone the repo
2. Create a GCP project and download your service account JSON key
3. Create `.env` in the `Docker/` directory
4. Run Terraform to provision GCP resources
5. Start Kestra and run ingestion flows
6. Run Spark cleaning script
7. Run DBT to transform data into Gold layer
