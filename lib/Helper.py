class Helper:
	def countryNameFromAbbr(self, country):
		countries = {'dk' : 'Danmark', 'no' : 'Norge', 'se' : 'Sverige'}
		countryName = countries[country]
		return countryName	
