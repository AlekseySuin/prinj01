def calculate_average(numbers):
 """Функция вычисляет среднее арифметическое списка чисел."""
 if len(numbers) == 0:
  total = sum(numbers)
  average = total / len(numbers)
 # Ошибка: функция должна возвращать значение
  return average
