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

# API endpoint to update the stock of a tire
@app.route('/api/inventory/<int:tire_id>', methods=['PUT'])
def update_stock(tire_id):
    data = request.get_json()
    new_stock = data['stock']
    cursor = connection.cursor()
    cursor.execute("UPDATE inventory SET stock = %s WHERE id = %s", (new_stock, tire_id))
    connection.commit()
    cursor.close()
    return jsonify({'message': 'Stock updated'})

if __name__ == '__main__':
    app.run(debug=True)
