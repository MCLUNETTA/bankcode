import os
from typing import Any
from src.utils import get_financial_data, read_transactions_from_csv, read_transactions_from_excel
from src.processing import process_bank_search


def main() -> None:
    """Основная логика работы программы по управлению банковскими транзакциями."""
    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")
    print("Выберите необходимый пункт меню:")
    print("1. Получить информацию о транзакциях из JSON-файла")
    print("2. Получить информацию о транзакциях из CSV-файла")
    print("3. Получить информацию о транзакциях из XLSX-файла")

    choice = input("Пользователь: ").strip()

    data: list[dict[str, Any]] = []

    if choice == "1":
        print("Программа: Для обработки выбран JSON-файл.")
        file_path = os.path.join("data", "operations.json")
        data = get_financial_data(file_path if os.path.exists(file_path) else "operations.json")
    elif choice == "2":
        print("Программа: Для обработки выбран CSV-файл.")
        file_path = os.path.join("data", "transactions.csv")
        data = read_transactions_from_csv(file_path if os.path.exists(file_path) else "transactions.csv")
    elif choice == "3":
        print("Программа: Для обработки выбран XLSX-файл.")
        file_path = os.path.join("data", "transactions_excel.xlsx")
        data = read_transactions_from_excel(file_path if os.path.exists(file_path) else "transactions_excel.xlsx")
    else:
        print("Программа: Неверный выбор. Завершение программы.")
        return

    # Фильтрация по статусу
    valid_statuses = ["EXECUTED", "CANCELED", "PENDING"]
    while True:
        print("\nПрограмма: Введите статус, по которому необходимо выполнить фильтрацию.")
        print(f"Доступные для фильтровки статусы: {', '.join(valid_statuses)}")
        status_input = input("Пользователь: ").strip().upper()

        if status_input in valid_statuses:
            print(f'Программа: Операции отфильтрованы по статусу "{status_input}"')
            data = [t for t in data if str(t.get("state", "")).upper() == status_input]
            break
        else:
            print(f'Программа: Статус операции "{status_input}" недоступен.')

    # Сортировка по дате
    print("\nПрограмма: Отсортировать операции по дате? Да/Нет")
    sort_date = input("Пользователь: ").strip().lower()
    if sort_date in ["да", "yes", "д"]:
        print("Программа: Отсортировать по возрастанию или по убыванию?")
        sort_order = input("Пользователь: ").strip().lower()
        reverse_flag = "убыван" in sort_order
        data = sorted(data, key=lambda x: str(x.get("date", "")), reverse=reverse_flag)

    # Рублевые транзакции
    print("\nПрограмма: Выводить только рублевые транзакции? Да/Нет")
    only_rub = input("Пользователь: ").strip().lower()
    if only_rub in ["да", "yes", "д"]:
        data = [
            t for t in data
            if (
                t.get("operationAmount", {}).get("currency", {}).get("code") == "RUB"
                or t.get("currency_code") == "RUB"
            )
        ]

    # Фильтрация по определенному слову в описании
    print("\nПрограмма: Отфильтровать список транзакций по определенному слову в описании? Да/Нет")
    filter_word = input("Пользователь: ").strip().lower()
    if filter_word in ["да", "yes", "д"]:
        print("Программа: Введите слово для поиска в описании:")
        search_query = input("Пользователь: ").strip()
        data = process_bank_search(data, search_query)

    # Вывод результатов
    print("\nПрограмма: Распечатываю итоговый список транзакций...\n")
    if not data:
        print("Программа: Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")
        return

    print(f"Всего банковских операций в выборке: {len(data)}\n")

    for t in data:
        date_raw = t.get("date", "")
        formatted_date = f"{date_raw[8:10]}.{date_raw[5:7]}.{date_raw[0:4]}" if len(date_raw) >= 10 else date_raw
        description = t.get("description", "Без описания")

        op_amount = t.get("operationAmount", {})
        amount = op_amount.get("amount", t.get("amount", "0"))
        currency = op_amount.get("currency", {}).get("name", op_amount.get("currency", {}).get("code",
                                                                                               t.get("currency_name",
                                                                                                     "руб.")))

        print(f"{formatted_date} {description}")
        print(f"Сумма: {amount} {currency}\n")


if __name__ == "__main__":
    main()
