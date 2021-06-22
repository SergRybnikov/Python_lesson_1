num = int(input('Введите число до 20: '))
if num ==1:
    print(num, 'процент')
if (num >= 2) and (num < 5):
    print(num, 'процента')
if (num >= 5) and (num <= 20):
    print(num, 'процентов')
elif num >= 21:
    print('Введено не правильное значение')
