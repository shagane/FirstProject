import os
mydirpath = r"d:\Background"
files = os.listdir(mydirpath)

import sqlite3
table_files = "files"
mydb = sqlite3.connect(':memory:')
cursor = mydb.cursor()
cursor.execute('''CREATE TABLE {}
                (name text, modification_date real, size integer)
              '''.format(table_files))

for file_name in files:
  absolpath = os.path.join(mydirpath, file_name)
  filemoddate = os.path.getctime(absolpath)
  filesize = os.path.getsize(absolpath)
  cursor.execute("""INSERT INTO {} VALUES
                ("{}", {}, {})
                """.format(table_files, file_name, filemoddate , filesize))

sqlite_select_query = """SELECT * from {}""".format(table_files)
cursor.execute(sqlite_select_query)
records = cursor.fetchall()
print (records)




#midsize =
#if size > midsize:
#    print (midsize)

