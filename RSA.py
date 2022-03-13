import math
def enrsa(message, e, n):
  c = math.pow(message,e)%n
  return c
def dersa(c, d, n):
  c = math.pow(c,d)%n
  return c