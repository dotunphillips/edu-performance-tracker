terraform {
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "5.6.0"
    }
  }
}

provider "google" {
  project = var.project
  region  = var.region
}

# 1. Data Lake (GCS)
resource "google_storage_bucket" "data_lake" {
  name          = var.gcs_bucket_name
  location      = var.region
  force_destroy = true
}

# 2. BigQuery Dataset
resource "google_bigquery_dataset" "dataset" {
  dataset_id = var.bq_dataset_name
  location   = var.region
}