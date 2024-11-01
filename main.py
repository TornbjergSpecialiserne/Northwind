import mysql.connector

def GetTable(cursor:mysql, tableName:str):    
    query = f"SELECT * FROM {tableName}"
    cursor.execute(query)
    return cursor.fetchall()


try:
    # Connect to the database
    conn = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "bWsEocb2r706!",
        database = "Northwind"
    )

    # Create cursor object
    cursor = conn.cursor(dictionary=True)

    # Get products
    productData = GetTable(cursor, 'products')
    # Find UK & Spain customere
    customerData = GetTable(cursor, "customers")
    # Lands with orders
    ordersData = GetTable(cursor, 'orders')

    # Close cursor and connection
    cursor.close()
    conn.close()

    # Show produkt after Unit Price (UP)
    print("Products")
    productData.sort(key = lambda x: x['UnitPrice'])
    for line in productData:
        print(f"{line['ProductName']}: ${round(line['UnitPrice'], 2)}")
    print()

    # Show produkts with 100 or more unites on lager & is 25 or more
    print("Priority produkts")
    priorityProdukts = []
    for row in productData:
        if(row['UnitPrice'] >= 25 and row['UnitsInStock'] > 100):
            priorityProdukts.append(row)
    print(len(priorityProdukts))
    print()

    # Show Customere from UK & Spain
    shopsInReigon = []
    # Sort data
    for line in customerData:
        if(line['Country'] == "UK" or line['Country'] == "Spain"):
            shopsInReigon.append(line)
    shopsInReigon = sorted(shopsInReigon, key=lambda x: x['Country'])
    # Show data
    for line in shopsInReigon:
        print(f"{line['Country']}: {line['CompanyName']}")
    print()

    # Lands with orders
    print("Lands with orders")
    landsWithOders  = []
    for row in ordersData:
        if(row['ShipCountry'] not in landsWithOders):
            landsWithOders.append(row['ShipCountry'])
    landsWithOders.sort()
    print(len(landsWithOders))
    for land in landsWithOders:
        print(land)

except mysql.connector.Error as err:
    print(f"Error: '{err}'")    
