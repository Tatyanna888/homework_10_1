from unittest.mock import mock_open, patch

from src.decorators import log, my_function


def test_log():
    @log(filename="mylog.txt")
    def my_function(x, y):
        return x + y

    result = my_function(1, 2)
    assert result == 3


def test_log_success():
    @log(filename="mylog.txt")
    def my_function(x, y):
        return x + y

    with patch("builtins.open", mock_open()) as mocked_file:
        result = my_function(1, 2)
        assert result == 3
        mocked_file().write.assert_called_with("my_function ok\n")


def test_log_result(capsys):

    print(my_function(1, 2))
    captured = capsys.readouterr()
    assert captured.out == "3\n"


def test_log_res(capsys):

    my_function(1, 2, filename="mylog.txt")
    captured = capsys.readouterr()
    assert captured.out == ""


def test_log_error(capsys):

    my_function("1", [2])
    captured = capsys.readouterr()
    assert captured.out == ""
