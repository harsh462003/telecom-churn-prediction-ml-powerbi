"""Project configuration (paths and constants)."""

from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
DATA_PATH = PROJECT_ROOT / "data" / "WA_Fn-UseC_-Telco-Customer-Churn.csv"
SAMPLE_DATA_PATH = PROJECT_ROOT / "data" / "sample_telco.csv"
OUTPUTS_DIR = PROJECT_ROOT / "outputs"
REPORT_FIG_DIR = PROJECT_ROOT / "reports" / "figures"
