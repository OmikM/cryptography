def ceasar():
  a = input("plain texst: ")
  b = int(input("shift(can by -): "))
  c = ""
  for i in range(len(a)):
    d = ord(a[i])
    if d>=97 and d<=122:
      d+=b
    if d>=122:
      d-=25
    c = c+(chr(d))
  return c
    