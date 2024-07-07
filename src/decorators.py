from functools import wraps
from typing import Any, Callable


def log(filename: Any = None) -> Callable:
    """Декораторб логирующий начало и конец выполнения функции, ее результаты или возникшие ошибки,
    принимающий необязательный аргумент filename и определяющий, куда будут записываться логи
    (в файл или в консоль)"""

    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            try:
                result = func(*args, **kwargs)
                log_message = f"{func.__name__} ok\n"

            except Exception as e:
                result = None
                log_message = f"{func.__name__} error: {e}. Inputs: {args}, {kwargs} \n"
            if filename:
                with open(filename, "a", encoding="utf-8") as file:
                    file.write(log_message)
            else:
                print(log_message)
            return result

        return wrapper

    return decorator


@log(filename="mylog.txt")  # для вывода в файл mylog.txt
# @log()                                 # для вывода в консоль
def my_function(x: int, y: int) -> int:
    """Функция, складывающая два числа"""
    return x + y


if __name__ == "__main__":
    print(my_function("1", 2))
