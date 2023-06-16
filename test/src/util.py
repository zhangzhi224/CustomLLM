import pandas as pd
import sqlite3

def db_connector():
    conn = sqlite3.connect('../db/sqlite/data.db')
    print("Opened database successfully")
    res = conn.execute("SELECT *  from GoodCountryIndex")
    df = pd.DataFrame(res,columns=['country','gdp','happiness_index'])
    conn.close()
    print("\r\nstart-------------------------------------")
    print(df)

