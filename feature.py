from connect import Connect
import sqlite3

def add_column(db, title, datatype, table='products'):
  stmt = f'''
  ALTER TABLE {table} ADD COLUMN {title} {datatype}
  '''
  db.c.execute(stmt)
  db.conn.commit()

def column_list(curs):
  curs.execute('PRAGMA TABLE_INFO("products")')
  cols = curs.fetchall()
  names = [elem[1] for elem in cols]
  return names

#def new_table(self, title, **kwargs)
#def copy_data(self, title, *ids)
  