n = int(input('number: '))
for _ in range(3):
    for i in range(1, n+1):
        print(" " * (n-i) + "*" * (i * 2 - 1))