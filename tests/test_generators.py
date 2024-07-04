import pytest

from src.generators import filter_by_currency, transaction_descriptions, card_number_generator


def test_filter_by_currency(transactions, currency):
    generator = filter_by_currency(transactions, "USD")
    assert next(generator) == {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572',
                               'operationAmount': {'amount': '9824.07', 'currency': {'name': 'USD', 'code': 'USD'}},
                               'description': 'Перевод организации', 'from': 'Счет 75106830613657916952',
                               'to': 'Счет 11776614605963066702'}
    generator = filter_by_currency(transactions, "RUB")
    assert next(generator) == {'id': 873106923, 'state': 'EXECUTED', 'date': '2019-03-23T01:09:46.296404',
                               'operationAmount': {'amount': '43318.34', 'currency': {'name': 'руб.', 'code': 'RUB'}},
                               'description': 'Перевод со счета на счет', 'from': 'Счет 44812258784861134719',
                               'to': 'Счет 74489636417521191160'}


def test_filter_by_wrong_currency(transactions, currency):
    generator = filter_by_currency(transactions, "EVRO")
    with pytest.raises(StopIteration):
        next(generator)


def test_filter_by_currency_empty(transactions, currency):
    generator = filter_by_currency([], "")
    with pytest.raises(StopIteration):
        next(generator)


def test_transaction_descriptions(transactions):
    generator = transaction_descriptions(transactions)
    assert next(generator) == "Перевод организации"
    assert next(generator) == "Перевод со счета на счет"
    assert next(generator) == "Перевод со счета на счет"
    assert next(generator) == "Перевод с карты на карту"
    assert next(generator) == "Перевод организации"


def test_transaction_descriptions_empty(transactions):
    generator = transaction_descriptions([])
    with pytest.raises(StopIteration):
        next(generator)


def test_card_number_generator(start, stop):
    generator = card_number_generator(1, 5)
    assert next(generator) == "0000 0000 0000 0001"
    assert next(generator) == "0000 0000 0000 0002"
    assert next(generator) == "0000 0000 0000 0003"
    assert next(generator) == "0000 0000 0000 0004"
    assert next(generator) == "0000 0000 0000 0005"
