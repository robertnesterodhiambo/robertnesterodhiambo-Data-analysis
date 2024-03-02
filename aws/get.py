from flask import Flask, request, jsonify
import mysql.connector

# AWS RDS MySQL connection configuration
config = {
    'host': 'falode3368-1.ch6kyu62mcnp.us-east-1.rds.amazonaws.com',
    'user': 'Falode',
    'password': '1QAZ2wsx',
    'database': 'cis3368DB'
}

app = Flask(__name__)
connection = mysql.connector.connect(**config)

@app.route('/api/calculate', methods=['GET'])
def calculate_total():
    try:
        # Get the code and amount from request headers
        code = request.headers.get('code')
        amount = request.headers.get('amount')

        # Check if the code exists in the database
        cursor = connection.cursor()
        cursor.execute("SELECT discount FROM coupon WHERE code = %s", (code,))
        coupon = cursor.fetchone()

        if not coupon:
            return jsonify({'error': 'Code does not exist in the database.'}), 404

        # Calculate the total price after discount
        discount = coupon[0]
        total_price = float(amount) * (1 - discount / 100)

        return jsonify({'total_price': total_price}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    finally:
        cursor.close()

if __name__ == '__main__':
    app.run(debug=True)
