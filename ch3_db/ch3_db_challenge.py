import sqlite3 as lite
import pandas as pd 

con = lite.connect('getting_started.db')

with con:
	cur = con.cursor()
	cur.execute("SELECT name, warm FROM cities INNER JOIN weather ON name = city AND warm='July' ORDER BY warm")
	rows = cur.fetchall()

	cols = [desc[0] for desc in cur.description]

	df = pd.DataFrame(rows, columns=cols)
	for wa in df[cols[0]]:
		print ("The cities that are warmest in July are: %s \n" %wa)