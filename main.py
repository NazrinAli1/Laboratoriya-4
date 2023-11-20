from random import randint

n = 24
a = [0] * n

for i in range(n):
    a[i] = randint(-12, 24)

with open("output.txt", "w") as o:
    o.write('\n'.join(map(str, a[:-1])) + '\n')

p = next((i for i, x in enumerate(a) if x > 0), -1)

if p != -1:
    r = 1
    for i in range(p):
        r *= a[i]

    with open("output.txt", "a") as o:
        o.write(str(r) + '\n')
