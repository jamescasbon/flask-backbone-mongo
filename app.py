from flask import Flask, render_template, url_for, jsonify, json, request
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')

# the collection api expects a raw list of objects, so we cannot use flask.jsonify 
@app.route('/todos')
def list_todos():
    return json.dumps(todos.values())
    
@app.route('/todos',  methods=['POST'])
def new_todo():
    todo = request.json
    todo['id'] = max(todos.keys()) + 1
    todos[todo['id']] = todo
    return json.dumps(todo)

@app.route('/todos/<int:todo_id>', methods=['PUT'])
def put_todo(todo_id):
    todo = request.json
    todos[todo['id']] = todo
    return json.dumps(todo)

@app.route('/todos/<int:todo_id>', methods=['DELETE'])
def delete_todo(todo_id):
    todos.pop(todo_id)
    return ""

todos = {
    1: {'content': 'oh hai', 'done': False, 'id': 1, 'order': None},
    2: {'content': 'can haz', 'done': False, 'id': 2, 'order': None}
}



if __name__ == '__main__':
    app.run(debug=True)



