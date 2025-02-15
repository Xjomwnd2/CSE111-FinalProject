// Import Express module
const express = require('express');
const path = require('path');
const bodyParser = require('body-parser');

// Initialize Express app
const app = express();

// Set up the port (default is 3000)
const PORT = process.env.PORT || 3000;

// Serve static files (like images, stylesheets, and JS)
app.use(express.static(path.join(__dirname, 'assets')));

// Set up a basic route to serve the HTML file
app.get('/', (req, res) => {
  res.sendFile(path.join(__dirname, 'index.html'));
});

// Set up a route to handle the form submission (for contact form or weekly progress)
app.post('/submit-form', (req, res) => {
  // Here you would handle the form data (e.g., save it to a database)
  console.log(req.body); // Print form data to the console
  res.send('Form submitted successfully!');
});
//////////////////////////


// Use body-parser middleware to parse form data
app.use(bodyParser.urlencoded({ extended: true }));
app.use(bodyParser.json());
///////////////////////////////////////////

// Middleware to parse incoming form data
app.use(bodyParser.urlencoded({ extended: true }));
app.use(bodyParser.json());

// Serve static files (like index.html and CSS)
app.use(express.static('public'));

// Handle progress form submission
app.post('/submit-progress', (req, res) => {
  const { date, timeSpent, tasksCompleted } = req.body;

  console.log('Progress Report Submitted:');
  console.log(`Date: ${date}`);
  console.log(`Time Spent: ${timeSpent} hours`);
  console.log(`Tasks Completed: ${tasksCompleted}`);
  
  // Send a response to the client
  res.send('Progress report submitted successfully!');
});
// Handle contact form submission
app.post('/submit-contact', (req, res) => {
  const { name, email, message } = req.body;

  console.log('Contact Form Submitted:');
  console.log(`Name: ${name}`);
  console.log(`Email: ${email}`);
  console.log(`Message: ${message}`);
  
  // Send a response to the client
  res.send('Thank you for reaching out! I will respond soon.');
});
// Start the server
app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});


///////////////////////////////////////////


//////////////