# Finde alle Primzahlen bis 2000, die 2 auseinanderliegen

allPrimes = [2,3]
twins = []

for num in range(2000):
	teilbar = False
	for i in range(2,num,1):
		if num % i == 0:
			teilbar = True
			break
	if teilbar == False:
		allPrimes.append(num)
		if allPrimes[-1] - allPrimes[-2] == 2:
			twins.append((allPrimes[-2],allPrimes[-1]))

for t in twins:
	print(t)



####################################################

import numpy as np

Anzahl 		= 10
Prim 			= Anzahl
Summe 		= 2
Fortschritt	= 0
Intervall 	= 200

for i in range(Anzahl,1,-1):
	for j in range(2,i,1):
		if(i%j)==0:
			if Prim%Intervall == 0:
				print("Es gibt maximal", Prim, "Primzahlen zwischen 2 und", Anzahl, "// Summe kumulativ:", Summe, "// Fortschritt:", np.round(Fortschritt,3), "Prozent")
				Fortschritt+=100*Intervall/Anzahl
			Prim-=1
			break
		if j==2:
			Summe+=i

print("Es gibt genau", Prim-1, "Primzahlen zwischen 2 und", Anzahl, "// Summe kumulativ:", Summe)

# Lösung aus Internet
import math

def isPrime(n):
   if n == 1:
      return False
   if n == 2:
      return True
   if n > 2 and n % 2 == 0:
      return False

   max_divisor = math.floor(math.sqrt(n))
   for d in range(3, 1 + max_divisor,2):
     if n % d == 0:
        return False
   return True

primes = [x for x in range(1,10) if isPrime(x) ==True]
print(sum(primes))
