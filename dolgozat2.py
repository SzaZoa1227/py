#a csoport
n = 5
matrix = []
szamlalo = 0
matrixSor = []
for i in range(25):
    matrixSor.append(i+1)
    if len(matrixSor) == n:
        matrix.append(matrixSor)
        matrixSor = []
print(matrix)
osszeg = 0
for i in range(len(matrix)):
    osszeg += matrix[i][3]
print(f"Az utolsó előtti oszlop összege: {osszeg}")