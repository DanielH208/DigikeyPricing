
# Python program to read CSV file without header

# Import necessary packages
import csv
###
import sys



    

def pricing (file, quantity):
	# Open file
	with open(file) as file_obj:
	

		
		# Skips the heading
		# Using next() method
		heading = next(file_obj)
	
		# Create reader object by passing the file
		# object to reader method
		reader_obj = csv.reader(file_obj)
	
		specific_columns = []

		# Iterate over each row in the csv file
		# using reader object
		# Append the quantity and stock code value of each row into the specific columns list
		for row in reader_obj:
			specific_columns.append([row[1],row[4]])

		
		
		print(specific_columns)
		print(quantity)

		overall_price = 0
		unmatched_components = []



	



if __name__ == '__main__':
    pricing (*sys.argv[1:])