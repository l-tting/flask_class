*INTRODUCTION TO FLASK*
Create a new project called MyDuka
Create two files in this project:
 - database.py
 - main.py

Next:
Open up a terminal (ctrl + j) and run the following commands:
1. pip install psycopg2-binary
2. pip install flask


pip - pip installs packages  - install external libraries in Python


create database myduka;

\c myduka


create the following tables: products , sales, stock , users
main.py - server file
database.py - database file

*psycopg2* - a database driver / adapter ued to connect Python to a postgres database
*psycopg2,connect()* - a function used to establish a connection between Python and Postgres

conn - variable establishing a connection between Python and Postgres

1.host - where is your database located? 
     - localhost (your own device)
2.port - where exactly on my device or server is my database located
3.user - username of a user accessing the Postgres database
4.password - password attached to a user to authenticate a user trying to access Postgres
5.dbname - the specific database you're trying to connect to

*cur* - an object / tool used to perform database operations(select,insert,update,delete)
cur.execute() - a function to execute sql queries
cur.fetchall() - a  function to retrieve data from postgres to python 

what is yout data format? - how is your data stored? => list of tuples


numbers = [1,2,3,4,5] - list

[(3, 'bread', Decimal('60.00'), Decimal('65.00')), (4, 'bread', Decimal('50.00'), Decimal('60.00')), (5, 'samsung phone', Decimal('50000.00'), Decimal('60000.00'))]

*list* - contains your entire dataset
*tuple* - contains a single record / row

*Inserting data in psycopg2*
-> insert query : insert into table_name(col1,col2,...)values(val1,val2,....)

"insert into products(name,buying_price,selling_price)values("laptop",50000,60000)"

*conn.commit()* - a function meant to commit / save data in the database


*FUNCTIONS*
-> A block of reusable code meant to perform specific tasks

*why use functions?*
1.Code reusability - reduces repitition
2.Modularity - breaking large code into smaller manageable and reusable pieces
3.Code written in functions is easier to maintain and scale
4.Better debugging
5.Better readability

*Parts of a function*
1.function definition 
   - creating a function using the def keyword + giving the function a name + possible parameters
   - e.g def get_result()
2.function body
   - part of the function that executes the intended task
3.function call
   - calling a function by its name to perform the task laid out in the function body 


*Note* - a function is made reusable by the use of parameters & arguments

*Parameters vs Arguments*
-> Parameter : a placeholder variable / value meant to make a function reusable
-> Arguments : are real values passed in place of parameters when callng the function
*N/B* - the no & order of parameters matches the no & order of arguments

-> Functions typically use the return keyword 
 *return* - gives back the result of a function and also signifies the end of function 

 *Variable Scope*
-> Defines where a variable can be accessed from in a program
-> We have 2 variable scopes:
*1.Global scope* 
 -> Variables / data in the global scope can be accessed from anywhere in the program
 -> Variables in the global scope are called global variables
*2.Local scope*
 -> Variables / data in the local scope can only be accessed in its defined scope
 -> Variables in the local scope are called local variables
 Research on types of functions (inbuilt vs user defined functions)


 *task*
Optimize your program in database.py by using functions to either select or insert data


CREATE TABLE products (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    buying_price NUMERIC(20, 2) NOT NULL CHECK (buying_price >= 0),
    selling_price NUMERIC(20, 2) NOT NULL CHECK (selling_price >= 0)
);

CREATE TABLE stock (
    id SERIAL PRIMARY KEY,
    pid INTEGER NOT NULL REFERENCES products(id) ON DELETE CASCADE,
    stock_quantity INTEGER NOT NULL CHECK (stock_quantity >= 0),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE sales (
    id SERIAL PRIMARY KEY,
    pid INTEGER NOT NULL REFERENCES products(id) ON DELETE CASCADE,
    quantity INTEGER NOT NULL CHECK (quantity > 0),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    full_name VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL UNIQUE,
    phone_number VARCHAR(100) NOT NULL,
    password VARCHAR(255) NOT NULL
);
  


*SQL MUST KNOW*
1.basic sql queries
2.primary and foreign keys
3.joins and aliases
4.aggregate functions (max,min,count,avg,sum)
5.group by & order by
6.where clause

*PYTHON MUST KNOW*
1.Functions
2.Loops
3.If statements
4.Python data structures -lists & tuples and their properties
5.data types 


products - id, name , buying_price, selling_price
sales - id, pid, quantity, created_at

*sales per product* - sales, product
sales = quantity * selling_price

*JOINS*
Enables us to fetch data from more than one table based on a related column 



 id | pid | quantity |         created_at         
----+-----+----------+----------------------------
  1 |   3 |       50 | 2026-04-10 15:06:40.615398
  2 |   3 |       40 | 2026-04-10 15:06:40.615398
  3 |   3 |       10 | 2026-04-10 15:06:40.615398



*TASK 13-04*
1.Using functions insert the following data: stock, sales, users 
2.Write sql queries to fetch the following data:
   - *sales per product*
   - sales per day
   - profit per product
   - profit per day

   *2nd method to insert data* 




   *multiline string*
-> A frmat of writing strings where a string is allowed to traverse / cover more than a single line
-> By default , strings use either the ' ' or " "
-> Multiline strings use """ """ or ''' '''


sales per day
sales = quantity * selling_price
day - time component

products - id, name, buying_price,selling_price
sales -id,pid,quantity , created_at

profit = (selling_price - buying_price) * quantity
*sales per products*
select products.name as p_name , sum(quantity * selling_price) as total_sales from sales join products 
on products.id = sales.pid group by p_name;

*sales per day*
select date(sales.created_at) as day, (sales.quantity * products.selling_price) as total_sales from products join sales 
on sales.pid = products.id group by day;

*profit per product*
select products.name as p_name , sum((selling_price - buying_price) * quantity) as total_profit
from sales join products on sales.pid = products.id group by p_name;

*profit per day*
select date(sales.created_at) as day, sum((selling_price - buying_price) * quantity) as total_profit
from sales join products on sales.pid = products.id group by day;


*Inserting data using placeholders*
-> Here we use placeholders to safely add data to tables instead of usiing f-string
-> using f-string in sql queries is prone to SQL injection

*sql injection*
 -> an attack where someone tricks your database into running unintended sql commands by inserting malicious
 inputs into yout query

e.g.
def get_user(name,password):
    cur.execute(f"select * from users where users.name = 'admin' and password = '' OR '1' = '1')
   1 = 1
   name : admin
   password : '' OR '1' = '1'
   To prevent sql injection here , we use placeholders to insert data

*task 14-04*
1.change all your insert functions to use placeholders instead of f-strings



*INTRODUCTION TO OOP*
-> We have a broad classification of data types namely:
1.Inbuilt data types 
   -> Come predefined with the programming language 
   -> int,float,str,bool,list,tuple, dict
2.User defined types
   -> Are custom data types created by the programmer 
   -> is enabled by object oriented programmng


*OOP*
-> Object Oriented Programming => this is a concept whereby programs are built using classes and objects
*Class* - a blueprint / template for creating objects
*Object* - an instance of a class

*Properties of a class*
-> Any class has the following properties:
1.Identity
   -> the unique name of the class / object
2.State
   -> Variables contained inside a class
   -> Variables contained inside a class are called *attributes*
   -> what do i have? 
3.Behaviour
   -> represents what a class can do
   -> enabled by use of functions
   -> functions inside classes are called *methods*

-> We create classes using the 'class' keyword

class Phone
   attributes / state - memory, colour, storage, make, model ,imei
   behaviour - call, ring, text, tweet, play_games, power_on, power_off, take_photos,download_apps

class Dog
    attributes - name, age, breed
    behaviour - bark, bite, sleep, chase, walk,eat,sleep

Class Programmer
    attributes -  name, favourite language, experience
    behaviour - write code, debug code, use github

class Laptop 
   attributes - memory , colour, size, storage, processor, os , 
   behaviour - power_on, power_off, code, watch_movies, download_software

Class Doctor:
	Attributes: name, age, department, 
	Behaviour: treats, diagnoses, assess

class Car
   attributes - make, model , yom , fuel_capacity, 
   behaviour - drive, stop, start, stall , carry_good


*Method* - a function inside a class
*Constructor* - a special method used to initialize objects. It is automatically called when 
     creating an object . In Python , we use the __init__(self,parameters) constructor
*self* - reference the object created
*parameters* - attributes of the class

dunder_methods -> double underscore methods



*task 15-04*
OOP Task 
1.Create a class called BankAccount with the following attributes: -account number -balance -owner name -date opened
2.Give the above BankAccount class the following behaviour or methods: -deposit() -withdraw() -display_info()
3.Create two BankAccount objects that can deposit, withdraw and display_info

*task 16-04*
1.Create a Car Class Have the following attributes brand - model - year -fuel_capcity - fuel_level -is_running(boolen value) Have the following methods as behaviour for your class: start() stop() refuel() drive() display_car_info()


*OOP Concepts*
1.Inheritance 
2.Polymorphism
3.Abstraction
4.Encapsulation
5.Method overriding and Method Overloading


*PYTHON CONTROL STRUCTURES*
->Control structures are building blocks that control the flow of execution in a program. They decide what code runs, when it runs and how many times
it runs
-> We have 3 control structures:
1.Sequence 
   - a program executes from top to bottom , left to right
2.Selection /Decision Control
   -> the ability of a program to make decisins based on some condition
   -> use of conditional statements e.g if statements
3.Iteration
    -> execution of a block of code repeatedly
    -> Looping controls -> for and while

   *LOOPING*
-> Loops are used to execute a block of code repeatedly. They help reduce redundancy & tedious work
-> Types of Loops:
1.for loop
    -> used when you know how many times you want to repeat something
2.while loop
    -> executes code repeatedly until a condition becomes false

*break* - stop the loop immediately
*continue* - skip the current iteration

*Nested Loops*
-> A loop inside another loop
-> The outer loop runs first, and for each iteration of the outer loop, the inner loop runs completely


*Classes*
*dunder methods* - are special methods that let you defines how your objects behave with inbuilt operations
*instance variables* -> name mangling

*Aggregate Functions*
-> take multiple rows and return a single summarized / computed value
-> Aggregate functions are almost always used with GROUP BY

1.Count - counts rows
2.Max - returns largest value
3.Minn- return smallest value
4.Avg. - computes arithmetic average
5.Sum - adds numeric values















*INTRODUCTION TO FLASK*
*Internet* - global network of connected devices or computers
*www* - a service running on the internet that connects users to the internet via the browser
*server* - a computer device used for receiving / sending data from a client
*Hosting* - uploading application files to a server to make the application available to everyone online

Build your application -----> Uploading app files to a server ----> Ip address is assigned to your app ----> Users can now access it

*IP Address* - a number used to uniquely identify a device on a network
  types of ip addresses -> ipv4 and ipv6
  e.g. 172.181.405.220

*Domain name* - a user friendy name used in place of complex ip addresses to access applications
  e.g. google.com

*DNS* - Domain Name System - the internet's phonebook used to match domain names to ip addresses  

127.0.0.1 - > ip address of your own local device
localhost -> domain name for 127.0.0.1

*FLASK*
-> A python framework used to build web applications

*Framework vs Library*
approach 1 -  very strict on guidelines but easier - framework
approach 2 - very flexible but harder - library

*Framework* - a prebuilt structure of code and tools used to help developers build applications by 
not having to create everything from scratch. They easen the development process but have very strict
guidelines on usage

*Examples of frameworks*
1.Python - Flask,Django,FastAPI
2.PHP - Laravel
3.JavaScript - React, Angular, Vue,Svelte
4.Java - Spring
5.C# - .NET
6.Golang - Chi , Gin
7.NodeJS - Express
8.Ruby - Ruby on Rails

*ROUTING IN FLASK*
-> Routing is the mechanism that maps / connects URLs to Python functions. It is a system for resource navigation.
-> Connects a URL to functions in your Flask app

*URL* -> uniform resource locator - the full address used to access an application
 e.g. https://meet.google.com/dsh-idtb-oqb

 *parts of a url*
 1.Protocol - tells the browser how to communicate (http<sends data as raw text> or https<data is encrypted>)
 2.Domain name - name of the application  e.g meet.google.com
 3.Port (optional) - where exactly on a server is the service running
 4.Path - path to a specific resource e.g /login ,/register

 *Routing in Flask*
 -> Its enabled by the use of a decorator function called @app.route()
 *decorator function* is a special function that determines / modifies the behaviour of another function
 they have the '@' character as a prefix
 *app.route()* can take some arguments :
    1.Rule / path - the specific resource to be accessed e.g / , /products
    2.Method

 *view function*: a function responsible for returning resources to a client


 *NOTE* - all view functions must have unique names , no view functions can share the same name

 *Instead of returning a single piece of data e.g products data , we should instead return full html pages e.g products.html
 and in these html pages , we display our data and more content
 Adjust your project structure to the one below:
    
    static - a folder containing all static files (css files, images, videos, icons, favicons)
    templates - a folder containing all html files
              - a single html file is called a template
    database.py
    main.py

To render / display html pages in flask, we use render_template() function imported from flask


*TEMPLATE INHERITANCE*
-> This is a feature that enables us to reduce redundancy in building html pages by having one parent template called base.html conataining all common features of all pages e.g navbar , footer and then have the rest of the pages inherit from it
*why use template inheritance?*
1.Reduce redundancy
2.Uniformity
3.Simpler development process

{% block title %} {% endblock %} -> defines a placeholder to define a title for child pages
{% block content %} {% endblock   %} -> defines a placeholder block where unique content of each page is passed

-> To implement template inheritance , we go to the child page and extend the parent



*DISPLAYING DATA IN FLASK*
-> To  render / display data from Python in HTML we use Jinja
-> *Jinja* - a templating engine used to render dynamic html pages in Flask - It is simply
syntax ussed to display Python data in html
-> Jinja can be used in two ways:
1.When displaying variables 
   -> use two curly braces {{}}
2.When using control structures (conditional statements, Loops)
  -> use the followng syntax:

  {% for product in products %} -> initialization block

       {{ product }}

   {% endfor %} - termination

   {% if i%2 == 0 %}
     
       {{ i }}

   {% endif %}
     

*Posting Data In Flask*
Posting -> moving data from a client to a server 

*Workflow / Process*
1.User is provided with a form to fill in the browser
2.User fills the form and submits it to the server
3.The form is submitted to a route in Flask
4.Data from the form is extracted by a request object 
    -> Data from the from is stored in key-value pairs
    -> request object extracts the value using the key 
    -> request object has access to some methods:
       1.request.method - determines what method is specified in the form
       2.request.form - extracts data from the form using key defined in the name attirbute
5.Data is processed and inserted in database
6.User is redirected - here we use the redirect() function - taking them to another section / resource
   redirect(url_for('')) - pass the name of the view function


*Form CheckList*
1.method attribute - method determines what a server should do with data / a resource
                    1.GET - retrive data from the server e.g. displaying products
                    2.POST - sending data to a server e.g. adding products
                    3.PUT. - updating an existng resource / data e.g changing product name
                    4.DELETE - get rid of data e.g delete a product
2.action attribute  - determines what route the form is submitted
3.name attribute - is the key used by the request object to access & extract data from the form
4.input type
5.button - type submit


p_name : "milk"
b_price: "50"
s_price: "60"
   

*TASK*
Post sales and stock data following the same process as posting products


*Flash Messaging* 
-> Flash Messages are one time notifications to a user based on some action. Flash messages are stored in the server in session storage. 
-> Any data stored in session must be secured using a secret key
-> Flash messages contain 2 parts:
1.Message  - the actual feedback e.g. Product Added Successfully
2.Message Category - type of message 

*Messsage Categories*
1.Informational messages - blue
2.Success messages - green
3.Warning Messages - yellow
4.Error / Danger Messsages - red

flash messages are enabled by the flash() function imported from flask
 -> flash(message,category)


*TASK*
1.Replace every print message with a flash message
2.In database.py , using functions write queries to do the following:
    a) insert users -> create_user()
    b) check whether a user exists using their email -> check_user_exists()



