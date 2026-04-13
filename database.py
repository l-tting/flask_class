import psycopg2

#establishing connection to Postgres
conn = psycopg2.connect(host='localhost',port=5432,user='postgres',password='6979',dbname='myduka')

#object to perform db operations
cur = conn.cursor()

#fetching products
def get_products():
    cur.execute("select * from products")
    products = cur.fetchall()
    return products

product_data = get_products()
print(product_data)


#fetching sales
def get_sales():
    cur.execute("select * from sales")
    sales = cur.fetchall()
    return sales

sales_data = get_sales()
print(sales_data)


#fetching stock
def get_stock():
    cur.execute("select * from stock")
    stock = cur.fetchall()
    return stock

stock_data = get_stock()
print(stock_data)


def get_data(table):
    cur.execute(f"select * from {table}")
    data = cur.fetchall()
    return data

products = get_data('products')
sales = get_data('sales')


def insert_products(product_details):
    cur.execute(f"insert into products(name,buying_price,selling_price)values{product_details}")
    conn.commit()

product1 = ('iphone 12',45000,55000)
product2 = ('calculator',1000,1500)
insert_products(product1)
insert_products(product2)

