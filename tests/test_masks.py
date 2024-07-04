from src.masks import get_mask_card_number, get_mask_account


def test_get_mask_card_number(card_number):
    assert get_mask_card_number(card_number) == "7000 79** **** 6361"



def test_get_mask_account(account_number):
    assert get_mask_account(account_number) == "**4305"
