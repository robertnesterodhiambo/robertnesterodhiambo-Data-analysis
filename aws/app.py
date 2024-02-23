from flask import Flask
import mysql.connector

app = Flask(__name__)

# Establish a connection to your MySQL database
connection = mysql.connector.connect(
    host="falode3368-1.ch6kyu62mcnp.us-east-1.rds.amazonaws.com",
    user="Falode",
    password="1QAZ2wsx",
    database="cis3368DB"
)

# Register blueprints
from get_inventory import get_inventory
from post_inventory import post_inventory
from put_inventory import put_inventory
from delete_inventory import delete_inventory

app.register_blueprint(get_inventory)
app.register_blueprint(post_inventory)
app.register_blueprint(put_inventory)
app.register_blueprint(delete_inventory)

if __name__ == '__main__':
    app.run(debug=True)
