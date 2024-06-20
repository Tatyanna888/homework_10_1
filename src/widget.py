from masks import get_mask_account, get_mask_card_number


def mask_account_card(cards_number: str) -> str:
    """Функция, маскирующая номер карты/счета"""

    if "Счет" in cards_number:
        mask_account = f"Счет {get_mask_account(cards_number[-20:])}"
        return mask_account

    else:
        card = get_mask_card_number(cards_number[-16:])
        mask_card = cards_number.replace(cards_number[-16:], card)
        return mask_card


if __name__ == "__main__":
    print(mask_account_card("Счет 64686473678894779589"))





# def get_data():
#
#     return

