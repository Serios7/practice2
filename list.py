# Вариант 5: списки № 3

# 3.Дан список чисел.
# Выведите значение наибольшего элемента в списке,
# а затем индекс этого элемента в списке.
# Если наибольших элементов несколько,
# выведите индекс первого из них.

lst = input('Введите список чисел: ').split(',')
lst = list(map(int, lst))
num_max = max(lst)
print(num_max)
print(lst.index(num_max))
