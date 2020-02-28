Factions = {
	"Muaat" : {
		"red": 1,
		"yellow" : 5,
		"green" : 16,
		"blue" : 16,
		"purple" : 14,
		"black" : 7,
	},
	"Nekro" : {
		"red": 2,
		"yellow" : 17,
		"green" : 17,
		"blue" : 15,
		"purple" : 13,
		"black" : 3,
	},
	"Sardakk" : {
		"red": 3,
		"yellow" : 14,
		"green" : 12,
		"blue" : 17,
		"purple" : 16,
		"black" : 4,
	},
	"Barony" : {
		"red": 4,
		"yellow" : 11,
		"green" : 10,
		"blue" : 5,
		"purple" : 5,
		"black" : 1,
	},
	"L1Z1X" : {
		"red": 5,
		"yellow" : 13,
		"green" : 13,
		"blue" : 4,
		"purple" : 6,
		"black" : 2,
	},
	"Saar" : {
		"red": 6,
		"yellow" : 3,
		"green" : 6,
		"blue" : 6,
		"purple" : 8,
		"black" : 5,
	},
	"Mentak" : {
		"red": 7,
		"yellow" : 2,
		"green" : 9,
		"blue" : 13,
		"purple" : 12,
		"black" : 6,
	},
	"Hacan" : {
		"red": 8,
		"yellow" : 1,
		"green" : 7,
		"blue" : 12,
		"purple" : 11,
		"black" : 15,
	},
	"Sol" : {
		"red": 9,
		"yellow" : 9,
		"green" : 5,
		"blue" : 2,
		"purple" : 7,
		"black" : 10,
	},
	"Yin" : {
		"red": 10,
		"yellow" : 6,
		"green" : 15,
		"blue" : 11,
		"purple" : 3,
		"black" : 8,
	},
	"Ghosts" : {
		"red": 11,
		"yellow" : 15,
		"green" : 8,
		"blue" : 1,
		"purple" : 4,
		"black" : 9,
	},
	"Naalu" : {
		"red": 12,
		"yellow" : 4,
		"green" : 4,
		"blue" : 10,
		"purple" : 10,
		"black" : 12,
	},
	"Winnu" : {
		"red": 13,
		"yellow" : 8,
		"green" : 14,
		"blue" : 7,
		"purple" : 2,
		"black" : 13,
	},
	"JolNar" : {
		"red": 14,
		"yellow" : 16,
		"green" : 11,
		"blue" : 3,
		"purple" : 1,
		"black" : 14,
	},
	"Arborec" : {
		"red": 15,
		"yellow" : 7,
		"green" : 1,
		"blue" : 9,
		"purple" : 9,
		"black" : 11,
	},
	"Yssaril" : {
		"red": 16,
		"yellow" : 10,
		"green" : 2,
		"blue" : 14,
		"purple" : 17,
		"black" : 16,
	},
	"Xxcha" : {
		"red": 17,
		"yellow" : 12,
		"green" : 3,
		"blue" : 8,
		"purple" : 15,
		"black" : 17,
	}
}
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
	sum = 0
	for i in range(0,len(arangement[0])):
		sum = sum + Factions[arangement[0][i]][arangement[1][i]]
	return sum
factions = []
i = 0
while True:
	print(factions)
	print("Enter name of faction")
	dumb = input("")
	try:
		Factions[dumb]
		factions.append(dumb)
	except KeyError:
		print("Not a valid faction")

	if len(factions) == 6:
		break


colors = []
permute(["red", "yellow", "green", "blue", "purple", "black"], colors)

bestScore = 10000
answer = []
for setup in colors:
	cost = score([factions,setup])
	if cost < bestScore:
		bestScore = cost
		answer = setup


print(factions)
print(answer)
