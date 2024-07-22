import json

import pytest

from src.utils import get_transactions
from unittest.mock import mock_open, patch


def test_get_transactions_empty():
    assert get_transactions("") == []


def test_get_transactions():
    mock_transactions = [
        {
            "id": 441945886,
            "state": "EXECUTED",
            "date": "2019-08-26T10:50:58.294041",
            "operationAmount": {
                "amount": "31957.58",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод организации",
            "from": "Maestro 1596837868705199",
            "to": "Счет 64686473678894779589"
        }
    ]

    mock_file = json.dumps(mock_transactions)

    with patch("builtins.open", mock_open(read_data=mock_file)):
        result = get_transactions("../data/operations.json")
        assert result == mock_transactions


def test_get_transactions_1():
    mock_transactions = []

    mock_file = json.dumps(mock_transactions)

    with patch("builtins.open", mock_open(read_data=mock_file)):
        result = get_transactions("../data/operations.json")
        assert result == [mock_transactions]


# def test_get_transactions_not_list():
#     transactions = "1258489963"
#     with pytest.raises(json.JSONDecodeError, match="Ошибка декодирования файла"):
#         get_transactions("../data/operations.json")
#
#
# def test_get_transactions_not_file():
#     mock_transactions = []
#     with pytest.raises(FileNotFoundError, match="Файл не найден"):
#         get_transactions("data/operations.json")