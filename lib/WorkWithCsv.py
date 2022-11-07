# coding=utf-8

import csv
import os
import subprocess

class WorkWithCsv:
	def __init__(self, country):
		self.country = country

	def openCsv(self) -> dict:			
		# Open csv file
		with open(os.getcwd() + '/models.csv', 'r') as file:
			reader = csv.DictReader(file, delimiter=';')
			# We will append and return to this dict
			models = {}
			# Iterate through models.csv
			i = 0
			for key in reader:
				models[i] = {'brand' : key['brand'], 'model' : key['model'], 'device' : key['device'], 'topkw' : key['topkw'], 'devicetype': key['devicetype'].lower(), 'screensize' : key['screensize'], 'camera' : key['camera'], 'releaseyear' : key['releaseyear'], 'texts': []}			
				i += 1
			# return
			return models

	def saveCsv(self, models:dict):
		country = self.country
		# Path to save file, and create folder if missing
		path = os.getcwd() + '/import/' + country.upper() + '/'
		if not os.path.exists(path):
			os.makedirs(path)		

		# Create fieldnames / Each key in models dict		
		fieldnames = []
		for model in models:
			for key, value in models[model].items():
				fieldnames.append(key)
				
				if key == 'texts':
					for textKey in models[model][key].keys():
						fieldnames.append(textKey)
			
		# Remove duplicates
		fieldnames = list(dict.fromkeys(fieldnames))				

		# Write CSV
		with open(path + country.upper() + '_category_desc.csv', 'w') as file:
			fieldnames = fieldnames
			writer = csv.DictWriter(file, fieldnames=fieldnames, delimiter=';')
			writer.writeheader()

			# Write rows
			for model in models:
				writer.writerow(models[model])

		# # Return filepath if user opens
		filePath = path + country.upper() + '_category_desc.csv'
		return filePath

	def openFile(self, filePath):
		userOpenFile = input("Do you want open the file? (y/n): ").lower()
		if userOpenFile == 'y':
			subprocess.check_call(['open', filePath])		




