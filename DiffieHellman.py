import random
from sympy import *

def baza():
    g = random.randrange(0,2**4096) # p = 4094-bit
    return g

def generirajProste():
    prostiBrojevi = [i for i in range(1,2**16,2) if isprime(i)] # g = 1024-bit, stavljeno 16 radi testiranja
    return prostiBrojevi

def prost(prostiBrojevi):
    p = random.choice(prostiBrojevi)
    return p

print("Generiram bazni broj...")
g = baza()
print("Generiram listu prostih brojeva...")
prostiBrojevi = generirajProste()
print("Generiram prosti broj...")
p = prost(prostiBrojevi)
print(p, " ", g)

kljucA = 16 # ovo očigledno zamjeniti varijablama
kljucB = 25 # ovo očigledno zamjeniti varijablama

A = (g**kljucA) % p
B = (g**kljucB) % p

print(A, " ", B)

rjesenjeA = (B**kljucA) % p
rjesenjeB = (A**kljucB) % p

print(rjesenjeA, " ", rjesenjeB)
