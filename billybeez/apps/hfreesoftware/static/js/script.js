$j = jQuery.noConflict();				   
	
$j(document).ready(function() {	
    			   
	$j("ul.sf-menu").superfish({
		autoArrows:  false,
		delay:       400,                             // one second delay on mouseout 
		animation:   {opacity:'show',height:'show'},  // fade-in and slide-down animation 
		speed:       'fast',                          // faster animation speed 
		autoArrows:  false,                           // disable generation of arrow mark-up 
		dropShadows: false                            // disable drop shadows 			
	}); 
	
	// wrap 'span' to nav page link
	$j('.topnav ul').children('li').each(function() {
		$j(this).children('a').html('<span>'+$j(this).children('a').text()+'</span>'); // add tags span to a href
	});
	$j('#nav1 ul').children('li').each(function() {
		$j(this).children('a').html('<span>'+$j(this).children('a').text()+'</span>'); // add tags span to a href
	});
	
	var show_slideshow = false;
	$j("#slideshow").children().each(function() {
	    if (this.tagName == "IMG" || $j(this).hasClass("plugin_picture")) {
	        show_slideshow = true;
	        var parent = $j(this).parent()
	        var inner_node = $j('<div class="slide-image"><a href="#"></a></div>');
	        $j("a", inner_node).append(this);
	        $j(parent).append(inner_node);
	        $j("#slider_nav").append('<li><a href="#"></a></li>');
	    }
	    else if ($j(this).hasClass('cms_placeholder-bar')) {
	        $j("#slideshow").css("height", "auto");
        }
	    else {
	        $j("#content").prepend(this);
	    }
	});
	if (show_slideshow) {
	    $j('#slideshow').cycle({
            fx:     'fade',
            speed:  'slow',
            timeout: 5000,
            pager:  '#slider_nav',
            pagerAnchorBuilder: function(idx, slide) {
                // return sel string for existing anchor
                return '#slider_nav li:eq(' + (idx) + ') a';
            }
        });
        $("#slider_nav").css("width", $("#slider_nav").children().length*22);
    }
	
	// radius Box
	$j('.social-links span').css({"border-radius": "3px", "-moz-border-radius":"3px", "-webkit-border-radius":"3px"});	
	$j('.wp-pagenavi a, .wp-pagenavi .current').css({"border-radius": "3px", "-moz-border-radius":"3px", "-webkit-border-radius":"3px"});

});
