$(document).ready(function () {
    // change color of header element to #FF0000
    url = 'https://swapi-api.alx-tools.com/api/people/5/?format=json';

  $.get(url), function (data) {
    $('UL#list_movies').append(...data.results.map(movie=> `<li>${movie.title}</li>`));
  };
});
