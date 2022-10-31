import sqlite3

con = sqlite3.connect('searchHistory.db')
cur = con.cursor()

# creating db for weather app
cur.execute(""" CREATE TABLE if NOT EXISTS searchHistory (
   cityName text,
   localTime text
)""")

def showAll():
   con = sqlite3.connect('searchHistory.db')
   cur = con.cursor()

   cur.execute("SELECT rowid,* FROM searchHistory")
   items=cur.fetchall()

   for item in items:
      print(item)
    
   con.commit()
   con.close()

def addOne(city,localTime):
   con = sqlite3.connect('searchHistory.db')
   cur = con.cursor()

   cur.execute("INSERT INTO searchHistory VALUES (?,?)",(city,localTime))

   con.commit()
   con.close()

def deleteOne(rowid):
   con = sqlite3.connect('searchHistory.db')
   cur = con.cursor()

   cur.execute("DELETE FROM searchHistory WHERE rowid = (?)",rowid)

   con.commit()
   con.close()

def deleteAll():
   con = sqlite3.connect('searchHistory.db')
   cur = con.cursor()

   cur.execute("DELETE FROM searchHistory")

   con.commit()
   con.close()

def getUpTo4LastRecords():
   con = sqlite3.connect('searchHistory.db')
   cur = con.cursor()

   cur.execute("SELECT * FROM searchHistory ORDER BY rowid DESC LIMIT 4")
   items = cur.fetchall()

   con.commit()
   con.close()
   return items

def count():
   con = sqlite3.connect('searchHistory.db')
   cur = con.cursor()

   cur.execute("SELECT COUNT(*) FROM searchHistory")
   n = cur.fetchone()

   con.commit()
   con.close()
   return n