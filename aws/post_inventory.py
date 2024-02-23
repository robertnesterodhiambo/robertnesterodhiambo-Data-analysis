from flask import Flask, jsonify, request
import mysql.connector

app = Flask(__name__)

# Establish a connection to your MySQL database
connection = mysql.connector.connect(
    host="falode3368-1.ch6kyu62mcnp.us-east-1.rds.amazonaws.com",
    user="Falode",
    password="1QAZ2wsx",
    database="cis3368DB"
)

# POST /api/inventory
@app.route('/api/inventory', methods=['POST'])
def add_tire():
    data = request.json
    cursor = connection.cursor(dictionary=True)
    query = "INSERT INTO inventory (brand, model, loadrating, speedrating, type, stock) VALUES (%s, %s, %s, %s, %s, %s)"
    cursor.execute(query, (data['brand'], data['model'], data['loadrating'], data['speedrating'], data['type'], data['stock']))
    connection.commit()
    new_tire_id = cursor.lastrowid
    cursor.close()
    return jsonify({"id": new_tire_id}), 201

if __name__ == '__main__':
    app.run(debug=True, port=5002)  # Run the app on port 5002
