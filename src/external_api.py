import os
from typing import Any

import requests
from dotenv import load_dotenv


def get_amount_transaction_in_rub(transaction: dict) -> Any:
    """
    Функция, которая принимает на вход транзакцию и возвращает
    сумму транзакции в рублях. Если транзакция была в USD или
    EUR, через API конвертируется сумма операции в рубли по текущему курсу валюты.
    """
    try:
        amount = float(transaction["operationAmount"]["amount"])
        currency = transaction["operationAmount"]["currency"]["code"]
        if currency == "RUB":
            return amount
        else:
            load_dotenv()
            api_key = os.getenv("API_KEY")
            url = f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={currency}&amount={amount}"
            headers = {"apikey": api_key}
            response = requests.get(url, headers=headers)

            status_code = response.status_code
            if status_code == 200:
                data = response.json()
                return round(data["result"], 2)
            else:
                print(f"Запрос не был успешным. Возможная причина: {response.reason}")

    except (KeyError, TypeError, ValueError, requests.RequestException) as e:
        print(f"Error {e}")
        return 0.00


if __name__ == "__main__":
    transaction = {
        "id": 816266176,
        "state": "CANCELED",
        "date": "2018-06-24T00:46:32.422648",
        "operationAmount": {"amount": "60030.73", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод организации",
        "from": "МИР 6381702861749111",
        "to": "Счет 27804394774631586026",
    }
    print(get_amount_transaction_in_rub(transaction))
