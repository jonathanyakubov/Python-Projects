def main():
	print("This program reads in financial information from a")
	print("file and prints it neatly to the user's screen.\n")
	file_to_open=input("Please enter the filename of the finance data: ")
	data=open(file_to_open, 'r')
	x=data.read()
	data_split=x.split()
	years=int(data_split[1])
	principal=float(data_split[3])
	interest=float(data_split[5])
	
	values=list(data_split[6:7+years])
	for i in range(0,years+1):
		values[i]=float(values[i])
	
		
	print("\nThe initial principal is: ${0:.2f} ".format(principal))
	print("Annual percentage rate is: {0:.1f}% ".format(interest*100))
	print("Length of the term (years): {0:0} ".format(years))
	
	
	print("\nYear\tValue\n-------------------------")
	for i in range(0,years+1):
		print("{0:0}\t${1:7.2f}".format(i,values[i]))
		
	data.close()
	
main()
	