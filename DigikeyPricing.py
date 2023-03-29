# Python program to read CSV file without header

# Import necessary packages
import csv
###
# Open file
with open(r'D:\3adesign\DigikeyPricing\DigikeyPricing\Bill Of Materials PowerPortMax-v5.csv') as file_obj:
	
	# Skips the heading
	# Using next() method
	heading = next(file_obj)
	
	# Create reader object by passing the file
	# object to reader method
	reader_obj = csv.reader(file_obj)
	
	specific_columns = []

	# Iterate over each row in the csv file
	# using reader object
	for row in reader_obj:
		specific_columns.append([row[1],row[4]])
		
	print(specific_columns)



#import pandas as pd
#import numpy as np

#df=pd.read_csv(r'D:\3adesign\DigikeyPricing\DigikeyPricing\Bill Of Materials PowerPortMax-v5.csv')
#print("The dataframe is:")
#print(df)
#specific_columns=df[["Quantity","Stock Code"]]

#print("The column are:")
#print(specific_columns)

#for item in specific_columns:
#	print(item["Quantity"])
#	print(item["Stock Code"])

#while specifc_columns[i] <= specifc_columns.length:
