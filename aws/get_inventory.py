from flask import Flask, jsonify
import mysql.connector

app = Flask(__name__)

# Establish a connection to the MySQL database
connection = mysql.connector.connect(
    host="falode3368-1.ch6kyu62mcnp.us-east-1.rds.amazonaws.com",
    user="Falode",
    password="1QAZ2wsx",
    database="cis3368DB"
)

# API endpoint to retrieve all tires from inventory
@app.route('/api/inventory', methods=['GET'])
def get_all_tires():
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM inventory")
    tires = cursor.fetchall()
    cursor.close()
    return jsonify(tires)

if __name__ == '__main__':
    app.run(debug=True)
