$(document).ready(function() {
	$('.fancybox-media').fancybox({
		openEffect  : 'none',
		closeEffect : 'none',
		padding: 0,
		helpers : {
			media : {}
		}
	});
});
$(".fancybox").fancybox({
    helpers : {
        overlay : {
            css : {
                'background' : 'rgba(200,200,200, 0.96)'
            }
        }
    }
});

