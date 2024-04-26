from flask import Flask, request, jsonify, render_template
import mysql.connector

app = Flask(__name__)

# Database connection
connection = mysql.connector.connect(
    host="falode3368-1.ch6kyu62mcnp.us-east-1.rds.amazonaws.com",
    user="Falode",
    password="1QAZ2wsx",
    database="cis3368DB"
)
cursor = connection.cursor()

# Function to assign teacher to classroom
def assign_teacher_to_classroom(teacher_id, classroom_id):
    # Check the number of children already assigned to the classroom
    cursor.execute("SELECT COUNT(*) FROM child WHERE classroom_id = %s", (classroom_id,))
    num_children = cursor.fetchone()[0]

    # Check the number of teachers assigned to the classroom
    cursor.execute("SELECT COUNT(*) FROM teacher WHERE classroom_id = %s", (classroom_id,))
    num_teachers = cursor.fetchone()[0]

    # Calculate the adjusted capacity based on the number of teachers
    adjusted_capacity = 20 - num_teachers * 10

    # Check if the teacher assignment exceeds the adjusted capacity
    if num_children >= adjusted_capacity:
        return False

    # If capacity allows, assign the teacher to the classroom
    cursor.execute("UPDATE teacher SET classroom_id = %s WHERE id = %s", (classroom_id, teacher_id))
    connection.commit()
    return True

# Function to assign child to classroom
def assign_child_to_classroom(child_id, classroom_id):
    # Check the number of teachers assigned to the classroom
    cursor.execute("SELECT COUNT(*) FROM teacher WHERE classroom_id = %s", (classroom_id,))
    num_teachers = cursor.fetchone()[0]

    # Check if there are teachers assigned to the classroom
    if num_teachers == 0:
        return False

    # Check the number of children already assigned to the classroom
    cursor.execute("SELECT COUNT(*) FROM child WHERE classroom_id = %s", (classroom_id,))
    num_children = cursor.fetchone()[0]

    # Calculate the adjusted capacity based on the number of teachers
    adjusted_capacity = 20 - num_teachers * 10

    # Check if the child assignment exceeds the adjusted capacity
    if num_children >= adjusted_capacity:
        return False

    # If capacity allows, assign the child to the classroom
    cursor.execute("UPDATE child SET classroom_id = %s WHERE id = %s", (classroom_id, child_id))
    connection.commit()
    return True

# Route to serve index.html when accessing the root URL
@app.route('/')
def index():
    return render_template('index.html')

# Route to add a new teacher
@app.route('/teacher', methods=['POST'])
def add_teacher():
    data = request.json
    firstname = data['firstname']
    lastname = data['lastname']
    classroom_id = data['classroom_id']

    cursor.execute("INSERT INTO teacher (firstname, lastname, classroom_id) VALUES (%s, %s, %s)", (firstname, lastname, classroom_id))
    connection.commit()
    return jsonify({'message': 'Teacher added successfully'})

# Route to add a new child
@app.route('/child', methods=['POST'])
def add_child():
    data = request.json
    firstname = data['firstname']
    lastname = data['lastname']
    age = data['age']
    classroom_id = data['classroom_id']

    cursor.execute("INSERT INTO child (firstname, lastname, age, classroom_id) VALUES (%s, %s, %s, %s)", (firstname, lastname, age, classroom_id))
    connection.commit()
    return jsonify({'message': 'Child added successfully'})

# Route to assign teacher to classroom
@app.route('/assign_teacher', methods=['POST'])
def assign_teacher():
    data = request.json
    teacher_id = data['teacher_id']
    classroom_id = data['classroom_id']

    if assign_teacher_to_classroom(teacher_id, classroom_id):
        return jsonify({'message': 'Teacher assigned to classroom successfully'})
    else:
        return jsonify({'error': 'Teacher assignment failed. Classroom capacity exceeded'})

# Route to assign child to classroom
@app.route('/assign_child', methods=['POST'])
def assign_child():
    data = request.json
    child_id = data['child_id']
    classroom_id = data['classroom_id']

    if assign_child_to_classroom(child_id, classroom_id):
        return jsonify({'message': 'Child assigned to classroom successfully'})
    else:
        return jsonify({'error': 'Child assignment failed. No teachers assigned to the classroom'})

if __name__ == '__main__':
    app.run(debug=True)
