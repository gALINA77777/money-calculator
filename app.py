def add_income(balance, amount):
    """Добавить доход к балансу."""
    if amount <= 0:
        raise ValueError("Сумма дохода должна быть положительной")
    return balance + amount


def add_expense(balance, amount):
    """Вычесть расход из баланса."""
    if amount <= 0:
        raise ValueError("Сумма расхода должна быть положительной")
    return balance - amount


def get_summary(incomes, expenses):
    """Вернуть словарь с итогами."""
    total_income = sum(incomes)
    total_expense = sum(expenses)
    return {
        "income": total_income,
        "expense": total_expense,
        "balance": total_income - total_expense,
    }
