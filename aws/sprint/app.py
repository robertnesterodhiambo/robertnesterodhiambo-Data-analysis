from flask import Flask, request, jsonify

app = Flask(__name__)

# Pre-configured username and password
username = "admin"
password = "password"

# Login endpoint
@app.route('/login', methods=['POST'])
def login():
    auth = request.authorization
    if not auth or not auth.username or not auth.password:
        return jsonify({"message": "Authentication required"}), 401

    if auth.username == username and auth.password == password:
        return jsonify({"message": "Login successful"}), 200
    else:
        return jsonify({"message": "Invalid username or password"}), 401

# Generic CRUD endpoints for all tables

# GET all rows from a table
@app.route('/<table>', methods=['GET'])
def get_all(table):
    # Add your code to retrieve data from the database table
    return jsonify({"message": "Get all records from table: " + table})

# GET a specific row by ID from a table
@app.route('/<table>/<int:id>', methods=['GET'])
def get_by_id(table, id):
    # Add your code to retrieve data from the database table
    return jsonify({"message": "Get record with ID {} from table: {}".format(id, table)})

# POST a new row to a table
@app.route('/<table>', methods=['POST'])
def add_row(table):
    # Add your code to insert data into the database table
    return jsonify({"message": "Add new record to table: " + table})

# PUT (update) a row in a table
@app.route('/<table>/<int:id>', methods=['PUT'])
def update_row(table, id):
    # Add your code to update data in the database table
    return jsonify({"message": "Update record with ID {} in table: {}".format(id, table)})

# DELETE a row from a table
@app.route('/<table>/<int:id>', methods=['DELETE'])
def delete_row(table, id):
    # Add your code to delete data from the database table
    return jsonify({"message": "Delete record with ID {} from table: {}".format(id, table)})

if __name__ == '__main__':
    app.run(debug=True)
