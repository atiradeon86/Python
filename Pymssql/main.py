import pymssql

server = "mssql.bryan86.hu"
user = "demo"
password = "Demo1234#"

conn = pymssql.connect(server, user, password, "AdventureWorks")
cursor = conn.cursor()

cursor.execute("SELECT P.FirstName, P.LastName FROM Person.Person P INNER JOIN Sales.SalesOrderHeader SH ON SH.CustomerID = P.BusinessEntityID WHERE P.EmailPromotion !=''")
row = cursor.fetchone()

while row:
    print("Firstname=%s, LastName=%s" % (row[0], row[1]))
    row = cursor.fetchone()
conn.close()