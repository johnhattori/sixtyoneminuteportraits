$(document).ready(function() {
	$('.fancybox-media').fancybox({
		openEffect  : 'none',
		closeEffect : 'none',
		padding: 0,
		helpers : { media: {}},
		afterShow: playback_started
	});

	function playback_started() {
		var iframe = $('.fancybox-iframe')[0];
		var player = $f(iframe);
		player.addEvent('ready', function() {
			player.addEvent('finish', function(id) {$.fancybox.close()});
		});
	}

	$.getJSON("portraits.json", function( data ) {
		$(".portraits").append("<ul></ul>");

	  	$.each( data, function( key, val ) {
	  		portrait = "<li>"
	    	portrait += "<a href='" + val["video"] + "' class='fancybox-media'>"
	    	portrait += "<img class='img_a' src='" + val["thumbnail"] + "' alt='" + val["name"] + "'>"
	    	portrait += "<div>" + val["name"] + "</div>"
	    	portrait += "</a></li>"
	    	$(".portraits ul").append(portrait);
	  	});
	});

});