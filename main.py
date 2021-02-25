import sqlite3


name = 'coffee.db'
conn = sqlite3.connect(name)
cr = conn.cursor()
query = """SELECT * FROM coffee"""
res = cr.execute(query).fetchall()
print(res)
cr.execute(query)
conn.commit()
conn.close()
