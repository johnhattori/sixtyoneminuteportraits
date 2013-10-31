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
});