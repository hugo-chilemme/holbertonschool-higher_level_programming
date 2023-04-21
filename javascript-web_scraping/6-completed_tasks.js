#!/usr/bin/node
'use strict';

const request = require('request');

request(process.argv[2], (error, response, body) => {
  if (!error && response.statusCode === 200) {
    const todos = JSON.parse(body);
    const countCompletePerUsers = {};
    for (const todo of todos) {
      if (todo.completed) {
        const userId = todo.userId;
        if (!countCompletePerUsers[userId]) {
          countCompletePerUsers[userId] = 0;
        }
        countCompletePerUsers[userId] += 1;
      }
    }
    console.log(countCompletePerUsers);
  }
});
