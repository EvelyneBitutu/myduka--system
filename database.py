import psycopg2
from datetime import datetime


# Create a connection to the database
conn = psycopg2.connect(user="postgres", password="bitutu", host="localhost", port="5432", database="myduka")

# Execute database operations
cur = conn.cursor()
# now=datetime.now()


# # Query to fetch products
def fetch_products():
    cur.execute("SELECT * FROM products")
    products = cur.fetchall()
    return products
    

# # Query to fetch sales
def fetch_sales():
    cur.execute("SELECT * FROM sales")
    sales = cur.fetchall()
    return sales
    

# Call the functions

# fetch_sales()


def insert_products():
    cur.execute("insert into  products(name,buying_price,selling_price)values('mandazi',100,150)")
    conn.commit()


# conn.commit()
# fetch_products()

def insert_sales():
    cur.execute(f"insert into sales(id,pid,quantity,created_at)values(80,3,4,'2023-10-01 12:00:00')")
    conn.commit()

# insert_products()
# insert_sales()

# fetch_products()
# fetch_sales()


# task querry(review)
def fetch_data(table):
    cur.execute(f'SELECT * FROM {table} ;')
    data = cur.fetchall()
    return data

products=fetch_data('products')
print("Products after insertion:\n", products)
sales = fetch_data('sales')
print("products from fetch data funct:\n", products)
print("products from fetch data funct:\n", sales)

#insert products -method 1 takes values as parameters

def insert_products(values):
   insert = "INSERT INTO products(name, buying_price, selling_price, stock_quantity) VALUES (%s, %s, %s, %s)"
   cur.execute(insert, values)
   conn.commit()

def insert_sales(values):
    insert = "INSERT INTO sales(pid, quantity, created_at) VALUES (%s, %s,'now()')"
    cur.execute(insert, values)
    conn.commit()

    product_values = ('mango', 50, 20, 80)
    product_values1 = ('banana', 20, 10, 30)
    insert_products(product_values)
    insert_products(product_values1)
    products = fetch_data('products')
    print("Products after inserting mango and banana:\n", products)

    # # print("Fetching data after modified func.\n",products)

    # #insert products-methods2- still takes values as parameter but doesnt use palceholders
    # #insead we repalce placeholders with (values)parameters in a formatted string

    def insert_products_method_two(values):
        insert=f"insert into products(name,buying_price,selling_price)values"
        cur.execute(insert)
        conn.commit()

        product_values=('kuku',600,500,650)
        insert_products_method_two(product_values)
        products=fetch_data('products')
        print('Fetching prods method 2:n",products')
        
#method3-insert data into mnultiple tables with varying number of columns
#insert into <table_name(columns){values}):

def insert_data(table,columns,values):
    cur.execute(f"insert into{table}({columns})values{values}")
    conn.commit()

    table='products'
    columns='name,selling_price,buying_price'
    values=('smartphone2',10000,20000.15000)




    insert_data (table,columns,values)

    products=fetch_data('products')
    print('data from last method:\n, products')
    

    # def profit_per_products():
    #     cur.execute("""select products.name, sum((products.selling price-products.buying price)*quantity) as profit from 
    #                 products join sales on products.id=sales.pid group by(products.name);""")
    #     profit=cur.fetchall()
    #     return profit_per_products
    
    # profit_per_products=profit_per_products()
    # print("profit_, profit_product")


    
def profit_per_product():
    cur.execute("""
        SELECT products.name, 
               SUM((products.selling_price - products.buying_price) * sales.quantity) AS profit 
        FROM products 
        JOIN sales ON products.id = sales.pid 
        GROUP BY products.name;
    """)
    profit_per_product = cur.fetchall()
    return profit_per_product
  
def profit_per_day():
    cur.execute("""
            SELECT DATE(sales.created_at) AS date, 
               SUM((products.selling_price - products.buying_price) * sales.quantity) AS profit 
        FROM products 
        JOIN sales ON products.id = sales.pid 
        GROUP BY DATE(sales.created_at);
    """)
    profit_per_day = cur.fetchall()
    return profit_per_day

def sales_per_product():
    cur.execute("""
        SELECT products.name, 
               SUM(sales.quantity) AS sales 
        FROM products 
        JOIN sales ON products.id = sales.pid 
        GROUP BY products.name;
    """)
    sales_per_product = cur.fetchall()
    return sales_per_product


def sales_per_day():
    cur.execute("""SELECT DATE(sales.created_at) AS date, 
               SUM(sales.quantity) AS sales 
        FROM sales 
        JOIN products ON products.id = sales.pid 
        GROUP BY DATE(sales.created_at);""")
    sales_per_day = cur.fetchall()
    return sales_per_day
    
def check_user():
    query="SELECT * FROM users where email =%s"
    cur.execute(query,(email,))
    user=cur.fetchall()
    return user
    
def add_user(user_details):
    query="INSERT INTO users(name,email,phone_number,password)VALUES(%s,%s,%s,%s)"
    cur.execute(query,user_details)
    conn.commit()
    cur.close()