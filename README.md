# Quick Intro

Playing around with `docker` and `python eve`.

Simple `eve api` to serve data and `flask server` which simply transforms api data into html representations.

Also includes:

- website route decorators to retrieve data
- website decorator to handle errors from api

Entire website route as simple as:

	@app.route('/offers/')
	@get_api_data('http://192.168.99.100:5000/offers/')
	@handle_api_errors()
	def offers(data):
	    return render_template('offers.html', data=data)

# Setup

If it works for you install the `docker toolbox`. If not install `docker`, `docker-machine` and `docker-compose`.

# Running the project

As simple as runnint the following from the project root directory:

    docker-compose up

which should create 3 containers called (or something similar):

* `snapcyle_mongo_1`
* `snapcyle_data_api_1`
* `snapcyle_website_1`

We have to create a user on mongodb before we can go any further.

First copy `db-setup.js`

    docker cp ./DataApi/db-setup.js snapcycle_mongo_1:/tmp

Then run it against mongo:

    docker exec snapcycle_mongo_1 mongo /tmp/db-setup.js

Then create some data with:

    curl -XPOST http://$(docker-machine ip dev):5000/offers/ -d '{"title": "Something I want to give away", "description": "A little something about it" }' -H 'Content-Type: application/json'
    
    curl -XPOST http://$(docker-machine ip dev):5000/offers/ -d '{"title": "Something else that I want to give away", "description": "A little something more about this other thing" }' -H 'Content-Type: application/json'
    
Note that my docker machine is called dev and might need changing depending on your setup.

# Viewing the api and site

Get the ip of your docker-machine with:

    docker-machine ip dev
    >> 192.168.99.100
    
Then visit the data api at;

    http://192.168.99.100:5000/offers

Or the website at:

    http://192.168.99.100:8080/offers