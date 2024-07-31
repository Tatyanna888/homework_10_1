import json
import logging

logger = logging.getLogger("utils")
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler("../logs/utils.log", "w", encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def get_transactions(path: str) -> list:
    """Функция, которая принимает на вход путь до JSON-файла и
    возвращает список словарей с данными о финансовых транзакциях"""
    try:
        logger.info("Через указанный путь открываем JSON-файл для чтения")
        with open(path, "r", encoding="utf-8") as operations_file:
            transactions_list = json.load(operations_file)

            if isinstance(transactions_list, list):
                logger.info("Получаем список финансовых транзакций")
                return transactions_list
            else:
                logger.error("Файл пустой, нет данных")
                return []

    except json.JSONDecodeError:
        logger.error("Ошибка декодирования файла")
        print("Ошибка декодирования файла")
        return []
    except FileNotFoundError:
        logger.error("Файл не найден")
        print("Файл не найден")
        return []


if __name__ == "__main__":
    path = "../data/operations.json"
    print(get_transactions(path))
