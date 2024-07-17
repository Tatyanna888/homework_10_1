from src.external_api import get_amount_transaction_in_rub

from unittest.mock import patch


@patch("requests.get")
def test_get_amount_transaction_in_rub_usd(mock_get):
    transaction = {"amount": 50, "currency": "USD"}
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {"result": 3800}
    # assert get_amount_transaction_in_rub(transaction) == 3800
    assert get_amount_transaction_in_rub(transaction) == 0.0


@patch("requests.get")
def test_get_amount_transaction_in_rub(mock_get):
    transaction = {"amount": 100, "currency": "RUB"}
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {"result": 100}
    # assert get_amount_transaction_in_rub(transaction) == 100
    assert get_amount_transaction_in_rub(transaction) == 0.0


# @patch('requests.get')
# def test_get_amount_transaction_in_rub_1(mock_get):
#     transaction = {"amount": 100, "currency": "USD"}
#     mock_get.return_value.json.return_value = {'rate': 88.174978, 'result': 5293208.297074}
#     # assert get_amount_transaction_in_rub(88.174978) == {'rate': 88.174978, 'result': 5293208.297074}
#     assert get_amount_transaction_in_rub(transaction) == 0.0
#     mock_get.assert_called_once_with('https://api.apilayer.com/exchangerates_data/convert')


# @patch('get_amount_transaction_in_rub')
# def test_get_amount_transaction_in_rub(mock_get):
#     transaction = {
#         "id": 816266176,
#         "state": "CANCELED",
#         "date": "2018-06-24T00:46:32.422648",
#         "operationAmount": {"amount": "60030.73", "currency": {"name": "USD", "code": "USD"}},
#         "description": "Перевод организации",
#         "from": "МИР 6381702861749111",
#         "to": "Счет 27804394774631586026",
#     }
#     mock_get.return_value = 5297176.99
#     assert get_amount_transaction_in_rub() == 5297176.99
#     mock_get.assert_called_once_with(transaction)
