
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

		
		
		refresh_token = "**PLACEHOLDER**"
		client_id = "**PLACEHOLDER**"

		url = "https://api.digikey.com/v1/oauth2/token"

		post_data = {"client_id":client_id,
					 "client_secret":"**PLACEHOLDER**",
					 "refresh_token":refresh_token,
					 "grant_type":"refresh_token"}

		response = requests.post(url, data=post_data)

		
		
		extract = response.json()
		print(extract)
	

		refresh_token = extract['refresh_token']
		access_token = extract['access_token']
		print("refresh token: " + refresh_token)
		print("access token: " + access_token)

		for item in specific_columns:
			get_headers = {"Authorization":"Bearer "+access_token,
						   "X-DIGIKEY-Client-Id":client_id,
						   "X-DIGIKEY-Locale-Site":"UK",
						   "X-DIGIKEY-Locale-Language":"en",
						   "X-DIGIKEY-Locale-Currency":"GBP",
						   "X-DIGIKEY-Locale-ShipToCountry":"uk",
						   "X-DIGIKEY-Customer-Id":"0"}

			params = {"includes": "DigiKeyPartNumber,StandardPricing"}

			item_url = "https://api.digikey.com/Search/v3/Products/" + item[1]
			get_response = requests.get(item_url, headers=get_headers, params=params)
			get_extract = get_response.json()
			print(get_extract)
			print(item_url)

		
		
	



if __name__ == '__main__':
    pricing (*sys.argv[1:])