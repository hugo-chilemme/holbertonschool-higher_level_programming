#!/usr/bin/node
'use strict';

const request = require('request');

request(process.argv[2], (error, response, body) => {
  if (!error) {
    console.log('code: ' + response.statusCode);
  }
});
