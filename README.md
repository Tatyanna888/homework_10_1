# homework_10_1

## Описание:

Проект - это виджет, который показывает несколько последних успешных банковских операций клиента

## Установка:
1. Клонируйте репозиторий:
```
git@github.com:Tatyanna888/homework_10_1.git
```
2. Установите зависимости:
```
poetry install
poetry add --group dev pytest pytest-cov
```
## Примеры использования (код):

1. Модуль masks.py имеет две функции:
   - Функция маскировки номера карты - принимает на вход номер карты и возвращает ее маску. Номер карты замаскирован и 
   отображается в формате XXXX XX** **** XXXX. 
def get_mask_card_number(card_number: str) -> str | None:
   - Функция маскировки номера счета - принимает на вход номер счета и возвращает его маску. Номер счета замаскирован и 
   отображается в формате **XXXX.
def get_mask_account(account_number: str) -> str | None:
   Запускается из корневого модуля main.py.
      Созданы логеры. Реализована запись логов в одноименный файл с расширением .log в папку logs в корне проекта. 
   Формат записи лога включает метку времени, название модуля, уровень серьезности и сообщение, описывающее событие 
   или ошибку, которые произошли. Лог перезаписывается при каждом запуске приложения.
2. Модуль widget.py имеет две функции:
   - Функция общей маскировки карты и счета - принимает на вход только один аргумент — строку, которая состоит из 
   требуемых частей. Это может быть строка типа Visa Platinum 7000 7922 8960 6361, или Maestro 7000 7922 8960 6361, 
   или Счет 73654108430135874305. 
def mask_account_card(cards_number: str) -> str:
   - Функция преобразования даты - принимает на вход строку вида 2018-07-11T02:26:18.671407 и возвращает строку 
   с датой в виде 11.07.2018. 
def get_data(data: str) -> str:
3. Модуль processing.py имеет две функции:
   - Функция фильтрации операций по ключу state - принимает на вход список словарей и значение для ключа state 
   (опциональный параметр со значением по умолчанию EXECUTED) и возвращает новый список, содержащий только те словари, 
   у которых ключ state содержит переданное в функцию значение.
def filter_by_state(list_id: list, state: str = "EXECUTED") -> list:
   - Функция сортировки операций по дате - принимает на вход список словарей и возвращает новый список, в котором 
   исходные словари отсортированы по убыванию даты (ключ date). Функция принимает два аргумента, второй необязательный 
   задает порядок сортировки (убывание, возрастание).
def sort_by_date(list_id: list, is_reverse: bool = True) -> list:
4. Mодуль generators.py имеет три функции,  реализующие генераторы для обработки данных:
   - Функция, возвращающая итератор, который поочередно выдает транзакции, где валюта операции соответствует заданной 
   (например, USD) - принимает на вход список словарей, представляющих транзакции.
def filter_by_currency(transactions: List[Dict[str, Any]], currency: str) -> Generator[Dict[str, Any], None, None]:
   - Функция-генератор, возвращающая описание каждой операции по очереди - принимает список словарей с транзакциями.
def transaction_descriptions(transactions: List[Dict[str, Any]]) -> Generator[Any | None, None, None]:
   - Функция-генератор, возвращающая номера банковских карт в формате XXXX XXXX XXXX XXXX, где X — цифра номера карты. 
   Генератор может сгенерировать номера карт в заданном диапазоне от 0000 0000 0000 0001 до 9999 9999 9999 9999. 
   Генератор принимает начальное и конечное значения для генерации диапазона номеров.
5. Модуль decorators.py имеет декоратор:
   - log, который автоматически логирует вызов функции, а также ее результаты или возникшие ошибки. Декоратор принимает 
   необязательный аргумент filename, который определяет, куда будут записываться логи (в файл или в консоль). Если 
   filename задан, логи записываются в указанный файл. Если filename не задан, логи выводятся в консоль. Логирование 
   включает:
   Имя функции и результат выполнения при успешной операции.
   Имя функции, тип возникшей ошибки и входные параметры, если выполнение функции привело к ошибке.
6. Модуль utils.py содержит функцию, которая принимает на вход путь до JSON-файла и возвращает список словарей с 
   данными о финансовых транзакциях. Если файл пустой, содержит не список или не найден, функция возвращает пустой 
   список. 
def get_transactions(path: str) -> list:
   Файл с данными о финансовых транзациях operations.json находится в директории data/ в корне проекта. 
      Созданы логеры. Реализована запись логов в одноименный файл с расширением .log в папку logs в корне проекта. 
   Формат записи лога включает метку времени, название модуля, уровень серьезности и сообщение, описывающее событие 
   или ошибку, которые произошли. Лог перезаписывается при каждом запуске приложения.
7. Модуль external_api.py содержит функцию конвертации, которая принимает на вход транзакцию и возвращает сумму 
   транзакции (amount) в рублях, тип данных — float. Если транзакция была в USD или EUR, происходит обращение к 
   внешнему API для получения текущего курса валют и конвертации суммы операции в рубли. Для конвертации валюты 
   используется Exchange Rates Data API: https://apilayer.com/exchangerates_data-api.
   - Использованы переменные окружения из файла .env для сокрытия чувствительных данных (токен доступа для API). 
   - Создан шаблон файла .env.example для размещения в репозитории на GitHub.

## О тестировании:
Оценка покрытия кода составляет 83%. Отчет сгенерирован в папке htmlcov и храниться в файле с названием index.html.
Правила запуска тестов: запуск pytest удобнее всего производить из PyCharm. Для этого выполните следующие шаги: в окне 
Edit Configurations выберите pytest, укажите директорию с тестами и директорию проекта в целом.

## Использование:

1. Перейдите на страницу в вашем веб-браузере.
2. Создайте новую учетную запись или войдите существующей.

## Документация:

## Лицензия:
