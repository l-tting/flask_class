from flask import Flask, render_template,request,redirect,url_for,flash,session
from database import get_products, get_sales, insert_products, insert_sale,insert_stock,get_stock,available_stock,insert_user,check_user_exists,sales_per_day,sales_per_product,profit_per_day,profit_per_product
from flask_bcrypt import Bcrypt
from functools import wraps

#creating a Flask instance
app = Flask(__name__)

#bcrypt
bcrypt = Bcrypt(app)


app.secret_key = 'ss9iennd88dsbbc8wshsjjsj'

#  http://127.0.0.1:5000/
@app.route('/') #decorator function
def home(): #view function
    return render_template('index.html')


def login_required(f):
    @wraps(f)
    def protected(*args,**kwargs):
        if 'email' not in session:
            return redirect(url_for('login'))
        return f(*args,**kwargs)
    return protected


# http://127.0.0.1:5000/products
@app.route('/products')
@login_required
def products():
    products_data = get_products()
    return render_template('products.html',products_data = products_data)


@app.route('/add_product',methods=['GET', 'POST'])
def add_product():
    if request.method == 'POST':
        product_name = request.form['p_name']
        buying_price = request.form['b_price']
        selling_price = request.form['s_price']
        new_product = (product_name,buying_price,selling_price)
        insert_products(new_product)
        flash("Product added successfully",'success')
    return redirect(url_for('products'))


@app.route('/sales')
@login_required
def sales():
    sales_data = get_sales()
    products_data = get_products()
    return render_template('sales.html',sales_data = sales_data,products_data = products_data)


@app.route('/add_sale',methods= ['GET','POST'])
def add_sales():
    if request.method == 'POST':
        product_id = request.form['pid']
        quantity = request.form['quantity']

        check_stock = available_stock(product_id)
        if check_stock < float(quantity):
            flash("Insufficient stock,can't complete sale",'danger')
            return redirect(url_for('sales'))
        new_sale = (product_id,quantity)
        insert_sale(new_sale)
        flash("Sale added successfully",'success')
    return redirect(url_for('sales'))



@app.route('/stock')
@login_required
def stock():
    stock_data = get_stock()
    product_data = get_products()
    return render_template("stock.html",stock_data = stock_data,product_data = product_data)



@app.route('/add_stock',methods= ['GET',"POST"])
def add_stock():
    if request.method == 'POST':
        product_id = request.form['pid']
        stock_quantity = request.form['stock_quantity']
        new_stock = (product_id,stock_quantity)
        insert_stock(new_stock)
        flash("Stock added successfully",'success')
    return redirect(url_for('stock'))



@app.route('/dashboard')
@login_required
def dashboard():
    sales_product = sales_per_product()
    sales_day = sales_per_day()
    profit_product = profit_per_product()
    profit_day = profit_per_day()

    
    #product data
    product_names = [ i[0] for i in sales_product ]
    product_sales = [ float(i[1]) for i in sales_product ]
    product_profit = [ float(i[1]) for i in profit_product ]

    # #day data
    day = [ str(i[0]) for i in sales_day ]
    day_sales = [ float(i[1]) for i in sales_day ]
    day_profit = [ float(i[1]) for i in profit_day ]

    return render_template("dashboard.html", 
              product_names = product_names, product_sales=product_sales, product_profit = product_profit,
               day = day , day_sales = day_sales , day_profit= day_profit            
                           )



@app.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        existing_user = check_user_exists(email)
        if not existing_user:
            flash("User doesn't exist,please register",'danger')
        else:
            if bcrypt.check_password_hash(existing_user[-1],password):
                session['email'] = email
                flash("Login successful",'success')
                return redirect(url_for('dashboard'))
            else:
                flash("Password incorrect",'danger')
    return render_template("login.html")


@app.route('/register',methods=['GET','POST'])
def regsiter():
    if request.method == 'POST':
        full_name = request.form['name']
        email = request.form['email']
        phone_number = request.form['phone']
        password = request.form['password']

        existing_user = check_user_exists(email)
        if not existing_user:
            hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
            new_user = (full_name,email,phone_number,hashed_password)
            insert_user(new_user)
            flash("User created successfully",'success')
        else:
            flash("User exists already ,please login",'danger')
    return render_template("register.html")


#logging out by removing email from session
@app.route('/logout')
def logout():
    session.pop('email',None)
    flash("User logged out successfully","success")
    return redirect(url_for('login'))


app.run(debug=True)