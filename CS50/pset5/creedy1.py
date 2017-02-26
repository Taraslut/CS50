from idlelib.configDialog import is_int
from pandas.lib import is_float

while True:
    x = input(u'Введіть суму > ')
    print(x)
    print(type(x))
    if x.isalpha():
        print(u'Введене значення повинно бути число.')
        continue
    if int(float(x)*100) <= 0:
        print(u'Число повинно бути більше 0')
        continue
    break

x = int(float(x) * 100)


print((x // 25) + (x % 25) // 10 + (x % 25 % 10)//5+ (x % 25 % 10 %5))
