# Readme.made#import flask to use it
# from flask import Flask

# #intantiate your application-initializion fo Flask
# #flask instance
# app=Flask(__name__)

# #__name__  - special built variable
# #represents the name of your current file where your application is built.
# #tells Flask where your project starts

# @app.route('/products') #function 1
# def home():function 2
#     return "My Home Page"

# #running your application
# app.run()



# div>
#         {% for number in numbers  %}
#         <p>Hello,{{data}}</p>
#         Hello world!
#         {% else %}
#         <p>Data not provided</p>
#         {% endif %}


# from flask import Flask, render_template

# #instantiating
# app=Flask(__name__)

# #dictonary
# @app.route('/') 
# def home():
#     user={"name":"Evelyne","location":"Nairobi"}
#     return render_template("index.html",data=user)


#  {% if data  %}
#         <p>Hello,{{data}}</p>
#         Hello world!
#         {% else  %}
#         <p>Data not provided</p>
#         {%end
#             if%}


# @app.route('/')
# def home():
#     numbers=[1,2,3,4]
#     return render_template ("index.html", numbers=numbers)

#   {% for number in numbers %}
#         <li>{{number}}</li>
#         {% endfor %}
#     </div>

    
# @app.route('/email')
# def email():
# #     return "show Email Page"

# @app.route('/products')
# def products():
#     return render_template("products.html")


# #run your app
# app.run()


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



new Chart(document.getElementById("line-chart"), {
  type: 'line',
  data: {
     label: "Africa",
        borderColor: "#3e95cd",
        fill: false
      }, { 
        data: [282,350,411,502,635,809,947,1402,3700,5267],
        label: "Asia",
        borderColor: "#8e5ea2",
        fill: false
    
      }
    ]
  },
  options: {
    title: {
      display: true,
      text: 'World population per region (in millions)'
    }
  }
});    labels: [1500,1600,1700,1750,1800,1850,1900,1950,1999,2050],
    datasets: [{ 
        data: [86,114,106,106,107,111,133,221,783,2478],



 <form action="/register" method="post">
            <div class="mb-3 ">
            <label class="form-label" for="full_name">Full name</label>
            <input class="form-control" class="form-label" type="text" name="full_name",>
            </div>
            <div class="mb-3">
                <label for="exampleInputEmail1" class="form-label">Email address</label>
                <input name="email" type="email" class="form-control" id="exampleInputEmail1" 
aria-describedby="emailHelp">
            </div>
            <div class="mb-3">
                <label for="exampleInputPassword1" class="form-label">Password</label>
                <input type="password" class="form-control" id="exampleInputPassword1" 
name="password">
            </div>  
            <button type="submit" class="btn btn-primary">Submit</button>
        </form>

   
 <!-- <p> {{date}} </p>
      <p> {{p_day}} </p>
      <p> {{s_day}} </p> -->
    
    
    new Chart(document.getElementById("line-chart"), {
    type: 'line',
    data: {
    
      labels: {{ date | safe }},

      datasets: [
        {
          data: {{ p_day | safe }}, 
          label: "Profit per Day",
          borderColor: "#3e95cd",
          fill: false
        },
        {
         
          data: {{ s_day | safe }}, 
          label: "Sales per Day",
          borderColor: "#8e5ea2",
          fill: false
        }
      ]
    },
    options: {
      title: {
        display: true,
        text: 'Sales and Profit Per Day'
      },
     }
  });