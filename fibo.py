def fibonacciSorozat(szam):
    if szam == 0:
        return 0
    if szam == 1:
        return 1
    a = 0
    b = 1
    for _ in range(2, szam + 1):
        c = a + b
        a = b
        b = c
    return b


mennyi = int(input("Mennyi értéket írjunk ki?    "))
print("Fibonacci sorozat:")
for sorszam in range(mennyi):
    print(f"{sorszam+1}. {fibonacciSorozat(sorszam):,}")
