import csv
import logging

import pandas as pd

logger = logging.getLogger("utils")
file_handler = logging.FileHandler("../logs/utils.log", "w", encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s - %(filename)s - %(levelname)s - %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)


def read_csv(file_name: str) -> list[dict]:
    """Функция, которая считывает данные из файла CVS и преобразовывает в список словарей"""
    logger.info("Открываем файл CVS для чтения")
    with open(file_name, "r", encoding="utf-8") as file:
        reader = csv.reader(file, delimiter=";")
        header = next(reader)
        result = []
        logger.info("Преобразовываем данные файла CVS в список словарей")
        for row in reader:
            row_dict = {
                "id": row[header.index("id")],
                "state": row[header.index("state")],
                "date": row[header.index("date")],
                "operationAmount": {
                    "amount": row[header.index("amount")],
                    "currency": {
                        "name": row[header.index("currency_name")],
                        "code": row[header.index("currency_code")],
                    },
                },
                "description": row[header.index("description")],
                "from": row[header.index("from")],
                "to": row[header.index("to")],
            }
            result.append(row_dict)
    logger.info("Получаем список финансовых транзакций из файла CVS")
    return result


def read_xlsx(file_name: str) -> list[dict]:
    """Функция, которая считывает данные из файла XLSX и преобразовывает в список словарей"""
    logger.info("Открываем файл Excel для чтения")
    df = pd.read_excel(file_name)
    logger.info("Преобразовываем данные файла Excel в список словарей")
    result = df.apply(
        lambda row: {
            "id": row["id"],
            "state": row["state"],
            "date": row["date"],
            "operationAmount": {
                "amount": row["amount"],
                "currency": {"name": row["currency_name"], "code": row["currency_code"]},
            },
            "description": row["description"],
            "from": row["from"],
            "to": row["to"],
        },
        axis=1,
    ).tolist()
    logger.info("Получаем список финансовых транзакций из файла XLSX")
    return result
