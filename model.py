from connect import Connect

class Model(Connect):
  def __init__(self):
    super().__init__()
  def seed(self):  
    self.c.execute('''
        CREATE TABLE IF NOT EXISTS products 
        (name text, brand text, price real)
        ''')
  def seed_new(self):
    self.c.execute('''
      DROP TABLE IF EXISTS products
      ''')
    self.seed()
  def example(self):
    empty = '''
      SELECT COUNT(*) FROM products LIMIT 5
    '''
    data = '''
    ("Jenga Classic Game", "Jenga", 10.27),
    ("Fire TV Stick", "Amazon", 49.99),
    ("Wyze Cam", "Wyze Labs", 34.98),
    ("Animal Crossing: New Horizons", "Nintendo", 59.99),
    ("Men's Ecosmart Fleece Sweatshirt", "Hanes", 7.99)
    '''
    query = '''INSERT INTO products (name, brand, price)
    VALUES ''' + data
    self.c.execute(query)
  def __repr__(self):
    self.c.execute('PRAGMA TABLE_INFO("products")')
    return str(self.c.fetchall())
  
if __name__=='__main__':
  m = Model()
  m.seed_new()
  m.example()
  print(repr(m))
  m.end()

