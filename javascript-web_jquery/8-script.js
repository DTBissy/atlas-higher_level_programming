#!/usr/bin/node
$(document).ready(function () {
  $.getJSON('https://swapi-api.hbtn.io/api/films/?format=json', function (data) {
    data.results.forEach(function (movie) {
      // $('UL#list_movies').append('<li>' + movie.title + '</li>');
      $('<li>' + movie.title + '</li>').appendTo("UL#list_movies");
    })
  })
});
