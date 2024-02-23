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

# PUT /api/inventory/<int:id>
@app.route('/api/inventory/<int:id>', methods=['PUT'])
def update_stock(id):
    data = request.json
    cursor = connection.cursor(dictionary=True)
    query = "UPDATE inventory SET stock = %s WHERE id = %s"
    cursor.execute(query, (data['stock'], id))
    connection.commit()
    affected_rows = cursor.rowcount
    cursor.close()
    if affected_rows > 0:
        return jsonify({"message": "Stock updated"}), 200
    else:
        return jsonify({"error": "Tire not found"}), 404

if __name__ == '__main__':
    app.run(debug=True, port=5003)  # Run the app on port 5003
