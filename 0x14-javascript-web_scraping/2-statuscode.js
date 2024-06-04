#!/usr/bin/node
const request = require('request');

let url = process.argv[2];
request.get(url).on('response', (response) => {
    console.log(`code: ${response.statusCode}`);
});
