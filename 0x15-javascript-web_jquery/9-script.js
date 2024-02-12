$(document).ready(function () {
    // change color of header element to #FF0000
    url = 'https://hellosalut.stefanbohacek.dev/?lang=fr';

  $.get(url, function (data) {
    $('DIV#hello').text(data.hello);
  });
});
