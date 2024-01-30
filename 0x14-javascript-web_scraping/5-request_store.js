#!/usr/bin/node

const request = require('request');
const fs = require('fs');

const URL = process.argv[2];
const filename = process.argv[3];
let content = null;

request(URL, (err, res, body) => {
  if (!err) {
    content = body;
    fs.writeFile(filename, content, 'utf8', (err) => {
      if (err) {
        console.error(err);
      }
    });
  } else {
    console.error(err);
  }
});
