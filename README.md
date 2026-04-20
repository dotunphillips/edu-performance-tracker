# Global Education Performance Tracker 🎓

## 📝 Problem Statement
Policymakers and global development organizations often struggle to answer a fundamental question: **"Are financial investments in education actually translating into higher literacy outcomes?"** Publicly available datasets from the World Bank contain the answers but are stored in "long-format" structures that are difficult for standard BI tools to visualize efficiently. This project builds a cloud-native ELT pipeline to centralize, transform, and visualize these indicators, allowing for a direct comparison between government expenditure and literacy rates across decades.

## 🏗️ Architecture
The project follows a modern Data Engineering lifecycle:
* **Infrastructure:** Terraform (IaC) to manage Google Cloud Storage and BigQuery.
* **Ingestion:** Python (Batch) extracting World Bank data to Parquet files and uploading to GCS.
* **Data Warehouse:** Google BigQuery, utilizing **Partitioning** (by Year) and **Clustering** (by Country Code).
* **Transformation:** **dbt** to pivot raw indicators into an analytical-ready "wide" format.
* **Orchestration:** Scripted workflow utilizing the `uv` package manager.
* **Visualization:** Streamlit dashboard with interactive Plotly components.

---

## 🚀 Getting Started

### 1. Prerequisites
* Python 3.12+ (using `uv` for package management)
* Google Cloud Platform account and a project ID.
* Terraform installed.

### 2. Infrastructure Setup
```bash
cd terraform
terraform init
terraform apply
```

### 3. Data Ingestion
```bash
# Install dependencies
uv sync

# Run ingestion script
uv run ingest_data.py
```

### 4. Transformations (dbt)
```bash
cd dbt_edu
uv run dbt deps
uv run dbt run
```

Note: Ensure your ```~/.dbt/profiles.yml``` is configured for BigQuery with the ```us-central1 location```.

### 5. Dashboard
```bash
uv run streamlit run app.py
```
## 📊 Data Warehouse Optimization
To maximize query performance and minimize costs:
* **Partitioning:** The `fact_education` table is partitioned by `year`. This allows the Streamlit dashboard to fetch specific time-ranges without scanning the entire dataset.
* **Clustering:** Data is clustered by `country_code`. This ensures that when a user selects a specific country in the dashboard, BigQuery only reads the relevant blocks of data.

## 🛠️ Project Evolution & Uniqueness
While this project follows the core architecture of the Data Engineering Zoomcamp, it features a unique implementation focused on Global Education Economics. The custom dbt logic to pivot disparate World Bank indicators into a synchronized analytical dataset was developed specifically for this use case to bridge the gap between raw data and actionable policy insights.