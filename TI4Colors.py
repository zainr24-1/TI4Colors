from ColorAssignments import FACTIONS;

####Stolen from the internet
def permute(a, results):
    if len(a) == 1:
        results.insert(len(results), a)
    else:
        for i in range(0, len(a)):
            element = a[i]
            a_copy = [a[j] for j in range(0, len(a)) if j != i]
            subresults = []
            permute(a_copy, subresults)
            for subresult in subresults:
                result = [element] + subresult
                results.insert(len(results), result)
####/stolen

def score(arangement):
		prod = 1
		for i in range(0,len(arangement[0])):
			prod *= 1 + FACTIONS[arangement[0][i]][arangement[1][i]]
		return prod

def bestSetup(factions, setups):
	bestScore = float("-inf")
	colours = []
	for setup in setups:
		cost = score([factions, setup])
		if cost > bestScore:
			bestScore = cost
			colours = setup
	return colours

def getNumFactions():
	numFactions = 0;
	
	while numFactions == 0:
		try:
			num = int(input("How many factions? \n"))
		except ValueError:
			print("Not a valid number")
		if num <= 8:
			numFactions = num
		else:
			print("Not a valid number")
		
		return numFactions

def getFactions(numFactions):	
	factions = []

	while True:
		print(factions)
		print("Enter name of faction")
		name = input("")
		try:
			FACTIONS[name]
			factions.append(name)
		except KeyError:
			print("Not a valid faction")

		if len(factions) >= numFactions:
			break

	return factions

def main():
	n = getNumFactions()
	factions = getFactions(n)

	setups = []
	permute(["red", "yellow", "green", "blue", "purple", "black", "orange", "pink"], setups)

	colours = bestSetup(factions, setups)
	answers = dict(zip(factions, colours))

	print(answers)

if __name__ == "__main__":
	main()