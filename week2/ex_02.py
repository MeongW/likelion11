l = ['A', 'B', 'O', 'AB', 'A', 'B', 'O', 'AB', 'A', 'B', 'O', 'AB', 'A', 'B', 'O', 'AB', 'A', 'B', 'O', 'AB', 'A', 'B', 'O', 'AB', 'A', 'B', 'O', 'AB', 'A', 'B', 'O', 'AB', 'A', 'B', 'O', 'AB', 'A', 'B', 'O', 'AB', 'A', 'B', 'O', 'AB', 'A', 'B', 'O', 'AB', 'A', 'B', 'O', 'AB', 'A', 'B', 'O', 'AB', 'A', 'B', 'O', 'AB', 'A', 'B', 'O', 'AB', 'A', 'B', 'O', 'AB', 'A', 'B', 'O', 'AB', 'A', 'B', 'O', 'AB', 'A', 'B', 'O', 'AB', 'A', 'B', 'O', 'AB', 'A', 'B', 'O', 'AB', 'A', 'B', 'O', 'AB', 'A', 'B', 'O', 'AB', 'A', 'B', 'O', 'AB', 'A', 'B', 'O', 'AB', 'A', 'B', 'O', 'AB', 'A', 'B', 'O', 'AB', 'A', 'B', 'O', 'AB', 'A', 'B', 'O', 'AB', 'A', 'B', 'O', 'AB', 'A', 'B', 'O', 'AB', 'A', 'B', 'O', 'AB', 'A', 'B', 'O', 'AB', 'A', 'B', 'O', 'AB', 'A', 'B', 'O', 'AB', 'A', 'B', 'O', 'AB', 'A', 'B', 'O', 'AB', 'A', 'B', 'O', 'AB', 'A', 'B', 'O', 'AB', 'A', 'B', 'O', 'AB', 'A', 'B', 'O', 'AB', 'A', 'B', 'O', 'AB', 'A', 'B', 'O', 'AB', 'A', 'B', 'O', 'AB', 'A', 'B', 'O', 'AB', 'A', 'B', 'O', 'AB', 'A', 'B', 'O', 'AB', 'A', 'B', 'O', 'AB', 'A', 'B', 'O', 'AB', 'A', 'B', 'O', 'AB', 'A', 'B', 'O', 'AB', 'A', 'B', 'O', 'AB', 'A', 'B', 'O', 'AB', 'A', 'B', 'O', 'AB', 'A', 'B', 'O', 'AB', 'A', 'B', 'O', 'AB', 'A', 'B', 'O', 'AB', 'A', 'B', 'O', 'AB', 'A', 'B', 'O', 'AB', 'A', 'B', 'O', 'AB', 'A', 'B', 'O', 'AB', 'A', 'B', 'O', 'AB', 'A', 'B', 'O', 'AB', 'A', 'B', 'O', 'AB', 'A', 'B', 'O', 'AB', 'A', 'B', 'O', 'AB', 'A', 'B', 'O', 'AB', 'A', 'B', 'O', 'AB', 'A', 'B', 'O', 'AB', 'A', 'B', 'O', 'AB', 'A', 'B', 'O', 'AB', 'A', 'B', 'O', 'AB', 'A', 'B', 'O']
a, o, ab, b = 0, 0, 0, 0

for i in l:
    if i == 'A':
        a += 1
    elif i == 'B':
        b += 1
    elif i == 'O':
        o += 1
    elif i == 'AB':
        ab += 1
print(a, o, ab, b)

l.append('B')
b += 1

d = { 'AB':ab, 'B':b, 'A':a, 'O':o}

print(d['A'])
print(d['O'])
print(d['AB'])
print(d['B'])