variable "project" {
  description = "Project ID"
  default     = "tactile-anthem-485519-v6"
}

variable "region" {
  description = "Region"
  default     = "us-central1"
}

variable "gcs_bucket_name" {
  description = "My Storage Bucket Name"
  default     = "edu-analytics-lake-dp"
}

variable "bq_dataset_name" {
  description = "My BigQuery Dataset Name"
  default     = "education_data_all"
}