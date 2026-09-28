import pytest
from src.processing import filter_by_state, sort_by_date


@pytest.fixture
def sample_transactions():
    """Фикстура с тестовым списком транзакций."""
    return [
        {"id": 1, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 2, "state": "CANCELED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 3, "state": "EXECUTED", "date": "2019-08-26T10:50:58.294041"},
        {"id": 4, "state": "PENDING", "date": "2019-07-03T18:35:29.512364"},
    ]


@pytest.fixture
def empty_transactions():
    """Фикстура для пустого списка."""
    return []


def test_filter_by_state_executed(sample_transactions):
    result = filter_by_state(sample_transactions, state="EXECUTED")
    assert len(result) == 2
    assert all(item["state"] == "EXECUTED" for item in result)


def test_filter_by_state_canceled(sample_transactions):
    result = filter_by_state(sample_transactions, state="CANCELED")
    assert len(result) == 1
    assert result[0]["state"] == "CANCELED"


def test_filter_by_state_default(sample_transactions):
    result = filter_by_state(sample_transactions)
    assert len(result) == 2


def test_filter_by_state_empty(empty_transactions):
    assert filter_by_state(empty_transactions) == []


def test_sort_by_date(sample_transactions):
    result = sort_by_date(sample_transactions)
    assert isinstance(result, list)
    assert len(result) == len(sample_transactions)


def test_sort_by_date_empty(empty_transactions):
    assert sort_by_date(empty_transactions) == []
