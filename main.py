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
    return render_template("sales.html")


@app.route('/stock')
def stock():
    return render_template("stock.html")


@app.route('/dashboard')
def dashboard():
    return render_template("dashboard.html")


@app.route("/login")
def login():
    return render_template("login.html")


@app.route('/register')
def register():
    return render_template("register.html")



# run your application
app.run()
