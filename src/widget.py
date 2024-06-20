from src.masks import get_mask_account, get_mask_card_number

from datetime import datetime


def mask_account_card(cards_number: str) -> str:
    """Функция, маскирующая номер карты/счета"""

    if "Счет" in cards_number:
        mask_account = f"Счет {get_mask_account(cards_number[-20:])}"
        return mask_account

    else:
        card = get_mask_card_number(cards_number[-16:])
        mask_card = cards_number.replace(cards_number[-16:], str(card))
        return mask_card


def get_data(data: str) -> str:
    """Функция, возвращающая строку с датой"""

    date_it = datetime.strptime(data, format("%Y-%m-%dT%H:%M:%S.%f"))
    return date_it.strftime("%d.%m.%Y")


if __name__ == "__main__":
    print(mask_account_card("Счет 64686473678894779589"))
    print(get_data("2018-07-11T02:26:18.671407"))
