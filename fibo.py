def fibonacciSorozat(szam):
    if(szam == 0):
        return 0
    elif(szam == 1):
        return 1
    else:
        return (fibonacciSorozat(szam - 1) + fibonacciSorozat(szam - 2))

i = int(input("Mennyi értéket írjunk ki?"))
print("Fibonacci sorozat:")
for i in range(0, i):  
   print(fibonacciSorozat(i))