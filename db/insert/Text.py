import os
import csv

class InsertText:
    def __init__(self, cursor, conn, country) -> None:
        self.createSmartphone(cursor)
        self.insertSmartphoneTexts(cursor, conn, country)
        self.createTablet(cursor)
        self.insertTabletTexts(cursor, conn, country)
        self.createSmartwatch(cursor)
        self.insertSmartwatchTexts(cursor, conn, country)

    '''
    Smartphone Texts
    '''
    # Creates Table Texts
    def createSmartphone(self, cursor):
        sql = 'CREATE TABLE if not exists smartphone (id integer primary key not null, title text, meta_desc text, description text, first_h2 text, first_h2_description text, second_h2 text, second_h2_description text, third_h2 text, third_h2_description text)'
        cursor.execute(sql)			        

    # Insert values
    def insertSmartphoneTexts(self, cursor, conn, country):
        with open(os.getcwd() + '/db/csv/'+ country +'/smartphone.csv', 'r') as file:
            reader = csv.DictReader(file, delimiter=';')
            i = 1 # Starting from 1, so we wont get the first row (tile, meta etc.)
            for row in reader:
                cursor.execute('INSERT INTO smartphone VALUES(?,?,?,?,?,?,?,?,?,?)', (i, str(row['title']), str(row['meta_desc']), str(row['description']), str(row['first_h2']), str(row['first_h2_description']), str(row['second_h2']), str(row['second_h2_description']), str(row['third_h2']), str(row['third_h2_description']) ))
                i += 1
            conn.commit()
            
    '''
    Tablet Text
    '''
    # Creates Table Texts
    def createTablet(self, cursor):
        sql = 'CREATE TABLE if not exists tablet (id integer primary key not null, title text, meta_desc text, description text, first_h2 text, first_h2_description text, second_h2 text, second_h2_description text, third_h2 text, third_h2_description text)'
        cursor.execute(sql)			

    # Insert values
    def insertTabletTexts(self, cursor, conn, country):
        with open(os.getcwd() + '/db/csv/'+ country +'/tablet.csv', 'r') as file:
            reader = csv.DictReader(file, delimiter=';')
            i = 1 # Starting from 1, so we wont get the first row (tile, meta etc.)
            for row in reader:
                cursor.execute('INSERT INTO tablet VALUES(?,?,?,?,?,?,?,?,?,?)', (i, str(row['title']), str(row['meta_desc']), str(row['description']), str(row['first_h2']), str(row['first_h2_description']), str(row['second_h2']), str(row['second_h2_description']), str(row['third_h2']), str(row['third_h2_description']) ))
                i += 1
            conn.commit()

    '''
    Smartwatch Texts
    '''
	# Creates Table Texts
    def createSmartwatch(self, cursor):		
        sql = 'CREATE TABLE if not exists smartwatch (id integer primary key not null, title text, meta_desc text, description text)'
        cursor.execute(sql)

    def insertSmartwatchTexts(self, cursor, conn, country):
        with open(os.getcwd() + '/db/csv/'+ country +'/smartwatch.csv', 'r') as file:
            reader = csv.DictReader(file, delimiter=';')			
            i = 1 # Starting from 1, so we wont get the first row (tile, meta etc.)
            for row in reader:
                cursor.execute('INSERT INTO smartwatch VALUES(?,?,?,?)', (i, str(row['title']), str(row['meta_desc']), str(row['description']) ))
                i += 1
            conn.commit()