import math

def guess():
	print("This program calculates the square root of a given number use the Newton's Method.")
	integer=eval(input("What is the number for which you want to calculate the square root? "))
	n=eval(input("How many iterations would you like to use? "))
	guess = (integer/2)
	for i in range(0,n):
		guess=((guess + (integer/guess))/2)
		print(guess)
	x=guess 
	print("My guess for the square root of", integer, "is", x)
	diff=x-(math.sqrt(integer))
	print("The difference between my guess and the real result is", diff) 
	
guess()
	




