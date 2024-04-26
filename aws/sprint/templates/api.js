// Import necessary modules
const mysql = require('mysql');
const express = require('express');
const path = require('path');

// Create an Express application
const app = express();

// Middleware to parse JSON request bodies
app.use(express.json());

// Serve the index.html file for all routes except '/add-teacher'
app.get('*', (req, res, next) => {
  if (req.url !== '/add-teacher') {
    res.sendFile(path.join(__dirname, 'index.html'));
  } else {
    next();
  }
});

// Serve the add_teacher.html file for '/add-teacher' route
app.get('/add-teacher', (req, res) => {
  res.sendFile(path.join(__dirname, 'add_teacher.html'));
});

// Create a MySQL connection pool
const pool = mysql.createPool({
  connectionLimit: 10,
  host: 'falode3368-1.ch6kyu62mcnp.us-east-1.rds.amazonaws.com',
  user: 'Falode',
  password: '1QAZ2wsx',
  database: 'cis3368DB'
});

// Route to handle login and fetch data
app.post('/login', (req, res) => {
  const username = req.body.username;
  const password = req.body.password;

  // Check if username and password match
  if (username === 'admin' && password === '123') {
    // Fetch data from tables
    pool.getConnection((err, connection) => {
      if (err) {
        res.status(500).json({ error: 'Internal Server Error' });
        return;
      }
      connection.query('SELECT * FROM facility', (err, facilityRows) => {
        if (err) {
          connection.release();
          res.status(500).json({ error: 'Internal Server Error' });
          return;
        }
        connection.query('SELECT * FROM classroom', (err, classroomRows) => {
          if (err) {
            connection.release();
            res.status(500).json({ error: 'Internal Server Error' });
            return;
          }
          connection.query('SELECT * FROM teacher', (err, teacherRows) => {
            if (err) {
              connection.release();
              res.status(500).json({ error: 'Internal Server Error' });
              return;
            }
            connection.query('SELECT * FROM child', (err, childRows) => {
              connection.release();
              if (err) {
                res.status(500).json({ error: 'Internal Server Error' });
                return;
              }
              // Send the fetched data as JSON response
              res.json({
                facility: facilityRows,
                classroom: classroomRows,
                teacher: teacherRows,
                child: childRows
              });
            });
          });
        });
      });
    });
  } else {
    res.status(401).json({ error: 'Unauthorized' });
  }
});

// Route to add a new teacher
app.post('/add-teacher', (req, res) => {
  const { name, email } = req.body;
  pool.query('INSERT INTO teacher (name, email) VALUES (?, ?)', [name, email], (error, results, fields) => {
    if (error) {
      console.error('Error adding teacher:', error);
      res.status(500).json({ error: 'Internal Server Error' });
      return;
    }
    res.status(200).json({ message: 'Teacher added successfully' });
  });
});

// Start the server
const port = process.env.PORT || 3000;
app.listen(port, () => {
  console.log(`Server is running on port ${port}`);
});
