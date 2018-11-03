"""This script accepts a date in the form month/date/year 
and prints whether or not the date is valid"""

def main(): 
	print("This program accepts a date",
		  "in the form month/day/year and outputs whether or not the date is valid.")	
	
	while True:
		try:
			date=input("Please enter a date (mm/dd/yyyy): ")
			month=int(date[0:2])    #convert the strings into integers below 
			day=int(date[3:5])
			year=int(date[6:10])
			break
		except ValueError:
			print("Please make sure the date is in the form (mm/dd/yyyy).") 
		
	
	if date_check(month,day,year) == True:
		print(month,"/",day,"/",year,sep= "",end="")
		print(" is valid.") 
	else:
		print(month,"/",day,"/",year, sep="", end="")
		print(" is not valid.")
	
	
	
def date_check(month,day,year):
	
	if month == 0:
		return False
	elif month in [1,3,5,7,8,10,12]: 
		if day <=31 and day>0 and year>0:
			return True
	elif month in [4,6,9,12]:
		if day <=30 and day>0 and year>0:
			return True
	elif month == 2:
		if leap_year(year)==True and day == 29:
			return True 
		elif day <=28 and day>0:
			return True
		elif day==29 and leap_year(year)==False:
			return False	
		else:
			return False
	else:
		return False
	
	
def leap_year(year):
	if year % 4 == 0 or (year % 100 == 0 and year % 400 == 0):
		return True 
	else:
		return False
		
main()



