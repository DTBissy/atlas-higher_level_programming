#!/usr/bin/node
$(document).ready(function () {
  $('DIV#update_header').click(function () {
    if ($('header').text('First HTML page')) {
      $('header').text('New Header!!!');
    }
  });
});
