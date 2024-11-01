import re
from typing import Callable, Generator

# Функція, яка ідентифікує всі дійсні числа у тексті та повертає генератор
def generator_numbers(text: str) -> Generator[float, None, None]:
    # Використовуємо регулярний вираз для знаходження чисел, відокремлених пробілами
    numbers = re.findall(r'(?<=\s)(-?\d+(\.\d+)?)(?=\s)', text)
    # Повертаємо числа як генератор
    for num in numbers:
        yield float(num[0])

# Функція, яка підсумовує всі числа, знайдені генератором
def sum_profit(text: str, func: Callable[[str], Generator[float, None, None]]) -> float:
    return sum(func(text))

# Приклад використання
text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")
