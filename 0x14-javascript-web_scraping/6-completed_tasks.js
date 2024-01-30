#!/usr/bin/node

const request = require('request');

const url = process.argv[2];

request(url, function (err, response, body) {
  if (!err) {
    const completedTasksPerUser = {};
    const tasks = JSON.parse(body);
    for (const task of tasks) {
      if (task.completed === true) {
        completedTasksPerUser[task.userId] = (completedTasksPerUser[task.userId] || 0) + 1;
      }
    }

    console.log(completedTasksPerUser);
  }
});