*Making Purchases*
add products -> add stock on products -> make sales on products in stock - stock is updated
-> check for sufficient stock before making another sale

milk ---> 1000 ----> 500 ----> 500 remaining 

 id | pid | stock_quantity |         created_at         
----+-----+----------------+----------------------------
  1 |   3 |             50 | 2026-04-10 15:06:58.088418
  2 |   7 |             50 | 2026-04-14 16:17:05.637068
  3 |   8 |             25 | 2026-04-14 16:17:05.639132
  4 |   7 |             50 | 2026-04-20 15:57:36.926479
  5 |   8 |             25 | 2026-04-20 15:57:36.92891
  6 |   7 |             50 | 2026-04-20 15:57:51.80367
  7 |   8 |             25 | 2026-04-20 15:57:51.815576
  8 |   7 |             50 | 2026-04-20 16:06:56.800811
  9 |   8 |             25 | 2026-04-20 16:06:56.805105
 10 |   7 |             50 | 2026-04-20 16:07:02.566926



100 packets of milk -> 40 sold ---> 60 in stock
100 - 40 = 60

milk => 100 + 50 + 40 + 30 = 220
milk => 20 + 60 + 80  => 160


cur.fetchall() -> returns multiple rows as a list of tuples 
cur.fetchone() -> returns a single row in a tuple (250,)

add bread -> add 100 stock -> no sale

zero -> 100 - 100 = 0
null / none


100 - null


*User Registration, Authentication & Login*
Post a user in the users table using register route











