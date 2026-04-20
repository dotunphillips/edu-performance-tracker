import os
import pandas as pd
from google.cloud import bigquery
from google.cloud import storage

# --- CONFIGURATION ---
PROJECT_ID = "tactile-anthem-485519-v6"
BUCKET_NAME = "edu-analytics-lake-dp"
SOURCE_TABLE = "bigquery-public-data.world_bank_intl_education.international_education"

def extract_and_upload():
    client = bigquery.Client(project=PROJECT_ID)
    
    print(f"🔍 Fetching Education Indicators from {SOURCE_TABLE}...")
    
    # Selecting key metrics: Literacy Rate and Govt Expenditure on Education
    query = f"""
    SELECT 
        country_name, 
        country_code, 
        indicator_name, 
        indicator_code, 
        year, 
        value
    FROM `{SOURCE_TABLE}`
    WHERE indicator_code IN ('SE.ADT.LITR.ZS', 'SE.XPD.TOTL.GD.ZS')
      AND year >= 2010
    """
    
    # Load into DataFrame
    df = client.query(query).to_dataframe()
    
    # Save as Parquet locally
    local_file = "raw_education_data.parquet"
    df.to_parquet(local_file, index=False)
    print(f"✅ Downloaded {len(df)} rows to {local_file}")

    # Upload to GCS
    storage_client = storage.Client(project=PROJECT_ID)
    bucket = storage_client.bucket(BUCKET_NAME)
    blob = bucket.blob(f"raw/{local_file}")
    
    print(f"🚀 Uploading to gs://{BUCKET_NAME}/raw/{local_file}...")
    blob.upload_from_filename(local_file)
    print("✨ Ingestion Complete!")

if __name__ == "__main__":
    extract_and_upload()