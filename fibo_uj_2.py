import sys
sys.set_int_max_str_digits(99999)
HANYADIK = int(input("Fibonacci sorozat hanyadik értékét írjuk ki?  "))
if HANYADIK == 1:
    print(f"A fibonacci sorozat {HANYADIK}. eleme a 0")
    exit()
elif HANYADIK == 2:
    print(f"A fibonacci sorozat {HANYADIK}. eleme az 1")
    exit()

f1, f2 = 0, 1
for i in range(2, HANYADIK+1):
    F = f1 + f2
    f1 = f2
    f2 = F
print(f"A fibonacci sorozat {HANYADIK}. eleme a(z): {F:,}")
