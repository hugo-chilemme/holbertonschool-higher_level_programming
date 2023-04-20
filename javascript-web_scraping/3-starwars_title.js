#!/usr/bin/node
'use strict';

const request = require('request');

request('https://swapi-api.hbtn.io/api/films/' + process.argv[2], (error, response, body) => {
  if (!error && response.statusCode === 200) {
    const obj = JSON.parse(body);
    console.log(obj.title);
  }
});
