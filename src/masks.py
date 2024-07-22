import logging


logger = logging.getLogger("masks")
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler("logs/masks.log", "w", encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def get_mask_card_number(card_number: str) -> str | None:
    """Функция, возвращающая маску номера карты"""

    if card_number.isdigit() and len(card_number) == 16:
        logger.info("Получаем маскированный номер банковской карты")
        return f"{card_number[:4]} {card_number[4:6]}{"*" * 2} {"*" * 4} {card_number[12:]}"
    else:
        logger.error("Введены некорректные данные")
        return None


def get_mask_account(account_number: str) -> str | None:
    """Функция, возвращающая маску номера счета"""

    if account_number.isdigit() and len(account_number) == 20:
        logger.info("Получаем маскированный номер банковского счета")
        return f"{'*' * 2}{account_number[-4::]}"
    else:
        logger.error("Введены некорректные данные")
        return None
