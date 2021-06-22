duration = int(input("Введите промежуток времени: "))
MINUTE = 60
HOUR = 3600
DAY = 86400
if duration < MINUTE:
     print(f'{duration} ' 'сек')
elif duration < HOUR:
     print(f'{duration // MINUTE} мин'f' {duration % MINUTE} сек')
elif duration < DAY:
     print(f'{duration // HOUR} час'f' {duration % HOUR // MINUTE} мин'f' {duration % MINUTE} сек')
elif duration > DAY:
     print(f'{duration // DAY} дн'f' {duration % DAY // HOUR} час'f' {duration % HOUR // MINUTE} мин'f' {duration % MINUTE} сек')