# Global Crowdsourced Price Comparison Pipeline

## Problem Description

Understanding the cost of living across different countries is critical for economic research, policy-making, and development planning. However, comparing prices across countries is challenging due to differences in currencies, data formats, and data availability.

This project builds an end-to-end data engineering pipeline that ingests, cleans, and analyzes **crowdsourced household goods and services price data** from 4 countries — **South Africa, Philippines, Nigeria, and Brazil** — collected during a World Bank pilot study (December 2015 to August 2016).

The pipeline answers the key question:
> **What is the average expenditure (in USD) for household goods and services across these countries, and how do they compare?**

## Data Source
World Bank Crowdsourced Price Data Pilot  
https://datacatalog.worldbank.org/search/dataset/0042083

## Architecture
Source (World Bank) → Kestra (ingest) → GCS Bronze → PySpark (clean) → GCS Silver → BigQuery → DBT → Gold

## Tools Used
- **Terraform** — GCP infrastructure provisioning
- **Docker & Kestra** — workflow orchestration and data ingestion
- **PySpark** — data cleaning and transformation
- **Google Cloud Storage** — data lake (Bronze/Silver layers)
- **BigQuery** — data warehouse
- **DBT** — SQL transformations for Gold layer

## Setup

### Prerequisites
- Google Cloud account with billing enabled
- Docker & Docker Compose
- Terraform

### Step 1 - GCP Setup
1. Create a GCP project in the GCP console
2. Create a Service Account with **Owner** role
3. Download the SA JSON key

### Step 2 - Configure .env
Create Docker/.env with the following variables:

```env
# Path to your SA JSON key
GOOGLE_APPLICATION_CREDENTIALS=/path/to/your/sa-key.json

# Base64 encoded SA JSON key
# Run: base64 -w 0 /path/to/sa-key.json
SECRET_GCP_KEY=<base64_encoded_sa_key>

# Base64 encoded GCP Project ID
# Run: echo -n "your-project-id" | base64
SECRET_PROJECT_ID=<base64_encoded_project_id>

# Base64 encoded GCP Region
# Run: echo -n "europe-west1" | base64
SECRET_REGION=<base64_encoded_region>
```

### Step 3 - Provision GCP Infrastructure
```bash
cd terraform
terraform init
terraform apply
```

### Step 4 - Start Kestra
```bash
cd Docker
docker compose --env-file .env up
```

### Step 5 - Run the Pipeline
1. Open Kestra UI at http://localhost:8080
2. Login with admin@kestra.io / Admin1234!
3. Run the full_pipeline flow under data_engineering namespace
4. The flow will automatically:
   - Download data from World Bank
   - Upload to GCS Bronze
   - Clean with PySpark
   - Save to GCS Silver
   - Load into BigQuery

