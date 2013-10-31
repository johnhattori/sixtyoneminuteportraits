$(document).ready(function() {
	$('.fancybox-media').fancybox({
		openEffect  : 'none',
		closeEffect : 'none',
		padding: 0,
		helpers : {
			media : {}
		},
		onPlayStart: function() {console.log('onPlayStart');},
		beforeShow  : function() {console.log('beforeShow');},
		afterShow  : function() {console.log('afterShow'); 
								started();
								setTimeout(function() {console.log('closing');
													   //$.fancybox.close();
													   //started();
													} ,
													   60000)},
		onFinish  : function() {console.log('onFinish');},
		onPlayEnd  : function() {console.log('onPlayEnd');},
		onComplete  : function() {console.log('onComplete');},
		afterLoad  : function() {console.log('afterLoad');}
	});

	//$('.fancybox-media')

	//function onMessageReceived(event) {
    //    console.log("onMessageReceived---1: ", event);
    //}
    //if (window.addEventListener) {
    //    window.addEventListener('message', onMessageReceived, false);
    //}
    //	// IE
    //else {
    //    window.attachEvent('onmessage', onMessageReceived);
    //}

	function started() {
		
		//console.log('started');
		var iframe = $('.fancybox-iframe')[0];
		var player = $f(iframe);
		player.addEvent('ready', function() {
		//	console.log('ready');
			//player.addEvent('onFinish', function() {console.log('onFinish'); });
			//player.addEvent('onPlayEnd', function() {console.log('onPlayEnd'); });
			//player.addEvent('onComplete', function() {console.log('onComplete'); });
			//player.addEvent('afterLoad', function() {console.log('afterLoad'); });
			//player.addEvent('play', function() {console.log('play'); });
			player.addEvent('pause', function(id) {console.log('pause!!!'); });
			//player.addEvent('playProgress', function(data, id) {console.log('playProgress'); });
			player.addEvent('finish', function(id) {console.log('finish!!!'); $.fancybox.close(); });
			//player.addEvent('seek', function() {console.log('seek'); });
			//player.api("setVolume", 0);
			//player.api("seekTo", 10);
			//player.api("setLoop", 1); //video doesn't loop. Only plays for once.
		});
        




        /*
		//var f = $('.fancybox-iframe')
		//var url = f.attr('src').split('?')[0]

		// Listen for messages from the player
		if (window.addEventListener){
		    window.addEventListener('message', onMessageReceived, false);
		}
		else {
		    window.attachEvent('onmessage', onMessageReceived, false);
		}

		// Handle messages received from the player
		function onMessageReceived(e) {
		    var data = JSON.parse(e.data);
		    
		    switch (data.event) {
		        case 'ready':
		            //onReady();
		            console.log('readying');
		            break;
		           
		        case 'playProgress':
		            //onPlayProgress(data.data);
		            break;
		            
		        case 'pause':
		            //onPause();
		            console.log('pausing');
		            break;
		           
		        case 'finish':
		            //onFinish();
		            console.log('its over');
		            break;
		    }
		}
		*/





	}






});