import sqlite3
from connect import Connect
import feature as ft

class Query():
  def __init__(self):
    self.db = Connect()
  def create_product(self, **kwargs):
    keys = tuple(kwargs.keys())
    vals = tuple(kwargs.values())
    query = f"INSERT INTO products {keys} "
    query += f"VALUES {vals}"
    try:
      self.db.c.execute(query)
      self.db.conn.commit()
    except sqlite3.OperationalError as err:
      print(err)
      print('create_product_alt accepts any columns')
  def create_product_alt(self, **kwargs):
    colset = set(ft.column_list(self.db.c))
    keyset = set(kwargs.keys())
    newset = keyset - (colset & keyset)
    newcols = list(newset)
    newtypes = []
    for elem in newcols:
      val = type(kwargs[elem])
      sqt = ''
      if val is int:
        sqt = 'INT'
      elif val is str:
        sqt = 'TEXT'
      elif val is float:
        sqt = 'REAL'
      elif val is None:
        sqt = 'NULL'
      else:
        sqt = 'BLOB'
      newtypes.append(sqt)
    for idx in range(len(newcols)):
      ft.add_column(self.db, newcols[idx], newtypes[idx])
    self.create_product(**kwargs)



    
    

    


    
      
