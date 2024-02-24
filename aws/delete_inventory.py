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

# API endpoint to delete a tire from inventory
@app.route('/api/inventory/<int:tire_id>', methods=['DELETE'])
def delete_tire(tire_id):
    cursor = connection.cursor()
    cursor.execute("DELETE FROM inventory WHERE id = %s", (tire_id,))
    connection.commit()
    cursor.close()
    return jsonify({'message': 'Tire deleted from inventory'})

if __name__ == '__main__':
    app.run(debug=True)
