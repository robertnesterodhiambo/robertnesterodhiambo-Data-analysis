from flask import Flask, request, jsonify
import mysql.connector

app = Flask(__name__)

# Establish a connection to the MySQL database
connection = mysql.connector.connect(
    host="falode3368-1.ch6kyu62mcnp.us-east-1.rds.amazonaws.com",
    user="Falode",
    password="1QAZ2wsx",
    database="cis3368DB"
)

# Function to execute SQL queries
def execute_query(query, data=None, commit=False):
    cursor = connection.cursor(dictionary=True)
    if data:
        cursor.execute(query, data)
    else:
        cursor.execute(query)
    if commit:
        connection.commit()
    if query.strip().lower().startswith('select'):
        result = cursor.fetchall()
    else:
        result = {"message": "Operation successful"}
    cursor.close()
    return result

# CRUD endpoints for Facility table
@app.route('/facility', methods=['GET'])
def get_all_facilities():
    query = "SELECT * FROM Facility"
    return jsonify(execute_query(query))

@app.route('/facility/<int:id>', methods=['GET'])
def get_facility(id):
    query = "SELECT * FROM Facility WHERE id = %s"
    return jsonify(execute_query(query, (id,)))

@app.route('/facility', methods=['POST'])
def add_facility():
    data = request.json
    query = "INSERT INTO Facility (name) VALUES (%s)"
    return jsonify(execute_query(query, (data['name'],), commit=True))

@app.route('/facility/<int:id>', methods=['PUT'])
def update_facility(id):
    data = request.json
    query = "UPDATE Facility SET name = %s WHERE id = %s"
    return jsonify(execute_query(query, (data['name'], id), commit=True))

@app.route('/facility/<int:id>', methods=['DELETE'])
def delete_facility(id):
    query = "DELETE FROM Facility WHERE id = %s"
    return jsonify(execute_query(query, (id,), commit=True))

# Add similar CRUD endpoints for Classroom, Teacher, and Child tables...

if __name__ == '__main__':
    app.run(debug=True)
