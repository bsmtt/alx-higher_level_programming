#!/usr/bin/node
const request = require('request');

request(process.argv[2], function (error, response, body) {
  if (!error) {
    const todos = JSON.parse(body);
    const completed = todos.filter(todo => todo.completed === true);
    const maped = {};
    completed.forEach((todo) => {
      if (todo.completed && maped[todo.userId] === undefined) {
        maped[todo.userId] = 1;
      } else if (todo.completed) {
        maped[todo.userId] += 1;
      }
    });
    console.log(maped);
  }
});
