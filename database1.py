import psycopg2

def connect_to_db():
    """Establish a connection to the database."""
    return psycopg2.connect(user="postgres", password="bitutu", host="localhost", port="5432", database="myduka")

def fetch_data(query):
    """Fetch data from the database based on the provided query."""
    # conn = connect_to_db()
    # cur = conn.cursor()
    # cur.execute(query)
    # data = cur.fetchall()
    # cur.close()
    # conn.close()
    # return data

def fetch_products():
    """Main function to fetch and display products and sales."""
    # # Fetch and display products
    # print("Products:")
    products = fetch_data("SELECT * FROM products")
    for product in products:
        print(product)

    # Fetch and display sales
def fetch_sales():
    sales = fetch_data("SELECT * FROM sales")
    for sale in sales:
        print(sale)

fetch_products
fetch_sales 

# if __name__ == "__main__":
#     main()