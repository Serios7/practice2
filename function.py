# Вариант 5: функция № 5

# 5. Написать функцию avaranger,
# которая принимает 1 аргумент - любое число и возвращается среднее арифметическое значение,
# на основании текущего числа и предыдущих, которые были введены ранее.
stock = []

def Avaranger(num):
    stock.append(num)
    return sum(stock)/len(stock)


while True:
    num = int(input('Введите число: '))
    print(Avaranger(num))