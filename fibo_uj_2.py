hanyadik = int(input("Fibonacci sorozat hanyadik értékét írjuk ki?  "))

f1, f2 = 1, 1
if hanyadik == 1 or hanyadik == 2:
    print(f"A fibonacci sorozat {hanyadik}. eleme az: 1")
else:
    for i in range(3, hanyadik+1):
        F = f1 + f2

        f1 = f2
        f2 = F
    print(f"A fibonacci sorozat {hanyadik}. eleme a(z): {F}")
