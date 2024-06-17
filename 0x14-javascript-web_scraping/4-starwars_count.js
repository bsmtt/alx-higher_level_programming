#!/usr/bin/node
const request = require('request');
const url = process.argv[2];

request(url, (error, response, body) => {
  if (!error) {
    const results = JSON.parse(body).results;
    const filtered = results.filter(film => film.characters.find((character) => character.endsWith('/18/')));
    console.log(filtered.length);
  }
});
