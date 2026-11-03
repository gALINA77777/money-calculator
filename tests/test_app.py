import pytest
from app import add_income, add_expense, get_summary


def test_add_income_increases_balance():
    assert add_income(100, 50) == 150


def test_add_expense_decreases_balance():
    assert add_expense(100, 30) == 70


def test_add_income_rejects_negative():
    with pytest.raises(ValueError):
        add_income(100, -10)


def test_add_expense_rejects_zero():
    with pytest.raises(ValueError):
        add_expense(100, 0)


def test_get_summary_calculates_correctly():
    result = get_summary([1000, 500], [200, 100])
    assert result["income"] == 1500
    assert result["expense"] == 300
    assert result["balance"] == 1200