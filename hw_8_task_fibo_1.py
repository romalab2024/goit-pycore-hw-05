def caching_fibonacci():
    # Створюємо словник для зберігання кешу
    cache = {}

    # Внутрішня функція, яка обчислює число Фібоначчі
    def fibonacci(n):
        # Базові випадки
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        # Перевірка, чи є значення у кеші
        if n in cache:
            return cache[n]
        # Рекурсивне обчислення та збереження результату в кеші
        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return cache[n]

    # Повертаємо функцію fibonacci, яка має доступ до кешу
    return fibonacci

# Приклад використання
fib = caching_fibonacci()
print(fib(10))  # Виведе 55
print(fib(15))  # Виведе 610
