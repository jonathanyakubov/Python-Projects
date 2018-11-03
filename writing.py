def main():
	print ("This program will ask you to input an arithmetic expression and evaluate it.")
	print ("You can do this 100 times. If you don't want to, hit CTRL-C to exit.")
	for i in range(0,100):
		x=input("Please input an arthmetic expression that I can evaluate:")
		print("The evaluation of",x, "=", eval(x))
		
main()

