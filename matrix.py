matrix = []
szam = 0
n = 5
for i in range(n):
    m = []
    for j in range(n):
        szam += 1
        m.append(szam)
    matrix.append(m)
print(matrix)
osszeg = 0
for i in range(n):
    osszeg += matrix[i][i]
print(osszeg)
osszeg = 0
for i in range(n):
    osszeg += matrix[-i][-i]
print(osszeg)