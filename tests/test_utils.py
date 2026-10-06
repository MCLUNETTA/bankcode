import json
import logging
from unittest.mock import mock_open, patch

from src.utils import get_financial_data


def test_get_financial_data_valid():
    """Тест успешного чтения корректного JSON файла."""
    data = [{"id": 1, "amount": 100}]
    with patch("builtins.open", mock_open(read_data=json.dumps(data))):
        with patch("os.path.exists", return_value=True):
            assert get_financial_data("dummy_path.json") == data


def test_get_financial_data_file_not_found():
    """Тест возврата пустого списка, если файл не существует."""
    with patch("os.path.exists", return_value=False):
        assert get_financial_data("invalid_path.json") == []


def test_get_financial_data_invalid_json():
    """Тест обработчика ошибок при поврежденном JSON."""
    with patch("builtins.open", mock_open(read_data="invalid json")):
        with patch("os.path.exists", return_value=True):
            assert get_financial_data("dummy_path.json") == []


def test_get_financial_data_logging(caplog):
    """Тест проверяет, что при отсутствии файла записывается ERROR в лог."""
    with caplog.at_level(logging.ERROR):
        get_financial_data("non_existent_file.json")
        assert "Файл не найден по пути: non_existent_file.json" in caplog.text
