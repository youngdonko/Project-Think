

import sqlite3 as lite

#con = lite.connect('getting_started.db')


# chapter 1
# with con:
# 	cur = con.cursor()
# 	cur.execute('SELECT SQLITE_VERSION()')
# 	data = cur.fetchone()

# 	print("SQLite version : %s" % data)



# chapter 2
# with con:
# 	cur = con.cursor()
# 	cur.execute("INSERT INTO cities VALUES ('Washington','DC')")
# 	cur.execute("INSERT INTO cities VALUES ('Houston','TX')")
# 	cur.execute("INSERT INTO weather VALUES ('Washington',2013,'July','January',63)")
# 	cur.execute("INSERT INTO weather VALUES ('Houston',2013,'July','January',45)")



# chapter 3
# citiesT = (('Las vegas','NV'), ('Atlanta','GA'))
# weatherT = (('Las vegas',2013,'July','December',33),
# 	('Atlanta',2013,'July','January',22))
# con = lite.connect('getting_started.db')

# with con:
# 	cur = con.cursor()
# 	cur.executemany("INSERT INTO cities VALUES(?,?)", citiesT)
# 	cur.executemany("INSERT INTO weather VALUES(?,?,?,?,?)", weatherT)

# chapter 4
# con = lite.connect('getting_started.db')
# with con:
# 	cur = con.cursor()
# 	cur.execute("SELECT * FROM cities")
# 	rows = cur.fetchall()
# 	for row in rows:
# 		print (row)



# chapter 5
import pandas as pd 

con = lite.connect('getting_started.db')

with con:
	cur = con.cursor()
	cur.execute("SELECT * FROM cities")

	rows = cur.fetchall()
	#df = pd.DataFrame(rows)

	cols = [desc[0] for desc in cur.description]
	df = pd.DataFrame(rows, columns=cols)

	print(df)






