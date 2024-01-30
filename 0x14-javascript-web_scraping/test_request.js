#!/usr/bin/node

// Import the 'request' library
const request = require('request');

// Specify the URL you want to make a request to (example.com in this case)
const url = 'http://www.example.com';

// Make a simple GET request to example.com
request(url, (error, response, body) => {
    if (!error && response.statusCode === 200) {
        // Print the HTML content of the page
        console.log(body);
    } else {
        // Print an error message if something went wrong
        console.error('Error:', error);
    }
});

