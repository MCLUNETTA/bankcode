import logging
import os

# Автоматически создаем папку logs, если ее еще нет
os.makedirs("logs", exist_ok=True)

logger = logging.getLogger("masks")
logger.setLevel(logging.DEBUG)

file_handler = logging.FileHandler("logs/masks.log", mode="w", encoding="utf-8")
file_handler.setLevel(logging.DEBUG)

formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(formatter)

if not logger.handlers:
    logger.addHandler(file_handler)


def get_mask_card_number(card_number: str) -> str:
    """Маскирует номер банковской карты."""
    logger.info(f"Запрос на маскирование номера карты: {card_number}")
    if not card_number.isdigit() or len(card_number) != 16:
        logger.error(f"Некорректный номер карты: {card_number}")
        return ""

    masked = f"{card_number[:4]} {card_number[4:6]}** **** {card_number[12:]}"
    logger.info("Маскирование карты успешно выполнено")
    return masked


def get_mask_account(account_number: str) -> str:
    """Маскирует номер банковского счета."""
    logger.info(f"Запрос на маскирование номера счета: {account_number}")
    if not account_number.isdigit() or len(account_number) < 4:
        logger.error(f"Некорректный номер счета: {account_number}")
        return ""

    masked = f"**{account_number[-4:]}"
    logger.info("Маскирование счета успешно выполнено")
    return masked
