from ceasar import *
from gcd import *
from basics import*


def help():
  print("\n"+"ceasar"+"\n"+"gcd = Gratest-Common-devisor"+"\n"+"egcd = exstendent gcd"+"\n"+"mod = modular arithemtic")

print("My code very helpfull for cryto CTF but not secured from dump users")
help()

odp = input("\n"+"home: ")
if odp=="ceasar":
  print(ceasar())
if odp=="gcd":
  print(gcd())
if odp=="egcd":
  print(egcd(input("p: "), input("q: ")))
if odp=="mod":
  print(mod())
if odp=="xor":
  print(xor())