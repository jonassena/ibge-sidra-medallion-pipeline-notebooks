# Configurações do pipeline IBGE SIDRA - Tabela 6579

SIDRA_API_URL = "https://apisidra.ibge.gov.br/values/t/6579/n3/all/p/all/v/all"

BASE_PATH = "dbfs:/mnt/medallion"

RAW_PATH = f"{BASE_PATH}/raw/sidra/t6579"
BRONZE_PATH = f"{BASE_PATH}/bronze/sidra/t6579"
SILVER_PATH = f"{BASE_PATH}/silver/sidra/t6579"
GOLD_PATH = f"{BASE_PATH}/gold/sidra/t6579"
