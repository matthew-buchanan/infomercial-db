class Connect:
  def __init__(self):
    import sqlite3
    self.conn = sqlite3.connect('infomercial.db')
    self.c = self.conn.cursor()
  def end(self):
    self.conn.commit()
    self.conn.close()
  
