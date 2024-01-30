#!/usr/bin/node

const request = require('request');

const ID = process.argv[2];
const URL = 'https://swapi-api.alx-tools.com/api/films/' + ID;

request(URL, (err, res, body) => {
  if (!err) {
    console.log(JSON.parse(body).title);
  } else {
    console.error(err);
  }
});
