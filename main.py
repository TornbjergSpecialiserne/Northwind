import mysql.connector


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
    query = f"SELECT * FROM products"
    cursor.execute(query)
    productData = cursor.fetchall()

    # Find UK & Spain customere
    query = "SELECT * FROM customers"
    cursor.execute(query)
    customerData = cursor.fetchall()

    # Close cursor and connection
    cursor.close()
    conn.close()

    # Show produkt after Unit Price (UP)
    productData.sort(key = lambda x: x['UnitPrice'])
    for line in productData:
        print(f"{line['ProductName']}: ${round(line['UnitPrice'], 2)}")
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

except mysql.connector.Error as err:
    print(f"Error: '{err}'")    
