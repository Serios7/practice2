# Вариант 5: списки № 3

# 3.Дан список чисел.
# Выведите значение наибольшего элемента в списке,
# а затем индекс этого элемента в списке.
# Если наибольших элементов несколько,
# выведите индекс первого из них.

list = input('Введите список чисел: ').split(',')
num_max = max(list)
print(num_max)
print(list.index(num_max))
