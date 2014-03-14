__author__ = 'Eladio'

import csv, pyodbc

# set up some constants
MDB = 'C:\Users\Eladio\Desktop\Grupo Inco\Datasur\Cr201301e.mdb'; DRV = '{Microsoft Access Driver (*.mdb)}'; PWD = 'pw'

# connect to db
con = pyodbc.connect('DRIVER={};DBQ={};PWD={}'.format(DRV,MDB,PWD))
cur = con.cursor()
tables = []
for row in cur.tables():
    if not "MSys" in row.table_name:
        tables.append(row.table_name)
# run a query and get the results
for table in tables:
    SQL = 'SELECT * FROM ' + table +';' # your query goes here
    rows = cur.execute(SQL).fetchall()
    cur.close()
    con.close()

    # you could change the mode from 'w' to 'a' (append) for any subsequent queries
    with open(table + '.csv', 'wb') as fou:
        csv_writer = csv.writer(fou) # default field-delimiter is ","
        csv_writer.writerows(rows)
