#!/usr/bin/node
'use strict';

const request = require('request');

const findUrl = 'https://swapi-api.hbtn.io/api/people/18/';

request(process.argv[2], (error, response, body) => {
  if (!error && response.statusCode === 200) {
    const films = JSON.parse(body).results;
    let count = 0;
    for (const film of films) {
      if (film.characters.includes(findUrl)) {
        ++count;
      }
    }
    console.log(count);
  }
});
