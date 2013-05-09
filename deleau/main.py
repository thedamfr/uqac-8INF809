import random


SIZE = 5
tableau = []
for i in range(0,SIZE):
	tableau.append(random.randint(0,5))

print(tableau)	


def makeVolume(tableau):
	dicoMax = {}
	volume = 0
	valMax = 0
	for i in range(0,len(tableau)):
		
			j = i - 1
			while j > 0 and tableau[i] > dicoMax[j]:
				volume += min(tableau[i],valMax) - dicoMax[j]
				dicoMax[j] = tableau[i]
				j -= 1
		
		if valMax < tableau[i]
			valMax = tableau[i]
		dicoMax[i] = tableau[i]

	return volume



print(makeVolume(tableau))

		
