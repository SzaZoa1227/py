"""hisztizik a vscodeee"""
import random
import time
import os
lehetosegek = ["fej", "írás"]
while True:
    os.system("cls")
    valasztas = random.choice(lehetosegek)
    print("A választás:", valasztas)
    time.sleep(2)
    ujjatek = input("Új játék? (I/N) ").lower()
    if ujjatek != "i":
        print("Viszlát")
        break
