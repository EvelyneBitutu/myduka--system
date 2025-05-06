from flask import Flask, render_template, request,redirect,url_for
from database import fetch_products, fetch_sales, insert_products, insert_sales, profit_per_product, profit_per_day, sales_per_product, sales_per_day,check_user, add_user
from flask_bcrypt import Bcrypt
#instantiating
app=Flask(__name__)

bcrypt=Bcrypt(app)


@app.route('/') 
def home():
    user={"name":"Evelyne","location":"Nairobi"}
    return render_template("index.html",data=user)



@app.route('/products')
def products():
    products=fetch_products()
    return render_template("products.html", products=products)

@app.route('/add_products',methods=['GET','POST'])
def add_product():
    if request.method=="POST":
        name=request.form['p-name']
        buying_price=request.form['b-price']
        selling_price=request.form['s-price'] 
        stock_quantity=request.form['s-quantity']
        new_product=(name,buying_price,selling_price,stock_quantity)
        insert_products(new_product)
        return redirect(url_for('products'))
   


@app.route('/sales')
def sales():
    sales=fetch_sales()
    products=fetch_products()
    return render_template("sales.html", sales=sales, products=products)


@app.route('/make_sale',methods=['POST'])
def make_sale():
    product_id=request.form['pid']
    quantity=request.form['quantity']
    new_sale=(product_id,quantity)
    insert_sales(new_sale)
    return redirect(url_for('sales'))
    

@app.route('/dashboard')
def dashboard():
    profit_data = profit_per_product()
    sales_data = sales_per_product()
    profit_day_data = profit_per_day()
    sales_day_data = sales_per_day()

    # list comprehension for product data(to get individual points)
    product_name = [i[0] for i in profit_data]
    p_profit = [float(i[1]) for i in profit_data]
    p_sales = [float(i[1]) for i in sales_data]

#day metrics data
    date = [str(i[0]) for i in profit_day_data]
    p_day = [float(i[1]) for i in profit_day_data ]
    s_day = [float(i[1]) for i in sales_day_data]

    return render_template("dashboard.html",
                           product_name=product_name, p_profit=p_profit, p_sales=p_sales,
                           date=date, p_day=p_day, s_day=s_day)



@app.route('/sample')
def sample():
    return render_template("sample.html")


@app.route('/register',methods=['POST'])
def register():
    name=request.form['name']
    email=request.form['email']
    phone_number=request.form['phone']
    password=request.form['password']

    hashed_password=bcrypt.generate_password_hash(password).decode('utf-8')
    user=check_user(email)
    if user==None:
        new_user=(name,email,phone_number,hashed_password)
        add_user(new_user)
        return redirect(url_for('login'))
    else:
        pass

    return render_template("register.html")


@app.route('/login',methods=['POST'])
def login():
    return render_template("login.html")

# run your app
app.run()


   