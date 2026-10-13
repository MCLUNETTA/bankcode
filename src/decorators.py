from functools import wraps
from typing import Any, Callable, Optional


def log(filename: Optional[str] = None) -> Callable:
    """Декоратор для логирования результатов работы функции в файл или консоль."""

    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            try:
                result = func(*args, **kwargs)
                log_message = f"{func.__name__} ok\n"
                _write_log(log_message, filename)
                return result
            except Exception as e:
                log_message = f"{func.__name__} error: {type(e).__name__}. Inputs: {args}, {kwargs}\n"
                _write_log(log_message, filename)
                raise e

        return wrapper

    return decorator


def _write_log(message: str, filename: Optional[str] = None) -> None:
    """Записывает сообщение лога в файл или выводит в консоль."""
    if filename:
        with open(filename, "a", encoding="utf-8") as f:
            f.write(message)
    else:
        print(message, end="")
