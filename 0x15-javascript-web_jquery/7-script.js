$(document).ready(function () {
    // change color of header element to #FF0000
    const url = 'https://swapi-api.alx-tools.com/api/people/5/?format=json';

  $.get(url, function (data) {
    $('DIV#character').text(data.name);
  });
});
