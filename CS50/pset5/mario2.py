from idlelib.configDialog import is_int

while True:
    x = input(u'Введіть число > ')
    if not is_int(x):
        print(u'Введене значення повинно бути число.')
        continue
    x = int(x)
    if x <= 1:
        print(u'Число повинно бути більше 0')
        continue
    break

for j in range(x):
    for i in range(x):
        if i+2 > x-j:
            print("#", end="")
        else:
            print(" ", end="")

    print(" ", end="")

    for i in range(x):
        if i > j:
            print(" ", end="")
        else:
            print("#", end="")

    print()
