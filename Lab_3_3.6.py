import sys

# Считываем массив чисел
arr = list(map(int, sys.argv[1:]))

# Находим максимальный элемент
max_element = max(arr)

# Выводим количество элементов меньших максимального
print(f'Количество элементов меньших максимального: {len([el for el in arr if el < max_element])}')

# Выводим сумму элементов больших 5
print(f'Сумма элементов больших 5: {sum([el for el in arr if el > 5])}')
