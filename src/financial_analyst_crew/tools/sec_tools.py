import psycopg2
from langchain.tools import tool

class SECTools():
  @tool("Database Search for all stocks")
  def search_db(query: str):
    """Used to provide the full database information for all stocks related to HSI 
    with the schema (id, stock_id, stock_name, risk, roi, sharpe_ratio, correlation_to_hsi, pe_ratio, var)"""
    conn = psycopg2.connect(host="localhost", dbname="finance", user='dev', password="93148325", port="5432")
    cur = conn.cursor()
    cur.execute("""SELECT * FROM stock_performance""")
    res = cur.fetchall()
    conn.commit()
    cur.close()
    conn.close()
    return res
  
  @tool("Database Search for particular stock")
  def search_db_stock(query: str):
    """Used to provide the full database information for queried stock related to HSI 
    with the schema (id, stock_id, stock_name, risk, roi, sharpe_ratio, correlatio_to_hsi, pe_ratio, var)"""
    conn = psycopg2.connect(host="localhost", dbname="finance", user='dev', password="93148325", port="5432")
    cur = conn.cursor()
    cur.execute(f"""SELECT * FROM stock_performance WHERE stock_id LIKE '{query}'""")
    res = cur.fetchall()
    conn.commit()
    cur.close()
    conn.close()
    return res
  
  