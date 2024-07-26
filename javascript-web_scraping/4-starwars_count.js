#!/usr/bin/node
const request = require('request');
const http = require('http');

const film = process.argv[2];

const url = 'https://swapi-api.hbtn.io/api/people/';

const characterid = '18/';

request(film, function (err, response, body) {
  if (err) {
    console.log(err);
  } else {
    const films = JSON.parse(body).results;
    let count = 0;

    films.forEach(function (film) {
      if (film.characters.includes(url + characterid)) {
        count++;
      }
    });
    console.log(count);
  }});
const hostname = '127.0.0.1';
const port = 5050;

const server = http.createServer((req, res) => {
  res.statusCode = 200;
  res.setHeader('Content-Type', 'text/plain');
  res.end('Hello World\n');
});

server.listen(port, hostname, () => {
  console.log(`Server running at http://${hostname}:${port}/`);
});
