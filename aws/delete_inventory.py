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

# DELETE /api/inventory/<int:id>
@app.route('/api/inventory/<int:id>', methods=['DELETE'])
def delete_tire(id):
    cursor = connection.cursor(dictionary=True)
    query = "DELETE FROM inventory WHERE id = %s"
    cursor.execute(query, (id,))
    connection.commit()
    affected_rows = cursor.rowcount
    cursor.close()
    if affected_rows > 0:
        return jsonify({"message": "Tire deleted"}), 200
    else:
        return jsonify({"error": "Tire not found"}), 404

if __name__ == '__main__':
    app.run(debug=True, port=5004)  # Run the app on port 5004
