$(document).ready(function () {
    // change color of header element to #FF0000
    const url = 'https://hellosalut.stefanbohacek.dev/?lang=fr';

  $.get(url, function (data) {
    $('DIV#hello').text(data.hello);
  });
});
