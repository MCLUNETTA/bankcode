from typing import Iterator


def filter_by_currency(transactions: list[dict], currency_code: str = "USD") -> Iterator[dict]:
    """Фильтрует транзакции по коду валюты и возвращает итератор."""
    for transaction in transactions:
        # Добираемся до кода валюты внутри словаря
        operation_amount = transaction.get("operationAmount", {})
        currency = operation_amount.get("currency", {})
        if currency.get("code") == currency_code:
            yield transaction


def transaction_descriptions(transactions: list[dict]) -> Iterator[str]:
    """Генератор, который возвращает описание каждой операции по очереди."""
    for transaction in transactions:
        yield transaction.get("description", "")


def card_number_generator(start: int, stop: int) -> Iterator[str]:
    """Генерирует номера карт в формате XXXX XXXX XXXX XXXX в заданном диапазоне."""
    for number in range(start, stop + 1):
        # Превращаем число в 16-значную строку с нулями впереди (напр. 0000000000000001)
        formatted_number = f"{number:016d}"
        # Делим на 4 блока по 4 цифры и соединяем пробелами
        yield f"{formatted_number[:4]} {formatted_number[4:8]} {formatted_number[8:12]} {formatted_number[12:]}"
