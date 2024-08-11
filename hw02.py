import re
from typing import Callable

def generator_numbers(text: str):
    """
    Генерує дійсні числа з тексту, використовуючи регулярні вирази.
    """
    pattern = r"\b\d+\.\d+\b"  # Шукаємо числа з крапкою, оточені пробілами
    for match in re.findall(pattern, text):
        yield float(match)

def sum_profit(text: str, func: Callable):
    """
    Обчислює загальну суму чисел, отриманих з генератора.
    """
    return sum(func(text))

# Приклад використання
text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")
