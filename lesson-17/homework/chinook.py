import sqlite3
import pandas as pd

#merging and joining

conn=sqlite3.connect("chinook.db")

cc=conn.cursor()

customers_query="select * from customers"
invoices_query="select * from invoices"

customers=pd.read_sql(customers_query,conn)
invoices=pd.read_sql(invoices_query,conn)

df=pd.merge(customers,invoices,on="CustomerId")

df1=df.groupby(["CustomerId","LastName"])["InvoiceId"].count().reset_index()

# print(customers)
# print(invoices)

print(df1)

conn.close()