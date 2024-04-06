// JavaScript code for button functionality
document.getElementById("loadButton").addEventListener("click", function() {
    fetchComments();
  });
  
  document.getElementById("sortButton").addEventListener("click", function() {
    sortComments();
  });
  
  function fetchComments() {
    fetch('/comments') // Fetch comments from the server
      .then(response => response.json()) // Parse the JSON response
      .then(data => {
        const commentsList = document.getElementById('commentsList');
        commentsList.innerHTML = ''; // Clear existing comments
        data.comments.forEach(comment => {
          // Create a list item for each comment and append it to the comments list
          const listItem = document.createElement('li');
          listItem.classList.add('comment');
          listItem.textContent = `${comment.user.username}: ${comment.body}`;
          commentsList.appendChild(listItem);
        });
      })
      .catch(error => console.error('Error fetching comments:', error));
  }
  
  function sortComments() {
    const commentsList = document.getElementById('commentsList');
    const comments = Array.from(commentsList.children);
    comments.sort((a, b) => {
      const usernameA = a.textContent.split(":")[0];
      const usernameB = b.textContent.split(":")[0];
      return usernameA.localeCompare(usernameB);
    });
    comments.forEach(comment => commentsList.appendChild(comment));
  }
  