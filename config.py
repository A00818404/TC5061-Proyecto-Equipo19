from pathlib import Path

# Directorio donde se encuentra este archivo.
PROJECT_ROOT = Path(__file__).resolve().parent

DATA_DIR = PROJECT_ROOT / "data"
RAW_DIR = DATA_DIR / "raw"
INTERIM_DIR = DATA_DIR / "interim"
PROCESSED_DIR = DATA_DIR / "processed"

REFERENCES_DIR = PROJECT_ROOT / "references"
MANIFEST_PATH = REFERENCES_DIR / "data_manifest.json"

DATA_SCHEMA_VERSION = "1.0.0"
CSV_ENCODING = "utf-8-sig"
PARQUET_COMPRESSION = "snappy"