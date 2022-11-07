# coding=utf-8
from db.Select import Select
from lib.Helper import Helper
# import random

class Make:
	def __init__(self, country:str):		
		self.country = country
		self.select = Select()
		self.helper = Helper()

	# Assign a random text from DB, according to the model device type (smartphone, smartwatch, tablet etc.)
	def assignDescriptions(self, models:dict) -> dict:	
		for model in models:
			models[model]['texts'] = self.select.deviceTypeRandomTemplate(models[model]['devicetype'])
		# return
		return models

	def replaceDescVariables(self, models:dict) -> dict:					
		staticVariables = ['DEVICE', 'SCREENSIZE', 'RELEASEYEAR', 'BRAND' ,'MODEL', 'CAMERA']
		# Loop through models
		i = 0
		for model in models:										
			# If models[i]['texts'] has variable ([VARIABLE]), replace it 
			for variable in staticVariables:
				for key, value in models[i]['texts'].items():
					# Convert value to string
					value = str(value)					
					# Other Variables
					if '[COUNTRY]' in value:
						models[i]['texts'].update({ key : value.replace('[COUNTRY]', self.helper.countryNameFromAbbr(self.country) )})

					# if '[DEVICETYPE]' in value:						
					# 	models[i]['texts'].update({ key : value.replace('[DEVICETYPE]', self.select.deviceTypeRandomSynonym(models[i]['devicetype']) )})

					# If template name has variable
					if '[' + variable + ']' in value:
						models[i]['texts'].update({key : value.replace('[' + variable + ']', models[i][variable.lower()])})
						
			# Loop through models['text'] Dictionary			
			# for key, value in models[i]['texts'].items():
					# If there is researched for Top_kw, Use a optimized title for this
					if models[i]['topkw'] and models[i]['devicetype'] == 'smartphone':
						# commonKw = self.select.commonKw(country=self.country, device_type=models[i]['devicetype'])
						models[i]['texts']['title'] = models[i]['topkw']						

						# # # If page isn't long enough, concatenate common kw
						# if len(models[i]['texts']['title']) < 55:							
						# 	# If KW already is in commonKw, delete from common KW, so we wont append duplicates
						# 	splitted = models[i]['texts']['title'].lower().split()							
						# 	for kw in commonKw:
						# 		if kw in splitted:									
						# 			commonKw.remove(kw)
						# 	# Get two random
						# 	twoRand = random.sample(commonKw, 2)
						# 	# Convert to String
						# 	twoRandString = ' & '.join(twoRand).title()
						# 	# New PT												
						# 	models[i]['texts']['title'] = models[i]['texts']['title'] + ', ' + twoRandString

						# # # Give a medal
						# models[i]['texts']['title'] = models[i]['texts']['title'] + ' &#129351; '

			i += 1 # model iteration		
		return models
	
	def giveDescRandomSynonym(self, models:dict) -> dict:
		randomVariables = ['[S_SCREENPROTECTOR]', '[P_SCREENPROTECTOR]', '[DEVICETYPE]']
		#
		i = 0
		for model in models:
			for variable in randomVariables:
				for key, value in models[i]['texts'].items():
					value = str(value)
					# If a variable exists in the text
					if variable in value:						
						# If singular version
						if variable[1:3] == 'S_':
							# Get word without [S_ and remove the closing ]
							table = variable[3:-1].lower()
							singular = self.select.randomSynonym(nounType = 'singular', table = table)
							models[i]['texts'].update({ key : value.replace(variable, singular )})
						
						# If plural version
						if variable[1:3] == 'P_':							
							# Get word without [S_ and remove the closing ]
							table = variable[3:-1].lower()							
							plural = self.select.randomSynonym(nounType = 'plural', table = table)
							models[i]['texts'].update({ key : value.replace(variable, plural )})
						
						# Other
						if variable == '[DEVICETYPE]':
							singular = self.select.deviceTypeRandomSynonym(nounType = 'singular', table = models[i]['devicetype'])
							models[model]['texts'].update({ key : value.replace('[DEVICETYPE]', singular) })					
			i += 1		
		return models

	# # Convert models[i]['texts'] Dict to models[i] List items, so it's writable to WorkWithCsv.savecsv()
	def dictToList(self, models:dict) -> dict:
		# Loop through models
		i = 0
		for model in models:						
			# Convert each item in to key:value in the models dict
			for key, value in models[i]['texts'].items():				
				models[i][key] = value			
			# Remove the text dict
			models[i].pop('texts')
			i += 1 # model iteration	

		# Return models
		return models