import os
import sys
import sqlite3
import argparse
from functools import reduce
from pathlib import Path

if __name__ == "__main__":

  # parser = argparse.ArgumentParser()
  # parser.add_argument("file_path", type=Path)
  # p = parser.parse_args()
  # print(p.file_path, type(p.file_path), p.file_path.exists())

  mydirpath = sys.argv[1]
  files = os.listdir(mydirpath)

  table_files = "files"
  mydb = sqlite3.connect(':memory:')
  cursor = mydb.cursor()
  cursor.execute('''CREATE TABLE {}
                  (name text, modification_date real, size integer)
                '''.format(table_files))
  list_file_sizes = []
  for file_name in files:
    absolpath = os.path.join(mydirpath, file_name)
    filemoddate = os.path.getctime(absolpath)
    filesize = os.path.getsize(absolpath)
    list_file_sizes.append(filesize)
    cursor.execute("""INSERT INTO {} VALUES
                  ("{}", {}, {})
                  """.format(table_files, file_name, filemoddate , filesize))

  sqlite_select_query = """SELECT * from {}""".format(table_files)
  cursor.execute(sqlite_select_query)
  records = cursor.fetchall()
  #print (records)

  midsize = reduce(lambda x,y:(x + y)/2, list_file_sizes)

  print(midsize)

  for file_name in files:
    absolpath = os.path.join(mydirpath, file_name)
    filesize = os.path.getsize(absolpath)
    if filesize > midsize:
      print (file_name, filesize)



