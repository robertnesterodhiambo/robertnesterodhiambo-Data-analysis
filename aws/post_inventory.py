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

# API endpoint to add a new tire to inventory
@app.route('/api/inventory', methods=['POST'])
def add_tire():
    data = request.get_json()
    brand = data['brand']
    model = data['model']
    loadrating = data['loadrating']
    speedrating = data['speedrating']
    tire_type = data['type']  # Changed variable name from 'type' to 'tire_type'
    stock = data['stock']
    cursor = connection.cursor()
    cursor.execute("INSERT INTO inventory (brand, model, loadrating, speedrating, type, stock) VALUES (%s, %s, %s, %s, %s, %s)",
                   (brand, model, loadrating, speedrating, tire_type, stock))  # Changed variable name from 'type' to 'tire_type'
    connection.commit()
    cursor.close()
    return jsonify({'message': 'Tire added to inventory'})

if __name__ == '__main__':
    app.run(debug=True)
else:
    print("Flask app is imported as a module.")
