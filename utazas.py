ut = float(input("Megtett út hossza kmben(. legyen a tizedesjegyek között)  "))
fogyasztas = float(input("Az autó fogyasztása 100kmenként: "))
benzinAr = 556
penz = round(ut*(fogyasztas/100)*556)
print(f"Az út {penz:,} forintba került.")
