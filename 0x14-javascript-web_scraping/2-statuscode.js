#!/usr/bin/node
const request = require('request');

var url = process.argv[2];
request.get(url).on('response', (response) => {
    console.log(response.statusCode)
});
