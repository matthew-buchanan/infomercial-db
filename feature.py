import sqlite3

def star(cs, username, productid, stars):
  cs.execute(f'''
    SELECT rating from ratings WHERE 
    refproduct={productid}
    AND username="{username}";
    ''')
  res = cs.fetchall()
  if len(res) == 0:
    cs.execute(f'''
      INSERT INTO ratings (username, rating, refproduct)
      VALUES ("{username}", {stars}, {productid});
    ''') 
  else:
    cs.execute(f'''
      UPDATE ratings SET rating={stars} 
      WHERE username="{username}"
      AND refproduct={productid};
    ''')

def top(cs, productid=-1):
  pid = f'WHERE refproduct={productid} ' if productid > 0 else ""
  qry = f'''
    SELECT name, AVG(rating) as a1 from ratings 
    LEFT JOIN products on products.rowid=ratings.refproduct
    {pid} 
    GROUP BY name ORDER BY a1 DESC;
  '''
  cs.execute(qry)
  res = cs.fetchall()
  for item in res:
    print(f'{item[0]}: {item[1]:.2}/5')

#def count_nulls

  