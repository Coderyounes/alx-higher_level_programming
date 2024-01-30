#!/usr/bin/node

const request = require('request');

const URL = process.argv[2];
const ID = 18;

request(URL, (err, res, body) => {
  let count = 0;
  if (!err) {
    const jsonData = JSON.parse(body);
    for (let i = 0; i < jsonData.results.length; i++) {
      const content = jsonData.results[i].characters;
      for (let j = 0; j < content.length; j++) {
        const char = jsonData.results[i].characters;
        const parts = char[j].split('/');
        const elementid = parts[parts.length - 2];
        const userId = String(ID);
        if (elementid === userId) {
          count++;
        }
      }
    }
    console.log(count);
  } else {
    console.error(err);
  }
});
