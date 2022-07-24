import sqlite3
conn = sqlite3.connect("C:/Users/Owner/Desktop/SUPPLIERS.db")
c=conn.cursor()
def get_suppliers(service,location):
    c.execute("SELECT Name FROM Supplier WHERE ((Location = "+location+" )  AND (Services = "+service+"))" )
    return [i[0] for i in c.fetchall()]
def get_services(supplier):
    c.execute("SELECT Services FROM Supplier WHERE Name ="+supplier)
    return [i[0] for i in c.fetchall()]

conn.commit()