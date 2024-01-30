#!/usr/bin/node
const request = require('request');

// Specifying the file path
const url = process.argv[2];
// const todos = https://jsonplaceholder.typicode.com/todos';

const completedTasks = {};
// getting requests
request(url, (err, _response, tasks) => {
  if (err) {
    console.log(err);
  } else {
    tasks = JSON.parse(tasks);

    for (let i = 0; i < tasks.length; ++i) {
      const userId = tasks[i].userId;
      const completed = tasks[i].completed;

      if (completed && !completedTasks[userId]) {
        completedTasks[userId] = 0;
      }

      if (completed) {
        ++completedTasks[userId];
      }
    }
  }

  // print complted tasks to the console
  console.log(completedTasks);
});
