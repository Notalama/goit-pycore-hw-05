def caching_fibonacci():
    """
    Створює та повертає функцію для обчислення чисел Фібоначчі з кешуванням.
    """

    cache = {}  # Словник для зберігання обчислених значень

    def fibonacci(n):
        """
        Обчислює n-те число Фібоначчі з використанням кешування.
        """

        if n <= 0:
            return 0
        elif n == 1:
            return 1
        elif n in cache:
            return cache[n]  # Повертаємо значення з кешу, якщо воно існує
        else:
            result = fibonacci(n - 1) + fibonacci(n - 2)  # Рекурсивний виклик
            cache[n] = result  # Зберігаємо результат у кеші
            return result

    return fibonacci

# Приклад використання
fib = caching_fibonacci()
print(fib(10))  # Виведе 55
print(fib(5))   # Виведе 5
