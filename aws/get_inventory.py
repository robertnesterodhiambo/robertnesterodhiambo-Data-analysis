from flask import Flask, jsonify
import mysql.connector

app = Flask(__name__)

# Establish a connection to your MySQL database
connection = mysql.connector.connect(
    host="falode3368-1.ch6kyu62mcnp.us-east-1.rds.amazonaws.com",
    user="Falode",
    password="1QAZ2wsx",
    database="cis3368DB"
)

# GET /api/inventory
@app.route('/api/inventory', methods=['GET'])
def get_inventory():
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM inventory")
    inventory = cursor.fetchall()
    cursor.close()
    return jsonify(inventory)

if __name__ == '__main__':
    app.run(debug=True, port=5001)  # Run the app on port 5001
