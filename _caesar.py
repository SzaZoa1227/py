input = str(input("Írj be egy szöveget amit szeretnél titkosítani!  "))
eltolas = 3
input = list(input)
for i in range(0,len(input)):
    print(input[i])
    j = ord(input[i])+eltolas
    j = chr(j)
    input[i] = j
input = ''.join(input)
print(input)
