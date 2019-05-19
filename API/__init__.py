from flask import Flask, g
from flask_restful import Resource, Api, reqparse
import markdown
import os
import shelve

app = Flask(__name__)
api = Api(app)

# Creating and Defining the persistent object form shevle 
def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = shelve.open('bikes.db')
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

# Documentation instructional page at index route
@app.route('/')
def index():
    # Present some documentation & open README file
    with open(os.path.dirname(app.root_path) + '/README.md', 'r') as markdown_file:
        content = markdown_file.read()

    return markdown.markdown(content)
 
# """ Below here are the endpoints defined with Flask-RESTful """

# GET Bike list 
class BikeList(Resource): 
    def get(self): 
        shelf = get_db()
        keys = list(shelf.keys())
    
        bikes = []

        for key in keys: 
            bikes.append(shelf[key])
    
        return {"message": "OK", "data": bikes}, 200 

class Bike(Resource): 
    def get(self, name): 
        shelf = get_db()

        # if name identifier doesnt exist
        if not (name in shelf): 
            return {"message": "Bike not found", "data": {}}, 404

        return {"message": "bike found", "data": shelf[name]}, 200

    def post(self,name): 
        parser = reqparse.RequestParser()

        parser.add_argument("identifier", required = True)
        parser.add_argument("brand", required = True)
        parser.add_argument("name", required = True)
        parser.add_argument("price", required = True)
        parser.add_argument("image", required = True)

        args = parser.parse_args()

        shelf = get_db()
        shelf[args["name"]] = args

        return {"message": "Bike created", "data": args}, 201

    def delete(self, name):
        shelf = get_db()

        # if name identifier doesnt exist
        if not (name in shelf): 
            return {"message": "Bike not found", "data": {}}, 404

        del shelf[name]
        return {"message": "Successfully deleted bike"}, 204

api.add_resource(BikeList, '/bikes')
api.add_resource(Bike, '/bikes/<name>')