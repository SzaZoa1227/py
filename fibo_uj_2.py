import sys
HANYADIK = int(input("Fibonacci sorozat hanyadik értékét írjuk ki?  "))
def fibo(HANYADIK):
    if HANYADIK == 1:
        return 0
    elif HANYADIK == 2:
        return 1
    else:
        f1, f2 = 0, 1
        for i in range(2, HANYADIK+1):
            F = f1 + f2
            f1 = f2
            f2 = F
            return F
print(f"A fibonacci sorozat {HANYADIK}. eleme a(z): {fibo(HANYADIK):,}")
