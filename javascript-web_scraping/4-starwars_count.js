#!/usr/bin/node
'use strict';

const request = require('request');

request(process.argv[2], (error, response, body) => {
  if (!error && response.statusCode === 200) {
    const films = JSON.parse(body).results;
    let count = 0;
    for (const film of films) {
      for (const author of film.characters) {
        const id = author.split('/people/')[1].split('/')[0];
        if (parseInt(id) === 18) {
          ++count;
        }
      }
    }
    console.log(count);
  }
});
