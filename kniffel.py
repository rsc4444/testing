# from statistics import mode, mode
import random
import collections

zwei = 0
vier = 0

wurf = []

for i in range(5):
	wurf.append(random.randint(1,6))

# wurf.append(1)
# wurf.append(5)
# wurf.append(5)
# wurf.append(5)
# wurf.append(6)

print()
wurf.sort()
print(wurf)
print()

print("Einsen:", collections.Counter(wurf)[1]*1, "Punkte")
print("Zweien:", collections.Counter(wurf)[2]*2, "Punkte")
print("Dreien:", collections.Counter(wurf)[3]*3, "Punkte")
print("Vieren:", collections.Counter(wurf)[4]*4, "Punkte")
print("Fünfen:", collections.Counter(wurf)[5]*5, "Punkte")
print("Sechsen:", collections.Counter(wurf)[6]*6, "Punkte")
print()

Fullhouse = "maybe"
Pasch = "maybe"

for i in range(1,7):
	if collections.Counter(wurf)[i] == 3:
		print("Dreierpasch:", sum(wurf),"Punkte")
		print("Viererpasch: -")
		Pasch = True
	if collections.Counter(wurf)[i] == 4:
		print("Dreierpasch:", sum(wurf),"Punkte")
		print("Viererpasch:", sum(wurf),"Punkte")
		Fullhouse = False
		Pasch = True
	if collections.Counter(wurf)[i] == 5:
		print("Dreierpasch:", sum(wurf),"Punkte")
		print("Viererpasch:", sum(wurf),"Punkte")
		Pasch = True

if Pasch != True:
	print("Dreierpasch: -")
	print("Viererpasch: -")

if len(set(wurf)) <= 2 and Fullhouse != False:
	print("Fullhouse, 25 Punkte")
else:
	print("Fullhouse: -")

if (3 in wurf and 4 in wurf) and ((1 in wurf and 2 in wurf) or (2 in wurf and 5 in wurf) or (5 in wurf and 6 in wurf)):
	print("Kleine Straße: 30 Punkte")
else:
	print("Kleine Straße: -")

if len(set(wurf)) == 5 and not (1 in wurf and 6 in wurf):
	print("Große Straße: 40 Punkte")
else:
	print("Große Straße: -")

if len(set(wurf)) == 1:
	print("Kniffel, 50 Punkte")
else:
	print("Kniffel: -")

print("Chance:",sum(wurf), "Punkte")

print()