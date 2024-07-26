#!/usr/bin/node
const request = require('request');

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
  }
});
