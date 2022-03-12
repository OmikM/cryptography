def gcd():
  p = int(input("a: "))
  q = int(input("b: "))
  while p!=q:
    if p>q:
      p-=q
    else:
      q-=p
  return p

def egcd(p,q):
    if p == 0:
        return (q, 0, 1)
    else:
        (gcd, u, v) = egcd(q % p, p)
        return (gcd, v - (q // p) * u, u)

#p = 26513
#q = 32321