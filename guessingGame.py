#Jack Gambello
#2/20


#Rewrite the number guessing game so the player guesses until they are correct or gives up.
# If the player wins, list all the guesses in order from low to high and mark the correct guess. 
#If the player quits, print some message.

import random

guess = raw_input("Guess a number to begin the guessing game. ") #this variable will start/stop loop
if guess == "":
	print("You did not enter a number. Please restart program.")
	exit()
	
secretNumber = random.randint(1,100) #Produces the random int the user must attempt to guess


guesses = [] #creates the list containing the guesses that will be printed at the end

while guess != "quit":
	guess = int(guess)
	if guess > secretNumber: #will tell the user to guess lower because there guess was higher than secretNumber
		guesses.append(guess)
		guess = raw_input("That is incorrect. Guess lower. Enter 'quit' if you give up. If not enter a number. ")
		if guess == "":
			print("You did not enter a number. Please restart program.")
			exit()
		winIndicator = 0
	elif guess < secretNumber:  #will tell the user to guess higher because there guess was lower than secretNumber
		guesses.append(guess)
		guess = raw_input("That is incorrect. Guess higher. Enter 'quit' if you give up. If not enter a number. ")
		if guess == "":
			print("You did not enter a number. Please restart program.")
			exit()
		winIndicator = 0
	elif guess == secretNumber: #will occur if user guesses correct number
		guesses.append(guess)
		output = "That is correct. It took you {} tries. Your guesses were ".format(len(guesses))
		guesses.sort()	
		for guess in guesses:
			if guess == secretNumber: #this if statement marks the correct guess
				guess = ("{}**, ".format(guess))
				output += str(guess)
			elif guess == (guesses[-1]): #gets ride of comma at end of output
				guess = ("{} ".format(guess))
				output += str(guess)
			else:
				guess = ("{}, ".format(guess))
				output += str(guess)
		print(output)
		guess = "quit" #ends loop
		winIndicator = 1

			
if guess == "quit":	
		if winIndicator == 1:
			print("Excellent Work.")
		elif winIndicator == 0:
			print("You couldn't guess the right number. It was {}. Try again soon! Good bye.".format(secretNumber))
