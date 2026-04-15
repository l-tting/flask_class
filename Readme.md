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
2.Give the above BankAccount class the following behaviour or methods: -deposit() -withdraw() 
-display_info()
3.Create two BankAccount objects that can deposit, withdraw and display_info











