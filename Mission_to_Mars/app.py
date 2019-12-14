from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars

import sys

app = Flask(__name__)

# Establish mongo database for mars data
mongo = PyMongo(app, uri= "mongodb://localhost:27017/mars_database")

print('Mongo connection established')

@app.route('/')
def index():

    mars_data = mongo.db.collection.find_one()

    return render_template("index.html", mars = mars_data)

    # Prints to screen
    print('Home Page', file=sys.stdout)

@app.route('/scrape')
def scrape():

    # Runs scrape function
    scarped_mars = scrape_mars.scrape()

    #Prints to screen
    print('Run scrape function', file=sys.stdout)

    # Updates database
    mongo.db.collection.update({}, scraped_mars_data, upsert=True)

    # Prints to screen
    print('Update mongo database', file=sys.stdout)

    # Redirects to home screen
    return redirect('\')

    # Prints to screen
    print("Redirect to index", file=sys.stdout)

if __name__ == "__main__":
    app.run(debug=True)
