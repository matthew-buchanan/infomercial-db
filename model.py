from connect import Connect
import sqlite3 

class Model(Connect):
  def __init__(self):
    super().__init__()
    self.c.execute('''
        CREATE TABLE if not exists products 
        (name text, brand text, price real)
        ''')
  def seed(self, new=False):  
    if new:
      self.c.execute('''
      DROP TABLE products;
      CREATE TABLE products 
        (name text, brand text, price real);
      ''')
    data = '''
    ("Jenga Classic Game", "Jenga", 10.27),
    ("Fire TV Stick", "Amazon", 49.99),
    ("Wyze Cam", "Wyze Labs", 34.98),
    ("Animal Crossing: New Horizons", "Nintendo", 59.99),
    ("Men's Ecosmart Fleece Sweatshirt", "Hanes", 7.99)
    '''
    qry = '''INSERT INTO products (name, brand, price)
    VALUES ''' + data
    self.c.execute(qry)
  def make_ratings(self):
    try:
      qry = '''
      CREATE TABLE ratings (
        username text, 
        rating integer 
          CHECK (rating > 0 and rating <= 5),
        review text,
        refproduct integer,
        FOREIGN KEY (refproduct) REFERENCES products(rowid)
      );
      '''
      self.c.execute(qry)
    except sqlite3.Error as err:
      print(err)
  def __repr__(self):
    self.c.execute('PRAGMA TABLE_INFO("products")')
    return str(self.c.fetchall())
  
if __name__=='__main__':
  m = Model()
  m.seed_new()
  m.example()
  print('products table created.')
  m.end()

