import sys

if len(sys.argv)>1 :
    param1 = sys.argv[1]
else:
    print(u'You don\'t enter key phrase :( ')
    print('Usage is:  python.exe vigenere.py  Secret phrase. ')
    exit()

secretKeys = []
secretLenth = 0
for letter in param1:
    if letter != ' ':
        secretKeys.append(ord(letter)-ord('a'))
        secretLenth += 1

while True:
    x = input(u'Введіть фразу для кодування > ')
    if not len(x):
        print(u'Фраза порожня.')
        continue
    break

i = 0
for letter in x:
    i %= secretLenth
    if letter == ' ':
        print(" ",end="")
        continue
    if ord(letter) < ord('Z'):
        print(chr(((ord(letter) + secretKeys[i] - ord('A')) % 26) + ord('A')), end="")
        i += 1
        continue
    if ord(letter) < ord('z'):
        print(chr(((ord(letter) + secretKeys[i] - ord('a')) % 26) + ord('a')), end="")
        i += 1
