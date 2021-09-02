import random

#generate a random number between 1 and 100 
randnum = random.randint(1,101)
print(randnum)

count=0
guess=-99

while(guess != randnum):
	#Get the user's guess number 
	guess =(int) (input("enter your guess number between 1 to 100:"))

	if guess < randnum:
		print("Higher")
	elif guess > randnum:
		print("Lower")
	else:
		print("you guessed it")
	count=count+1
#end of the loop 
print("you took "+ str(count) + " steps to guess the number")
		
