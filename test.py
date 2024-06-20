import psycopg2
def search_db(query: str):
    """Used to search on the database"""
    conn = psycopg2.connect(host="localhost", dbname="finance", user='dev', password="93148325", port="5432")
    cur = conn.cursor()
    cur.execute("""SELECT * FROM stock_performance""")
    res = cur.fetchall()
    conn.commit()
    cur.close()
    conn.close()
    return res

print(search_db(""))