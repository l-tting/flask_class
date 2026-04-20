from flask import Flask , render_template
from database import get_products,get_sales

#creating a Flask instance
app = Flask(__name__)

# http://127.0.0.1:5000/ - url
@app.route('/') #decorator function
def home():#view function
    return  render_template('index.html')


# http://127.0.0.1:5000/products
@app.route('/products')
def products():
    products_data = get_products()
    return render_template("products.html")


@app.route('/sales')
def sales():
    sales_data = get_sales()
    return sales_data


@app.route('/stock')
def stock():
    return "This is the stock route"


@app.route('/dashbaord')
def dashboard():
    return "This is the dashbaord page"


@app.route("/login")
def login():
    return "This is the login route"


@app.route('/register')
def register():
    return "This is the regsiter route"






# run your application
app.run()
