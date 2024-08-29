import psycopg2
from langchain.tools import tool

class SECTools():
  @tool("Database Search for all hsi stocks")
  def search_db_hsi(query: str):
    """Used to provide the full database information for all stocks related to HSI 
    with the schema (id, stock_id, stock_name, risk, roi, sharpe_ratio, correlation_to_hsi, pe_ratio, var)"""
    conn = psycopg2.connect(host="localhost", dbname="finance", user='dev', password="93148325", port="5432")
    cur = conn.cursor()
    cur.execute("""SELECT * FROM stock_performance_hsi_1y""")
    res = cur.fetchall()
    conn.commit()
    cur.close()
    conn.close()
    return res
  
  @tool("Database Search for all sse stocks")
  def search_db_sse(query: str):
    """Used to provide the full database information for all stocks related to sse 
    with the schema (id, stock_id, stock_name, risk, roi, sharpe_ratio, correlation_to_sse, pe_ratio, var)"""
    conn = psycopg2.connect(host="localhost", dbname="finance", user='dev', password="93148325", port="5432")
    cur = conn.cursor()
    cur.execute("""SELECT * FROM stock_performance_sse_1y""")
    res = cur.fetchall()
    conn.commit()
    cur.close()
    conn.close()
    return res
  
  @tool("Database Search for all nasdaq stocks")
  def search_db_nasdaq(query: str):
    """Used to provide the full database information for all stocks related to nasdaq 
    with the schema (id, stock_id, stock_name, risk, roi, sharpe_ratio, correlation_to_nasdaq, pe_ratio, var)"""
    conn = psycopg2.connect(host="localhost", dbname="finance", user='dev', password="93148325", port="5432")
    cur = conn.cursor()
    cur.execute("""SELECT * FROM stock_performance_nasdaq_1y""")
    res = cur.fetchall()
    conn.commit()
    cur.close()
    conn.close()
    return res
  
  @tool("Database Search for particular stock")
  def search_db_stock(query: str, index: str):
    """Used to provide the full database information for queried stock related to index 
    with the schema (id, stock_id, stock_name, risk, roi, sharpe_ratio, correlatio_to_index, pe_ratio, var),
    the possible input of index is hsi, sse, and nasdaq only"""
    conn = psycopg2.connect(host="localhost", dbname="finance", user='dev', password="93148325", port="5432")
    cur = conn.cursor()
    cur.execute(f"""SELECT * FROM stock_performance_{index}_1y WHERE stock_id LIKE '{query}'""")
    res = cur.fetchall()
    conn.commit()
    cur.close()
    conn.close()
    return res
  
  