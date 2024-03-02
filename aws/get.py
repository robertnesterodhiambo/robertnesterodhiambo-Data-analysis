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

@app.route('/api/coupon', methods=['POST'])
def add_coupon():
    try:
        # Parse JSON payload from request body
        data = request.json
        code = data.get('code')
        discount = data.get('discount')

        # Check if a coupon with the same discount percentage already exists
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM coupon WHERE discount = %s", (discount,))
        existing_coupon = cursor.fetchone()

        if existing_coupon:
            return jsonify({'message': 'Coupon with the same discount percentage already exists.'}), 409

        # Insert the new coupon record
        cursor.execute("INSERT INTO coupon (code, discount) VALUES (%s, %s)", (code, discount))
        connection.commit()

        return jsonify({'message': 'Coupon added successfully.'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    finally:
        cursor.close()

@app.route('/api/coupon', methods=['GET'])
def get_coupons():
    try:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM coupon")
        records = cursor.fetchall()
        coupons = [{'id': record[0], 'code': record[1], 'discount': float(record[2])} for record in records]
        return jsonify(coupons)
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    finally:
        cursor.close()

if __name__ == '__main__':
    app.run(debug=True)
