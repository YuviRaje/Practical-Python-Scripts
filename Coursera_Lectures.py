import sqlite3 as lite
import os
import sys
from module1 import download, scrape

# Defining the download action
connector = None

if not(os.path.exists('database.db')):
	connector = lite.connect('database.db')	
	urls = scrape('https://class.coursera.org/compilers-003/lecture')

	with connector:
		cur = connector.cursor()
		cur.execute("CREATE TABLE links(url TEXT)")

		for link in urls:
			cur.execute("INSERT INTO links VALUES(?)", (link,))			

else:
	connector = lite.connect('database.db')

	with connector:
		cur = connector.cursor()
		cur.execute("SELECT * FROM links")

		lines = cur.fetchall()

		for row in lines:
			download(row[0])
			cur.execute("DELETE FROM links WHERE url=?", (row[0],))
			connector.commit()
			print ('Deleted: ', row[0])