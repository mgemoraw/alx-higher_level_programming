$(document).ready(function () {
    // change color of header element to #FF0000
  $('DIV#add_item').click(function () {
    $('UL.my_list').append('<li>Item</li>');
  });
});
