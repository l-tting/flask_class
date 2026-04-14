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



def insert_stock(stock_details):
    cur.execute("insert into stock(pid,stock_quantity)values(%s,%s)",(stock_details))
    conn.commit()

stock1 = (5,40)
stock2 = (6,70)
insert_stock(stock1)
insert_stock(stock2)







def sales_per_product():
    cur.execute('''
                select products.name as p_name , sum(quantity * selling_price) as total_sales 
                from sales join products on products.id = sales.pid group by p_name;
    ''')
    sales_product = cur.fetchall()
    return sales_product


def sales_per_day():
    cur.execute('''
        select date(sales.created_at) as day, (sales.quantity * products.selling_price) as 
        total_sales from products join sales on sales.pid = products.id group by day;
    ''')
    sales_day = cur.fetchall()
    return sales_day


def profit_per_product():
    cur.execute('''
        select products.name as p_name , sum((selling_price - buying_price) * quantity) as total_profit
        from sales join products on sales.pid = products.id group by p_name;
    ''')
    profit_product = cur.fetchall()
    return profit_product

def profit_per_day():
    cur.execute('''
        select date(sales.created_at) as day, sum((selling_price - buying_price) * quantity) as total_profit
        from sales join products on sales.pid = products.id group by day;
    ''')
    profit_day = cur.fetchall()
    return profit_day

