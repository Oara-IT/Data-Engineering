from google.cloud import bigquery
from google.oauth2 import service_account
import os

credentials = service_account.Credentials.from_service_account_file(
    "/home/oara-it/Data-Engineering/stunning-ruler-493803-j1-8a2b20987da5.json"
)

client = bigquery.Client(credentials=credentials, project="stunning-ruler-493803-j1")

for name in ["zaf", "phl", "nga", "bra"]:
    print(f"Loading {name} to BigQuery...")
    
    uri = f"gs://silver-stunning-ruler-493803-j1/cleaned/{name}/*.parquet"
    table_id = f"stunning-ruler-493803-j1.silver_dataset.{name}_data"
    
    job_config = bigquery.LoadJobConfig(
        source_format=bigquery.SourceFormat.PARQUET,
        write_disposition=bigquery.WriteDisposition.WRITE_TRUNCATE
    )
    
    load_job = client.load_table_from_uri(uri, table_id, job_config=job_config)
    load_job.result()
    
    print(f"{name} loaded!")

print("All done!")