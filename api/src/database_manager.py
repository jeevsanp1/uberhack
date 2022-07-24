import sqlite3

conn = sqlite3.connect("../SUPPLIERS.db")
c=conn.cursor()
def get_suppliers(service,location):
    c.execute("SELECT Name FROM Suppliers WHERE ((Location = "+location+" )  AND (Services = "+service+"))" )
    return [i[0] for i in c.fetchall()]

def get_services(supplier):
    c.execute("SELECT Services FROM Suppliers WHERE Name ="+supplier)
    return [i[0] for i in c.fetchall()]

def get_costs(supplier):
    c.execute("SELECT Cost FROM Suppliers WHERE Name ="+supplier)
    strng = c.fetchall()[0][0]
    sstring = get_services(supplier)[0]
    nos = (len(sstring)+1)/2
    services=[]
    for i in range(0,int(nos)):
        services.append((sstring[0:sstring.find(",")]))
        sstring = sstring[sstring.find(",")+1:]
    costs = []
    for i in range(0,int(nos)):
        costs.append(int(strng[0:strng.find(",")]))
        strng = strng[strng.find(",")+2:]

    return(dict(zip(services, costs)))
conn.close()
