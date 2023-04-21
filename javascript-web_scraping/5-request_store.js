#!/usr/bin/node
'use strict';

const request = require('request');
const fs = require('fs');

request(process.argv[2], (error, response, body) => {
  if (!error && response.statusCode === 200) {
    fs.writeFile(process.argv[3], body, err => {
      if (err) {
        console.error(err);
      }
    });
  }
});
