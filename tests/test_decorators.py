

import pytest

from src.decorators import log


# Тест 1: Успешное выполнение с выводом в консоль
def test_log_console_success(capsys):
    @log()
    def add(x, y):
        return x + y

    result = add(2, 3)
    assert result == 5
    captured = capsys.readouterr()
    assert "add ok" in captured.out


# Тест 2: Ошибка с выводом в консоль
def test_log_console_error(capsys):
    @log()
    def divide(x, y):
        return x / y

    with pytest.raises(ZeroDivisionError):
        divide(10, 0)

    captured = capsys.readouterr()
    assert "divide error: ZeroDivisionError. Inputs: (10, 0), {}" in captured.out


# Тест 3: Успешное выполнение с записью в файл
def test_log_file_success(tmp_path):
    log_file = tmp_path / "test_log.txt"

    @log(filename=str(log_file))
    def multiply(x, y):
        return x * y

    result = multiply(4, 5)
    assert result == 20
    assert log_file.read_text(encoding="utf-8").strip() == "multiply ok"


# Тест 4: Ошибка с записью в файл
def test_log_file_error(tmp_path):
    log_file = tmp_path / "test_log.txt"

    @log(filename=str(log_file))
    def divide(x, y):
        return x / y

    with pytest.raises(ZeroDivisionError):
        divide(5, 0)

    content = log_file.read_text(encoding="utf-8")
    assert "divide error: ZeroDivisionError. Inputs: (5, 0), {}" in content
