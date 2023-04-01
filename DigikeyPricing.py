
# Python program to read CSV file without header

# Import necessary packages
import csv
###
import sys
import requests
import urllib.request 
import urllib.error 
import http.client
import json

    

def pricing (file, quantity):
	# Open file
	with open(file) as file_obj:
	

		quantity = int(quantity)

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

		
		

		cumulative_price = 0
		unmatched_components = []

		
		
		refresh_token = "**PLACEHOLDER**"
		client_id = "**PLACEHOLDER**"

		url = "https://api.digikey.com/v1/oauth2/token"

		# Data sent to digikey api to receieve new access and refresh tokens
		post_data = {"client_id":client_id,
					 "client_secret":"**PLACEHOLDER**",
					 "refresh_token":refresh_token,
					 "grant_type":"refresh_token"}

		response = requests.post(url, data=post_data)

		
		
		extract = response.json()
	

		refresh_token = extract['refresh_token']
		access_token = extract['access_token']


		
		for item in specific_columns:
			# Set headers so the Digikey API returns the UK prices 
			get_headers = {"Authorization":"Bearer "+access_token,
							"X-DIGIKEY-Client-Id":client_id,
							"X-DIGIKEY-Locale-Site":"UK",
							"X-DIGIKEY-Locale-Language":"en",
							"X-DIGIKEY-Locale-Currency":"GBP",
							"X-DIGIKEY-Locale-ShipToCountry":"uk",
							"X-DIGIKEY-Customer-Id":"0"}

			# Query to only include the standar pricing values in the returned data
			params = {"includes": "DigiKeyPartNumber,StandardPricing"}

			try:
				# Setting the URL path to change for each seperate item/product
				item_url = "https://api.digikey.com/Search/v3/Products/" + item[1]
				# Assemble the custom URL 
				get_response = requests.get(item_url, headers=get_headers, params=params)
				# Return a Json object of the result of get_response
				get_extract = get_response.json()

				# Raise the error so i can handle it below in the except block
				get_response.raise_for_status()
				prices = get_extract["StandardPricing"]


				a_key = "BreakQuantity"
				b_key = "UnitPrice"

				# Extract the break quantity out of prices and add to list_of_break_quantity
				list_of_break_quantity = [a_dict[a_key] for a_dict in prices]

				# Extract the unit price out of prices and add to list_of_unit_price
				list_of_unit_price = [b_dict[b_key] for b_dict in prices]


				overall_price = 0

				# Check if product doesnt have any break quantities
				if len(list_of_break_quantity) == 0:
					print(item[1] + "  does not have a break quantity")
					unmatched_components.append(item)
				# Check if the lowest break quantity of product is higher than item quantity we want
				elif  list_of_break_quantity[0] > int(item[0])*int(quantity):
					print(item[1] + " lowest break quantity higher than item quantity")
					unmatched_components.append(item)
				else:
					# Iterate through indexes of list_of_break_quantity checking if item quantity is greater than or equal to current index break quantity
					for i in range (0, len(list_of_break_quantity)):
						if list_of_break_quantity[i] <= int(item[0])*int(quantity):
							overall_price = (int(item[0])*int(quantity))*list_of_unit_price[i]

						

				
				cumulative_price = cumulative_price + overall_price
				

			
			# Handle HTTPError thrown from item stock code not corresponding with any item stock codes on Digikey API side
			except requests.exceptions.HTTPError as err:
				print("HTTP error: " + item[1] + " data does not match")
				# Add the unmatched item to the unmatched componets list to be returned at the end of the program
				unmatched_components.append(item)
				
	
	print("Overall price for buying " + str(quantity) + " sets of parts: £" + str(round(cumulative_price, 2)))
	print("List of componets where the data doesn't match: " + str(unmatched_components))
	
	
		
		
	



if __name__ == '__main__':
    pricing (*sys.argv[1:])