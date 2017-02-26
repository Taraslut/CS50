import sys

param1 = sys.argv[1]
if len(param1) == 0:
    print(u'You don\'t enter key digit :( ')
param1 = int(param1)
# print(param1)
print(u'Введіть рядок для кодування > ', end="")
x = input()

for letter in x:
    if ord(letter) < ord('Z'):
        print(chr(((ord(letter) + param1 - ord('A')) % 26) + ord('A')), end="")
        continue
    if ord(letter) < ord('z'):
        print(chr(((ord(letter) + param1 - ord('a')) % 26) + ord('a')), end="")
