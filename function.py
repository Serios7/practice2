# Вариант 5: функция № 5

# 5. Написать функцию avaranger,
# которая принимает 1 аргумент - любое число и возвращается среднее арифметическое значение,
# на основании текущего числа и предыдущих, которые были введены ранее.


def Avaranger():
    stock = []
    def inner_func(num):
        stock.append(num)
        return sum(stock)/len(stock)
    return inner_func

f = Avaranger()
while True:
    num = input('Введите число или N для выхода: ')
    if num == 'N':
        break
    else:
        print(f(int(num)))