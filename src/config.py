import os
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./ds_tools.db")

GITHUB_TOKEN = os.getenv("GITHUB_TOKEN", "")
PYPI_BASE_URL = "https://pypi.org/pypi"
HF_API_URL = "https://huggingface.co/api"
