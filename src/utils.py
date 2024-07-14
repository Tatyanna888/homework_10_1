import json


def get_transactions(path: str) -> list:
    """Функция, которая принимает на вход путь до JSON-файла и
    возвращает список словарей с данными о финансовых транзакциях"""
    try:
        with open(path, "r", encoding="utf-8") as operations_file:
            transactions = json.load(operations_file)

            if isinstance(transactions, list):
                return transactions
            else:
                return []

    except json.JSONDecodeError:
        print("Ошибка декодирования файла")
        return []
    except FileNotFoundError:
        print("Файл не найден")
        return []


if __name__ == "__main__":
    path = "../data/operations.json"
    print(get_transactions(path))
