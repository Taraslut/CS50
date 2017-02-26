while True:
    print(u'Введіть 16 цифр кредитної картки >', end="")
    x = input()
    if len(x) != 13 | len(x) != 15 | len(x) != 16:
        print(u'Повинно буть 13, 15 або 16 цифр.\n')
        continue
    if x.isalpha():
        print(u'Букв не повинно бути у введеному числі.')
        continue
    break

suma = 0
for figure in x[1::2]:
    print("{}*2+ ".format(figure), end="")
    suma += int(figure) * 2

for figure in x[0::2]:
    print("{}+ ".format(figure), end="")
    suma += int(figure)

print("={}".format(suma))
if suma % 10 != 0:
    print('Invalid')
    exit()

first = int(x[0:2])

if first == 34 | first == 37:
    print('American Express')
    exit()

if first > 50 & first < 56:
    print('MasterCard')
    exit()

first = int(x[0:1])
if first == 4:
    print("Visa")
    exit()
