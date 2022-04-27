

from unittest import mock
from flask import Flask 
import json
from mock_data import mock_catalog

app = Flask('server')

@app.route("/home")
def home():
    return "Hello there!!"

#####################################################################
########################## API CATALOG ##############################
#####################################################################


@app.route("/api/about", methods=["POST"])
def about():
    me = {
        "first": "Gibrahn",
        "last": "Duarte"
    }

    return json.dumps(me) # parse into json, then return


@app.route("/api/catalog")
def get_catalog():
    return json.dumps(mock_catalog)


@app.route("/api/catalog/cheapest")
def get_cheapest():
    cheapest = mock_catalog[0]

    for prod in mock_catalog:
        if (prod["price"] < cheapest["price"]):
            cheapest = prod 
    return json.dumps(cheapest)

@app.route("/api/catalog/total")
def get_total():
    total = 0

    for prod in mock_catalog:
        total += prod["price"]

    return json.dumps(total) 

@app.route("/api/products/<id>")
def find_product(id):
    for prod in mock_catalog:
        if  prod["_id"] == id:
            
            return json.dumps(prod)

@app.route("/api/products/categories")
def get_categories():
    categories = []

    for prod in mock_catalog:
        cat = prod["category"]
        if not cat in categories:
            categories.append(cat)

    return json.dumps(categories)

@app.route("/api/products/categories/<cat_name>")
def get_by_category(cat_name):
    results = []

    for prod in mock_catalog:
        if  prod["category"].lower() == cat_name.lower():
            results.append(prod)
    return json.dumps(results)

@app.route("/api/products/search/<text>")
def search_by_text(text):
    results = []
    text = text.lower()

    for prod in mock_catalog:
        title = prod["title"].lower()
        if text in title:
            results.append(prod)

    return json.dumps(results)

#start the server
app.run(debug=True)