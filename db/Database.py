#!/usr/bin/python
# -*- coding: utf_8 -*-
import sqlite3
import os
import csv
from db.insert.Synonym import InsertSynonym
from db.insert.Text import InsertText

class Database:
	def __init__(self, country):
		self.country = country
		global conn
		global c
		# Delete Database, so we are fully updated
		os.remove('category_texts.db')
		# Create new Database
		conn = sqlite3.connect('category_texts.db')
		conn.text_factory = str
		c = conn.cursor()

	# Insert Texts
	def insertText(self):
		InsertText(cursor = c, conn = conn, country = self.country)

	# Insert Synonyms 
	def insertSynonym(self):	
		InsertSynonym(cursor = c, conn = conn, country = self.country)		

	def closeConnection(self):
		c.close()
		conn.close()



		
