def square_each(numbers): # takes in a list of numbers and returns its square
	for i in range(len(numbers)):
		numbers[i]=numbers[i]*numbers[i]
	

def to_numbers(str_list):
	numbers=str_list.split()
	for i in range(len(numbers)):
		numbers[i]=int(numbers[i])
	return numbers


def sum(numbers):
	sum=0
	for i in range(len(numbers)):
		sum+=numbers[i]	
	return sum
	
	
def main():
	print("This program computes the sum of the squares of numbers read from a file.")
	file=input("Please enter the file name: ")
	in_file=open(file, 'r') 
	in_read=in_file.read()
	integers=to_numbers(in_read)
	square_each(integers)
	summation=sum(integers)
	print("The sum of the squares of the numbers in the file is", summation)
	in_file.close()

main()

