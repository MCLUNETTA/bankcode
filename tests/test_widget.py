import pytest
from src.widget import get_date, mask_account_card


@pytest.mark.parametrize(
    "user_input, expected",
    [
        ("Visa Platinum 7000792289606361", "Visa Platinum 7000 79** **** 6361"),
        ("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
        ("Счет 73654108430135874305", "Счет **4305"),
        ("Visa Classic 6831982476737658", "Visa Classic 6831 98** **** 7658"),
        ("Счет 12345678901234567890", "Счет **7890"),
        ("Visa Gold 5999415631248532", "Visa Gold 5999 41** **** 8532"),
    ],
)
def test_mask_account_card(user_input, expected):
    assert mask_account_card(user_input) == expected


@pytest.mark.parametrize(
    "date_str, expected",
    [
        ("2024-03-11T02:26:18.671407", "11.03.2024"),
        ("2018-06-30T02:08:58.425572", "30.06.2018"),
        ("2023-12-31T23:59:59.999999", "31.12.2023"),
        ("2021-01-01T00:00:00.000000", "01.01.2021"),
    ],
)
def test_get_date_valid(date_str, expected):
    assert get_date(date_str) == expected
