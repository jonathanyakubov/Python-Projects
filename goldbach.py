def get_input():
	
	while True: 
		try:
			print("This program tests the Goldbach's conjecture.")
			integer=int(input("Please enter an even integer larger than 2: "))
			if integer < 2:
				print("Your value is less than 2, please try again.")
			elif integer % 2!= 0:
				print("Wrong input")
			else:
				return integer
		except ValueError:
			print("Bad input, try again!")
		except NameError:
			print("Not correct, try agina!")
	
	
def is_prime(n):
	import math
	if n<2:
		return False
	for i in range(2,int(math.sqrt(n)+1)):
		if n%i==0:
			return False
		
	return True 

def main():
	num=get_input()
	i=1
	j=num-1
	prime_i=is_prime(i)
	prime_j=is_prime(j)
	container=[]
	while i+j!=num or (is_prime(i)!= True) or (is_prime(j)!=True):
		container.append(i)
		container.append(j)
		i+=1
		j-=1
		if len(container)>(2*(num-1)):
			print("Goldbach's Conjecture doesn't hold for",num)
			break
	print(i,j)	
# 	print("The two numbers are", i,j)
	print(i,"+",j,"=",num, sep="")	
main()
		


	
			
			