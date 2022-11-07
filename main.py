#!/usr/bin/env python3.0

# This program will generate category description from the models given in ~/models.csv
# In ~/models.csv the column top_kw is used as page title and meta description (Do a KW research)
# The description are made from template given in ~/db/csv/country/type (If you do any changes to these files, remember that the database also needs to be updated)
# Which template is used is decided from the type column in ~/models.csv, in order for this to work, these columns has to have the same name as the ones in ~/csv/country/type

from db.Database import Database
from lib.WorkWithCsv import WorkWithCsv
from lib.Make import Make

def main():	
	# User Message
	country = input("Write country abbreviation (eg. dk, se, no, en, etc.): ").lower()
	# country = 'no'
	# Creates Database
	getDatabase(country = country)
	# Opens CSV
	models = getCsv(country = country)
	# Make Description
	models = make(models = models, country = country)
	# # Save the csv file
	saveCsv(country = country, models = models)
	# # # # Close Connection to Database
	closeDatabaseConnection()
	# Final user message
	print('\x1b[0;30;42m' + 'Descriptions Created' + '\x1b[0m')
	# userMessage(path)

def getDatabase(country:str) -> None:
	# Each time the program runs it makes a new database. The values is the files in ~/db/csv/country/. 	
	database = Database(country)
	database.insertText()
	database.insertSynonym()

def getCsv(country:str) -> dict:
	csv = WorkWithCsv(country)
	openCsv = csv.openCsv()
	return openCsv

def make(models:dict, country:str) -> dict:		
	make = Make(country)
	models = make.assignDescriptions(models = models)
	models = make.replaceDescVariables(models = models)
	models = make.giveDescRandomSynonym(models = models)
	models = make.dictToList(models = models)
	return models

def saveCsv(country:str, models:dict) -> str:
	csv = WorkWithCsv(country = country)
	path = csv.saveCsv(models = models)
	return path

def closeDatabaseConnection():
	database = Database(None)
	database.closeConnection()

def userMessage(path):
	csv = WorkWithCsv(None)
	csv.openFile(path)
	
# Call the main function
if __name__ == '__main__':
	main()