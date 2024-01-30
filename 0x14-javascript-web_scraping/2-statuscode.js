#!/usr/bin/node

const request = require('request');

const url = process.argv[2];

request(url, (err, res, body) => {
  if (res) {
    console.log('code: ' + res.statusCode);
  } else {
    console.error(err);
  }
});
