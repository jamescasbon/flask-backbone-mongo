import pymongo
from bson.objectid import ObjectId
import json_util
from flask import Flask, render_template, url_for, jsonify, json, request

app = Flask(__name__)
connection = pymongo.Connection('localhost', 27017)
todos = connection['demo']['todos']

def json_load(data):
    return json.loads(data, object_hook=json_util.object_hook)

def json_dump(data):
    return json.dumps(data, default=json_util.default)

@app.route('/')
def hello_world():
    return render_template('index.html')

# the collection api expects a raw list of objects, so we cannot use flask.jsonify 
@app.route('/todos')
def list_todos():
    print json_dump(list(todos.find()))
    return json_dump(list(todos.find()))
    
@app.route('/todos',  methods=['POST'])
def new_todo():
    todo = json_load(request.data)
    todos.save(todo)
    return json_dump(todo)

@app.route('/todos/<todo_id>', methods=['PUT'])
def update_todo(todo_id):
    todo = json_load(request.data)
    todos.save(todo)
    return json_dump(todo)

@app.route('/todos/<todo_id>', methods=['DELETE'])
def delete_todo(todo_id):
    print 'id was', todo_id
    todos.remove(ObjectId(todo_id))
    return ""


if __name__ == '__main__':
    app.run(debug=True)



