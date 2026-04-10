import psycopg2

#establishing connection to Postgres
conn = psycopg2.connect(host='localhost',port=5432,user='postgres',password='6979',dbname='myduka')

#object to perform db operations
cur = conn.cursor()

cur.execute("select * from products")
products = cur.fetchall()
print(products)

cur.execute("select * from sales")
sales = cur.fetchall()
print(sales)

cur.execute("select * from stock")
stock = cur.fetchall()
print(stock)


cur.execute("insert into products(name,buying_price,selling_price)values('asus laptop',50000,60000)")
conn.commit()
print(products)