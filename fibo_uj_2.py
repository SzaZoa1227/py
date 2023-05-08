HANYADIK = int(input("Fibonacci sorozat hanyadik értékét írjuk ki?  "))

f1, f2 = 0, 1
for i in range(2, HANYADIK+1):
    F = None
    F = f1 + f2
    f1 = f2
    f2 = F
print(f"A fibonacci sorozat {HANYADIK}. eleme a(z): {F:,}") 
