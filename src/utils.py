import json
import os


def get_financial_data(path: str) -> list[dict]:
    """Читает финансовые данные из JSON файла."""
    if not os.path.exists(path):
        return []
    try:
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
            return data if isinstance(data, list) else []
    except (json.JSONDecodeError, Exception):
        return []
