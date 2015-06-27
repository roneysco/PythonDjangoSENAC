from random import randint
print("Welcome!")


opt = True
while opt == True:
	randNumber = randint(1,100)
	count = 1
	while True:
		typedNumber = int(input("Type a number: "))
		if (typedNumber == randNumber):
			print("WOW! You win with one try!")
			break
		else:
			print("Typed number is greater than drawded number" if typedNumber > randNumber else "Typed number is less than drawded number")
			count += 1

	print("End of Game!")
	print("Drawed Number: "+str(randNumber))
	print("Typed Number: "+str(typedNumber))
	print("How many tries you did: "+str(count))
	opt = int(input("Play again??? YES, type 1; NO, type 0."))

