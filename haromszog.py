import math
a = int(input("Első szakasz hossza  "))
b = int(input("Második szakasz hossza   "))
c = int(input("Harmadik szakasz hossza  "))
K = a+b+c
S = K/2
T = round(math.sqrt(S*(S-a)*(S-b)*(S-c)),2)
while a <=0:
    print("A szakaszok nem lehetnek 0val egyenlőek vagy annál kissebbek")
    a = int(input("Első szakasz hossza  "))
while b <=0:
    print("A szakaszok nem lehetnek 0val egyenlőek vagy annál kissebbek")
    b = int(input("Második szakasz hossza   "))
while c <= 0:
    print("A szakaszok nem lehetnek 0val egyenlőek vagy annál annál kissebbek")
    c = int(input("Harmadik szakasz hossza  "))

if a > b+c or b>a+c or c>a+b:
    print("A három szakasz nem alkothat háromszögegt")
else:
    print("A három szakasz alkothat háromszöget")
    print(f"A háromszög kerülete: {K}")
    print(f"A háromszög területe: {T}")
