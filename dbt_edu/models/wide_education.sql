{{ config(materialized='table') }}

WITH base AS (
    SELECT * FROM {{ source('raw_data', 'fact_education') }}
)

SELECT
    country_name,
    country_code,
    year,
    -- Pivoting the long indicators into clean columns for Streamlit
    MAX(CASE WHEN indicator_code = 'SE.ADT.LITR.ZS' THEN value END) AS literacy_rate,
    MAX(CASE WHEN indicator_code = 'SE.XPD.TOTL.GD.ZS' THEN value END) AS govt_expenditure
FROM base
GROUP BY 1, 2, 3
HAVING literacy_rate IS NOT NULL OR govt_expenditure IS NOT NULL