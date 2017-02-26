import crypt
#crypt.crypt(word, salt

while True:
    x = input(u'Введіть hash для розколування > ')
    if not len(x):
        print(u'Введений порожній рядок.')
        continue
    break

salt = x[0:2]
word = x[3:]

for i1 in range(256**4):
    secretPhase = crypt.crypt(word, salt)