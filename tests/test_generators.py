import pytest
from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


@pytest.fixture
def sample_transactions():
    """Тестовые транзакции с разными валютами."""
    return [
        {
            "id": 1,
            "operationAmount": {"currency": {"code": "USD"}},
            "description": "Перевод организации",
        },
        {
            "id": 2,
            "operationAmount": {"currency": {"code": "RUB"}},
            "description": "Перевод со счета на счет",
        },
        {
            "id": 3,
            "operationAmount": {"currency": {"code": "USD"}},
            "description": "Перевод с карты на карту",
        },
    ]


# --- Тесты filter_by_currency ---

def test_filter_by_currency_usd(sample_transactions):
    result = list(filter_by_currency(sample_transactions, "USD"))
    assert len(result) == 2
    assert result[0]["id"] == 1
    assert result[1]["id"] == 3


def test_filter_by_currency_not_found(sample_transactions):
    result = list(filter_by_currency(sample_transactions, "EUR"))
    assert len(result) == 0


def test_filter_by_currency_empty():
    result = list(filter_by_currency([], "USD"))
    assert len(result) == 0


# --- Тесты transaction_descriptions ---

def test_transaction_descriptions(sample_transactions):
    gen = transaction_descriptions(sample_transactions)
    assert next(gen) == "Перевод организации"
    assert next(gen) == "Перевод со счета на счет"
    assert next(gen) == "Перевод с карты на карту"


def test_transaction_descriptions_empty():
    gen = transaction_descriptions([])
    with pytest.raises(StopIteration):
        next(gen)


# --- Тесты card_number_generator ---

@pytest.mark.parametrize(
    "start, stop, expected",
    [
        (1, 2, ["0000 0000 0000 0001", "0000 0000 0000 0002"]),
        (5, 5, ["0000 0000 0000 0005"]),
    ],
)
def test_card_number_generator(start, stop, expected):
    result = list(card_number_generator(start, stop))
    assert result == expected


def test_card_number_generator_formatting():
    card = next(card_number_generator(1, 1))
    assert len(card) == 19  # 16 цифр + 3 пробела
    assert card == "0000 0000 0000 0001"
