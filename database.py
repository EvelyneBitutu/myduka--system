import psycopg2
from datetime import datetime


# Create a connection to the database
conn = psycopg2.connect(user="postgres", password="bitutu", host="localhost", port="5432", database="myduka")

# Execute database operations
cur = conn.cursor()
now=datetime.now()


# Query to fetch products
def fetch_products():
    cur.execute("SELECT * FROM products")
    products = cur.fetchall()
    for product in products:
        print(product)

# Query to fetch sales
def fetch_sales():
    cur.execute("SELECT * FROM sales")
    sales = cur.fetchall()
    for sale in sales:
        print(sale)

# Call the functions

# fetch_sales()


def insert_products():
    cur.execute("insert into  products(name,buying_price,selling_price)values('mindaza',100,150)")
    conn.commit()


# conn.commit()
# fetch_products()

def insert_sales():
    cur.execute(f"insert into sales(id,pid,quantity,created_at)values(80,3,4,'{now}')")
    conn.commit()

insert_products()
insert_sales()

fetch_products()
fetch_sales()





