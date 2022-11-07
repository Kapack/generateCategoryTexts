import os
import csv

class InsertSynonym:
    def __init__(self, cursor, conn, country):
        # Creates table
        self.createSmartphoneSynonym(cursor)
        # Insert values
        self.insertSmartphoneSynonym(cursor, conn, country)
        #
        self.createScreenProtectorSynonym(cursor)
        self.insertScreenProtectorSynonym(cursor, conn, country)

    def createSmartphoneSynonym(self, cursor):
        sql = 'CREATE TABLE if not exists smartphone_synonym (id integer primary key not null, word text, singular text, plural text)'
        cursor.execute(sql)

    def insertSmartphoneSynonym(self, cursor, conn, country):
        with open(os.getcwd() + '/db/csv/'+ country +'/synonym/smartphone_synonym.csv', 'r') as file:
            reader = csv.DictReader(file, delimiter=';')
            i = 1
            for row in reader:
                cursor.execute('INSERT INTO smartphone_synonym VALUES (?,?,?,?)', (i, row['word'], row['singular'], row['plural']))
                i += 1
            conn.commit()

    def createScreenProtectorSynonym(self, cursor):
        sql = 'CREATE TABLE if not exists screenprotector_synonym (id integer primary key not null, word text, singular text, plural text)'
        cursor.execute(sql)

    def insertScreenProtectorSynonym(self, cursor, conn, country):
        with open(os.getcwd() + '/db/csv/'+ country +'/synonym/screenprotector_synonym.csv', 'r') as file:
            reader = csv.DictReader(file, delimiter=';')
            i = 1
            for row in reader:
                cursor.execute('INSERT INTO screenprotector_synonym VALUES (?,?,?,?)', (i, row['word'], row['singular'], row['plural']))
                i += 1
            conn.commit()