import sqlite3

def create_product(cs, **kwargs):
  keys = tuple(kwargs.keys())
  vals = tuple(kwargs.values())
  query = f"INSERT INTO products {keys} "
  query += f"VALUES {vals}"
  try:
    cs.execute(query)
  except sqlite3.OperationalError as err:
    print(err)
    print('create_product_alt accepts any columns')
  
def create_product_alt(cs, **kwargs):
  colset = set(columns(cs))
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
    add_column(cs, newcols[idx], newtypes[idx])
  create_product(**kwargs)


def add_column(cs, title, datatype, table='products'):
  stmt = f'''
  ALTER TABLE {table} ADD COLUMN {title} {datatype}
  '''
  cs.execute(stmt)

def columns(cs):
  cs.execute('PRAGMA TABLE_INFO("products")')
  cols = cs.fetchall()
  names = [elem[1] for elem in cols]
  return names

def read_one(cs, id, colnames=False):
  try:
    query = f'''
      SELECT * FROM products WHERE rowid={id}
    '''
    cs.execute(query)
    results = cs.fetchall()
    if colnames:
      cols = columns(cs)
      zp = zip(cols, results)
      return dict(zp)
    else:
      return results
  except sqlite3.Error as err:
    return err

def find(cs, name):
  if len(name) is 0:
    return ValueError
  search = '%'.join(name) + '%'
  try:
    qry = f'''
      SELECT name, brand, price, 
      name like "{search}" as s1,
      brand like "{search}" as s2
      FROM products WHERE s1=1 OR s2=1;
    '''
    cs.execute(qry)
    results = cs.fetchall()
    return results
  except sqlite3.Error as err:
    print(err)
    print(qry)
  


def update(cs, col, val, id):
  try: 
    q_old = f'''
      SELECT {col} FROM products WHERE rowid={id}
    '''
    cs.execute(q_old)
    res = cs.fetchall()
    query = f'''
      UPDATE products SET {col}={val} WHERE rowid={id}
    '''
    cs.execute(query)
    return res
  except sqlite3.Error as err:
    return err

def delete(cs, id, name):
  query = f'''
    DELETE FROM products WHERE rowid={id} AND name={name}
  '''
  try:
    cs.execute(query)
    return "I don't blame you"
  except sqlite3.Error as err:
    return err