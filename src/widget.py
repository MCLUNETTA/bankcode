import masks

def mask_account_card(info: str) -> str:
    """Маскирует номер карты или счета в зависимости от типа."""
    parts = info.split()
    number = parts[-1]
    name = " ".join(parts[:-1])

    if name.lower().startswith("счет"):
        masked_number = masks.get_mask_account(number)
    else:
        masked_number = masks.get_mask_card_number(number)

    return f"{name} {masked_number}"


def get_date(date_string: str) -> str:
    """Преобразует строку с датой в формат ДД.ММ.ГГГГ."""
    date_part = date_string.split("T")[0]
    year, month, day = date_part.split("-")
    return f"{day}.{month}.{year}"