import pytest

from src.masks import get_mask_card_number, get_mask_account


def test_get_mask_card_number(card_number):
    assert get_mask_card_number(card_number) == "7000 79** **** 6361"


def test_get_mask_card_number_empty(card_number):
    assert get_mask_card_number("") == None


def test_get_mask_card_number_not_string(card_number):
    with pytest.raises(AttributeError):
        get_mask_card_number(4552548)



def test_get_mask_account(account_number):
    assert get_mask_account(account_number) == "**4305"


def test_get_mask_account_empty(account_number):
    assert get_mask_account("") == None


def test_get_mask_account_empty_not_string(account_number):
    with pytest.raises(AttributeError):
        get_mask_account(2555.032)
