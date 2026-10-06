from unittest.mock import patch

from src.external_api import convert_to_rub


def test_convert_rub():
    """Тест возврата суммы без запроса к API, если валюта RUB."""
    transaction = {"operationAmount": {"amount": "100.0", "currency": {"code": "RUB"}}}
    assert convert_to_rub(transaction) == 100.0


@patch("requests.get")
def test_convert_usd_success(mock_get):
    """Тест успешной конвертации USD в RUB с помощью мака requests.get."""
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {"result": 7500.0}

    transaction = {"operationAmount": {"amount": "100.0", "currency": {"code": "USD"}}}
    assert convert_to_rub(transaction) == 7500.0


def test_convert_invalid_transaction():
    """Тест обработки некорректных данных транзакции."""
    assert convert_to_rub({}) == 0.0
