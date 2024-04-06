const http = require('http');
const fs = require('fs');
const fetch = require('node-fetch');

const server = http.createServer((req, res) => {
  if (req.url === '/') {
    // Serve the HTML file
    fs.readFile('index.html', 'utf8', (err, data) => {
      if (err) {
        res.writeHead(500);
        return res.end('Error loading index.html');
      }
      res.writeHead(200, {'Content-Type': 'text/html'});
      res.end(data);
    });
  } else if (req.url === '/comments') {
    // Fetch comments from the API endpoint
    fetch("https://dummyjson.com/comments")
      .then(response => response.json())
      .then(data => {
        const comments = data.comments.slice(0, 10);
        res.writeHead(200, {'Content-Type': 'application/json'});
        res.end(JSON.stringify(comments));
      })
      .catch(error => {
        console.error("Error fetching comments:", error);
        res.writeHead(500);
        res.end('Error fetching comments');
      });
  } else {
    res.writeHead(404);
    res.end('Not Found');
  }
});

const PORT = process.env.PORT || 3000;
server.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});
