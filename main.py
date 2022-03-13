
from gcd import *
from basics import*
from RSA import *


def help():
  print("\n"+" BASIC:"+"\n"+"mod = modular arithemtic"+"\n"+"ceasar"+"\n"+" GCD:"+"\n"+"gcd = Gratest-Common-devisor"+"\n"+"egcd = exstendent gcd"+"\n"+" RSA"+"\n"+"enrsa = encrypt rsa with n, e, message"+"\n"+"dersa = decrypt rsa with c,d,n"+"\n"+"rsa d = get d with")

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
if odp=="enrsa":
  print(enrsa(int(input("message(int): ")), int(input("e: ")), int(input("N: "))))
if odp=="dersa":
  print(enrsa(int(input("encryptet message: ")), int(input("d: ")), int(input("N: "))))
if odp=="rsa d":
  print(rsaD(int(input("e: ")), int(input("p")), int(input("q"))))