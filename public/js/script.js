$(document).ready(function(){

  var photos = $('.portraits li');

  $.each(photos, function(k,v) {
    var photo = $(v);
    var img = photo.find('img');

    var time_element = $('<time>' + img.attr('alt') + '</time>');
    time_element.appendTo(photo);

    var time = $('time', photo);
    photo.on('mouseover', function() {
      time.show();
    });
    photo.on('mouseout', function() {
      time.hide();
    });
    photo.on('click', function() {
      cool_box(img.clone());
    });
  });