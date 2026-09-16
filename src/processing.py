def filter_by_state(data_list: list[dict], state: str = "EXECUTED") -> list[dict]:
    """Фильтрует список словарей по значению ключа 'state'."""
    filtered_data = []

    for item in data_list:
        if item.get("state") == state:
            filtered_data.append(item)

    return filtered_data

def sort_by_date(data_list: list[dict], descending: bool = True) -> list[dict]:
    """Сортирует список словарей по дате."""
    return sorted(data_list, key=lambda x: x["date"], reverse=descending)