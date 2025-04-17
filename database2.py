import psycopg2
#create a connection to the database
conn = psycopg2.connect(user="postgres",password="bitutu",host="localhost",port="5432",database="myduka")


#execute database operations
cur = conn.cursor()
#query
def fetch_products():
    cur.execute("select * from products")
    products =cur.fetchall()
    for product in products:
        print(product)

    #fetch sales
def fetch_sales():
    cur.execute("select * from sales")
    sales = cur.fetchall()
    for sale in sales:
        print(sale)  

fetch_products
fetch_sales   


# sample_list[1,2,3,3]

# for i in sample_list:
#     print(i)
#     products= cur.fetchall