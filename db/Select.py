# coding=utf-8
#!/usr/bin/python
import sqlite3
import random

class Select:
	def __init__(self):
		global connection
		global c
		connection = sqlite3.connect('category_texts.db')		
		c = connection.cursor()
	
	def deviceTypeRandomTemplate(self, deviceType):
		# Choose Database table from deviceType
		sql = 'SELECT * FROM ' + deviceType + ''
		c.execute(sql)				
		# Getting tables values
		rows = c.fetchall()
		template = {}
		
		if deviceType == 'smartphone' or deviceType == 'tablet':
			for row in rows:						
				template = {'title' : str(rows[random.randint(0, int(len(rows)) - 1)][1]), 'meta_desc' : str(rows[random.randint(0, int(len(rows)) - 1)][2]), 'description' : str(rows[random.randint(0, int(len(rows)) - 1)][3]), 'first_h2' : str(rows[random.randint(0, int(len(rows)) - 1)][4]),	'first_h2_description' : str(rows[random.randint(0, int(len(rows)) - 1)][5]), 'second_h2' : str(rows[random.randint(0, int(len(rows)) - 1)][6]), 'second_h2_description' : str(rows[random.randint(0, int(len(rows)) - 1)][7]), 'third_h2' : str(rows[random.randint(0, int(len(rows)) - 1)][8]), 'third_h2_description' : str(rows[random.randint(0, int(len(rows)) - 1)][9]) }
		else:
			for row in rows:		
				template = {'title' : str(rows[random.randint(0, int(len(rows)) - 1)][1]), 'meta_desc' : str(rows[random.randint(0, int(len(rows)) - 1)][2]), 'description' : str(rows[random.randint(0, int(len(rows)) - 1)][3]) }

		# Return results
		return template

	def randomSynonym(self, nounType:str, table:str):
		# Execute query
		cursor = connection.execute('SELECT ' + nounType + ' FROM ' + table + '_synonym')		
		# Makes rows a list
		rows = [item[0] for item in cursor.fetchall()]
		# Pick Random result from rows list				
		randVal = random.choice(rows)
		# randVal = rows[random.randint(0, int(len(rows)) -1)]
		return randVal

	def deviceTypeRandomSynonym(self, nounType:str, table:str):
		# Execute query
		cursor = connection.execute('SELECT ' + nounType + ' FROM ' + table + '_synonym')		
		# Makes rows a list
		rows = [item[0] for item in cursor.fetchall()]
		# Pick Random result from rows list				
		randVal = random.choice(rows)
		# randVal = rows[random.randint(0, int(len(rows)) -1)]
		return randVal
		
	
	