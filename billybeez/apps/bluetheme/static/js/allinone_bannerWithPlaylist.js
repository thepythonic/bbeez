(function($) {
	
	//the vars
	var effects_arr=new Array(
			'fade',
			
			'slideFromLeft',
			'slideFromRight',
			'slideFromTop',
			'slideFromBottom',
			
			'topBottomDroppingStripes',
			'topBottomDroppingReverseStripes',
			
			'bottomTopDroppingStripes',
			'bottomTopDroppingReverseStripes',
			
			'asynchronousDroppingStripes',
			
			'leftRightFadingStripes',
			'leftRightFadingReverseStripes',
			
			'topBottomDiagonalBlocks',
			'topBottomDiagonalReverseBlocks',
			
			'randomBlocks'					
			
	);		
	
	var stripe_width;
	var new_stripe_width;
	var delay_time = 100;
	var delay_time_stripes_step=50;
	var delay_time_blocks_step=25;	
	
	
	var currentCarouselTop=0;	
	
	
	function animate_singular_text(elem) {
		elem.animate({
                opacity: 1,
                left: elem.attr('data-final-left')+'px',
                top: elem.attr('data-final-top')+'px'
              }, elem.attr('data-duration')*1000, function() {
                //alert (elem.attr('data-initial-left'));
              });			
	};
    
    
    
    
	function animate_texts(current_obj,allinone_bannerWithPlaylist_the,bannerControls) {
		$(current_obj.currentImg.attr('data-text-id')).css("display","block");
		var texts = $(current_obj.currentImg.attr('data-text-id')).children();
		$(current_obj.currentImg.attr('data-text-id')).css('width',allinone_bannerWithPlaylist_the.width()+'px');
		$(current_obj.currentImg.attr('data-text-id')).css('left',bannerControls.css('left'));//alert (allinone_bannerWithPlaylist_the.width());
		$(current_obj.currentImg.attr('data-text-id')).css('top',bannerControls.css('top'));
		
		var i=0;
		currentText_arr=Array();
		texts.each(function() {
			currentText_arr[i] = $(this);
            //alert (currentText_arr[i].attr('data-initial-left'));
            //currentText_arr[i].css("display","block");
            currentText_arr[i].css("left",currentText_arr[i].attr('data-initial-left')+'px');
            currentText_arr[i].css("top",currentText_arr[i].attr('data-initial-top')+'px'); 
            currentText_arr[i].css("opacity",parseInt(currentText_arr[i].attr('data-fade-start'))/100); 
            
            var currentText=currentText_arr[i];
            setTimeout(function() { animate_singular_text(currentText);}, (currentText_arr[i].attr('data-delay')*1000));    
            	
            i++;
        });		
	};

	function shuffle(o){
		for(var j, x, i = o.length; i; j = parseInt(Math.random() * i), x = o[--i], o[i] = o[j], o[j] = x);
		return o;
	};	
	
    // generate the stripes
	function allinone_bannerWithPlaylist_generate_stripes(allinone_bannerWithPlaylist_container,options,current_obj){
		$('.stripe', allinone_bannerWithPlaylist_container).remove();
		$('.block', allinone_bannerWithPlaylist_container).remove();
    	
        stripe_width = Math.round(allinone_bannerWithPlaylist_container.width()/options.numberOfStripes);
    	//alert (allinone_bannerWithPlaylist_container.width()+'  --  '+stripe_width)
		new_stripe_width=stripe_width;
		//alert(allinone_bannerWithPlaylist_container.width()+' - '+stripe_width);
    	for(var i = 0; i < options.numberOfStripes; i++){
			if (i == options.numberOfStripes-1) {
				new_stripe_width=allinone_bannerWithPlaylist_container.width()-stripe_width*(options.numberOfStripes-1);
				//alert (stripe_width+'  -  '+new_stripe_width);
			}
			allinone_bannerWithPlaylist_container.append(
				$('<div class="stripe"></div>').css({ 
					opacity:'0',
					left:(stripe_width*i)+'px', 
					width:new_stripe_width+'px',
					height:'0px', 
					background: 'url("'+ current_obj.currentImg.attr('src') +'") no-repeat -'+ ((stripe_width + (i * stripe_width)) - stripe_width) +'px 0%'
				})
			);					
		}
    };
    
    
    function animate_block(block,i,j,options,allinone_bannerWithPlaylist_container){
        var w = block.width();
        var h = block.height();
        block.css({'width':'0'});
        block.css({'height':'0'});
        if (i==options.numberOfRows-1 && j==options.numberOfColumns-1) 
        	setTimeout(function(){
				block.animate({ opacity:'1.0', width:w, height:h }, (options.effectDuration*1000)/3 , '', function(){ allinone_bannerWithPlaylist_container.trigger('effectComplete'); });
			}, (delay_time));               	
        else	
			setTimeout(function(){
				block.animate({ opacity:'1.0', width:w, height:h }, (options.effectDuration*1000)/3 );
			}, (delay_time));
		delay_time += delay_time_blocks_step;
	};    
    
    
    // generate the blocks
	function allinone_bannerWithPlaylist_generate_blocks(allinone_bannerWithPlaylist_container,options,current_obj){
		$('.stripe', allinone_bannerWithPlaylist_container).remove();
		$('.block', allinone_bannerWithPlaylist_container).remove();
		var block_width = Math.round(allinone_bannerWithPlaylist_container.width()/options.numberOfColumns);
		var block_height = Math.round(allinone_bannerWithPlaylist_container.height()/options.numberOfRows);	        	
    	
        for(var i = 0; i < options.numberOfRows; i++){
        	for(var j = 0; j < options.numberOfColumns; j++){
        		allinone_bannerWithPlaylist_container.append(
					$('<div class="block"></div>').css({ 
						opacity:'0',
						left:(block_width*j)+'px', 
						top:(block_height*i)+'px',
						width:block_width+'px',
						height:block_height+'px',
						background: 'url("'+ current_obj.currentImg.attr('src') +'") no-repeat -'+ ((block_width + (j * block_width)) - block_width) +'px -'+ ((block_height + (i * block_height)) - block_height) +'px'
					})
				);	
        	}
		}
    };	
	
	
    // navigation
    function allinone_bannerWithPlaylist_navigation(direction,current_obj,options,total_images,thumbsHolder_Thumbs,allinone_bannerWithPlaylist_container,thumbsHolder_Thumb,thumbMarginTop,allinone_bannerWithPlaylist_thumbsHolder,allinone_bannerWithPlaylist_sliderVertical,imgs){
		var navigateAllowed=true;
		if ((!options.loop && current_obj.current_img_no+direction>=total_images) || (!options.loop && current_obj.current_img_no+direction<0))
			navigateAllowed=false;
		
		if (navigateAllowed) {
			//hide previous texts
			//$(current_obj.currentImg.attr('data-text-id')).css('opacity','0');
			$(current_obj.currentImg.attr('data-text-id')).css("display","none");
			
			//deactivate previous
			$(thumbsHolder_Thumbs[current_obj.current_img_no]).removeClass('thumbsHolder_ThumbON');
			
			//set current img
			if (options.randomizeImages) {
				var rand_no=Math.floor(Math.random() * total_images);
				if (current_obj.current_img_no===rand_no)
					current_obj.current_img_no=Math.floor(Math.random() * total_images);
				else
					current_obj.current_img_no=rand_no;
			} else {
				if (current_obj.current_img_no+direction>=total_images) {
					current_obj.current_img_no=0;
				} else if (current_obj.current_img_no+direction<0) {
					current_obj.current_img_no=total_images-1;
				} else {
					current_obj.current_img_no+=direction;
				}
			}
			//activate current
			$(thumbsHolder_Thumbs[current_obj.current_img_no]).addClass('thumbsHolder_ThumbON');
			//auto scroll carousel if needed
			/*currentCarouselTop=allinone_bannerWithPlaylist_thumbsHolder.css('top').substr(0,allinone_bannerWithPlaylist_thumbsHolder.css('top').lastIndexOf('px'));*/
			
//carouselScroll(0,thumbsHolder_Thumb,thumbMarginTop,total_images,allinone_bannerWithPlaylist_thumbsHolder,options,current_obj,allinone_bannerWithPlaylist_sliderVertical);
			
			current_obj.currentImg = $(imgs[current_obj.current_img_no]);
            if(!current_obj.currentImg.is('img')){
            	current_obj.currentImg = current_obj.currentImg.find('img:first');
            }				
            
			//set current_effect
			if(current_obj.currentImg.attr('data-transition')){
				current_effect = current_obj.currentImg.attr('data-transition');
            } else if (options.defaultEffect!='random') {
            	current_effect=options.defaultEffect;	            	
            } else {
            	current_effect=effects_arr[Math.floor(Math.random()*(effects_arr.length))];
            }

			//alert(current_obj.current_img_no);
			current_obj.effectIsRunning=true;
			if(current_effect == 'fade' || current_effect == 'slideFromLeft' || current_effect == 'slideFromRight' || current_effect == 'slideFromTop' || current_effect == 'slideFromBottom'){
				//alert ("fade");
				allinone_bannerWithPlaylist_generate_stripes(allinone_bannerWithPlaylist_container,options,current_obj);
				var first_stripe = $('.stripe:first', allinone_bannerWithPlaylist_container);
				
				if (current_effect == 'fade') {
					first_stripe.css({
	                    'height': '100%',
	                    'width': allinone_bannerWithPlaylist_container.width() + 'px'
	                });
					first_stripe.animate({ opacity:'1.0' }, (options.effectDuration*2000), '', function(){ allinone_bannerWithPlaylist_container.trigger('effectComplete'); });
				}
				
				if (current_effect == 'slideFromLeft') {
					first_stripe.css({
	                    'height': '100%',
	                    'width': '0'
	                });
					first_stripe.animate({ opacity:'1.0', width:allinone_bannerWithPlaylist_container.width() + 'px' }, (options.effectDuration*1000), '', function(){ allinone_bannerWithPlaylist_container.trigger('effectComplete'); });
				}
				
				if (current_effect == 'slideFromRight') {
					first_stripe.css({
	                    'height': '100%',
	                    'width':  '0',
	                    'left': allinone_bannerWithPlaylist_container.width()+5 + 'px'
	                });
					first_stripe.animate({ opacity:'1.0', left:'0', 'width':  allinone_bannerWithPlaylist_container.width() + 'px' }, (options.effectDuration*1000), '', function(){ allinone_bannerWithPlaylist_container.trigger('effectComplete'); });
				}

				if (current_effect == 'slideFromTop') {
					first_stripe.css({
	                    'height': '0',
	                    'width': allinone_bannerWithPlaylist_container.width() + 'px'
	                });
					first_stripe.animate({ opacity:'1.0', height:allinone_bannerWithPlaylist_container.height() + 'px' }, (options.effectDuration*1000), '', function(){ allinone_bannerWithPlaylist_container.trigger('effectComplete'); });
				}
				
				if (current_effect == 'slideFromBottom') {
					first_stripe.css({
	                    'height': '0',
	                    'width': allinone_bannerWithPlaylist_container.width() + 'px',
	                    'top': allinone_bannerWithPlaylist_container.height() + 'px'
	                });
					first_stripe.animate({ opacity:'1.0', top:0, height:allinone_bannerWithPlaylist_container.height() + 'px' }, (options.effectDuration*1000), '', function(){ allinone_bannerWithPlaylist_container.trigger('effectComplete'); });
				}					
				
			}   
			
			if(current_effect.indexOf('Stripes')>=0) {
				allinone_bannerWithPlaylist_generate_stripes(allinone_bannerWithPlaylist_container,options,current_obj);
				if (current_effect.indexOf('Reverse')>=0){
					var stripes = $('.stripe', allinone_bannerWithPlaylist_container).myReverse();
				} else {
					var stripes = $('.stripe', allinone_bannerWithPlaylist_container);
				}
				delay_time = 100;
				i = 0;
				stripes.each(function(){
					var stripe = $(this);
					//setting the css for stripes according to current effect
					if(current_effect=='topBottomDroppingStripes' || current_effect=='topBottomDroppingReverseStripes')
						stripe.css({ 'top': '0px' });
					if(current_effect=='bottomTopDroppingStripes' || current_effect=='bottomTopDroppingReverseStripes')
						stripe.css({ 'bottom': '0px' });
					if(current_effect=='leftRightFadingStripes' || current_effect=='leftRightFadingReverseStripes')
						stripe.css({ 'top': '0px', 'height':'100%', 'width':'0' });						
					if (current_effect=='asynchronousDroppingStripes') {
						if (i % 2)
							stripe.css({ 'top': '0px' });
						else
							stripe.css({ 'bottom': '0px' });
					} 
					
					if(current_effect=='leftRightFadingStripes' || current_effect=='leftRightFadingReverseStripes') {
						var aux_stripe_width=stripe_width;
						if ( (current_effect=='leftRightFadingStripes' && i == options.numberOfStripes-1) || (current_effect=='leftRightFadingReverseStripes' && i==0) )
							aux_stripe_width=new_stripe_width;
						
						
						if(i == options.numberOfStripes-1){
							setTimeout(function(){
								stripe.animate({ width:aux_stripe_width+'px', opacity:'1.0' }, (options.effectDuration*800), '', function(){ allinone_bannerWithPlaylist_container.trigger('effectComplete'); });
							}, (delay_time));
						} else {
							setTimeout(function(){
								stripe.animate({ width:aux_stripe_width+'px', opacity:'1.0' }, (options.effectDuration*800) );
							}, (delay_time));
						}							
					} else {
							if(i == options.numberOfStripes-1){
								setTimeout(function(){
									stripe.animate({ height:'100%', opacity:'1.0' }, (options.effectDuration*1000), '', function(){ allinone_bannerWithPlaylist_container.trigger('effectComplete'); });
								}, (delay_time));
							} else {
								setTimeout(function(){
									stripe.animate({ height:'100%', opacity:'1.0' }, (options.effectDuration*1000) );
								}, (delay_time));
							}
					}
					delay_time += delay_time_stripes_step;
					i++;
				});
			} //if stripes
			
			
			if(current_effect.indexOf('Blocks')>=0) {
				allinone_bannerWithPlaylist_generate_blocks(allinone_bannerWithPlaylist_container,options,current_obj);
				if (current_effect.indexOf('Reverse')>=0){
					var blocks = $('.block', allinone_bannerWithPlaylist_container).myReverse();
				} else if (current_effect=='randomBlocks') {
					var blocks = shuffle($('.block', allinone_bannerWithPlaylist_container));
				} else {
					var blocks = $('.block', allinone_bannerWithPlaylist_container);
				}
				delay_time = 100;
				
				if (current_effect=='randomBlocks') {
					i=0;
					var total_blocks = options.numberOfRows*options.numberOfColumns;
					blocks.each(function(){
						var block = $(this);
		                var w = block.width();
		                var h = block.height();
		                block.css({'width':'0'});
		                block.css({'height':'0'});							
						if(i == total_blocks-1){
		                	setTimeout(function(){
								block.animate({ opacity:'1.0', width:w, height:h }, (options.effectDuration*1000)/3 , '', function(){ allinone_bannerWithPlaylist_container.trigger('effectComplete'); });
							}, (delay_time));               	
						} else {
							setTimeout(function(){
								block.animate({ opacity:'1.0', width:w, height:h }, (options.effectDuration*1000)/3 );
							}, (delay_time));
						}
						delay_time += delay_time_blocks_step;
						i++;
					});						
				} else {

						var row_i=0;
						var col_i=0;
						var blocks_arr=new Array();
						blocks_arr[row_i] = new Array();
						blocks.each(function(){
								blocks_arr[row_i][col_i] = $(this);
								col_i++;
								if(col_i == options.numberOfColumns){
									row_i++;
									col_i = 0;
									blocks_arr[row_i] = new Array();
								}
						});
	
						
						//first part
						row_i=0;
						col_i=0;
						delay_time = 100;
						var block = $(blocks_arr[row_i][col_i]);
						animate_block(block,0,0,options,allinone_bannerWithPlaylist_container);
						while (row_i<options.numberOfRows-1 || col_i<options.numberOfColumns-1) {
							if (row_i<options.numberOfRows-1)
								row_i++;
							if (col_i<options.numberOfColumns-1)
								col_i++;
	
							i=row_i;
							if (col_i<row_i && options.numberOfRows>options.numberOfColumns)
								i=row_i-col_i;
							j=0;
							if (row_i<col_i && options.numberOfRows<options.numberOfColumns)
								j=col_i-row_i;
							while (i>=0 && j<=col_i) {
								var block = $(blocks_arr[i--][j++]);
								animate_block(block,i,j,options,allinone_bannerWithPlaylist_container);
								//alert (i+' - '+j);
							}
	
						}
						
						
						//last part
						if (options.numberOfRows<options.numberOfColumns)
							delay_time-=(options.numberOfRows-1)*delay_time_blocks_step;
						else
							delay_time-=(options.numberOfColumns-1)*delay_time_blocks_step;
						
						limit_i=0;
						limit_j=col_i-row_i;
						//alert (limit_j)
						//alert (row_i+'  -  '+col_i+' - '+limit_i+' - '+limit_j)
						while (limit_i<row_i && limit_j<col_i) {
							i=row_i+1; //options.numberOfRows-1;
							j=limit_j;
							while (i>limit_i && j<col_i) {
								i=i-1;
								j=j+1;							
								var block = $(blocks_arr[i][j]);
								animate_block(block,i,j,options,allinone_bannerWithPlaylist_container);
								//alert (i+'-'+j);
							}
							limit_i++;
							limit_j++;
						}
	
				} // else randomBlocks
			} // if blocks
			
		} // if navigateAllowed
		
	};
    
    
	function carouselScroll(direction,thumbsHolder_Thumb,thumbMarginTop,total_images,allinone_bannerWithPlaylist_thumbsHolder,options,current_obj,allinone_bannerWithPlaylist_sliderVertical) {
		var MAX_TOP=(thumbsHolder_Thumb.height()+thumbMarginTop)*(total_images-1);
		//alert (allinone_bannerWithPlaylist_sliderVertical.slider( "option", "animate" ));
		allinone_bannerWithPlaylist_thumbsHolder.stop(true,true);
		//alert(current_obj.isCarouselScrolling)
		if (direction && !current_obj.isCarouselScrolling) {
			
			current_obj.isCarouselScrolling=true;
			//allinone_bannerWithPlaylist_thumbsHolder.css('opacity','0.5');
			
			
			allinone_bannerWithPlaylist_thumbsHolder.animate({
			    //opacity: 1,
			    top:parseInt(options.borderWidth+MAX_TOP*(direction-100)/100)+'px'
			  }, 1100, 'easeOutQuad', function() {
			    // Animation complete.
				  current_obj.isCarouselScrolling=false;
			});
		} else if (!current_obj.isCarouselScrolling) {
			current_obj.isCarouselScrolling=true;
			allinone_bannerWithPlaylist_thumbsHolder.css('opacity','0.5');			
			var new_top=parseInt(options.borderWidth-(thumbsHolder_Thumb.height()+thumbMarginTop)*current_obj.current_img_no);
			allinone_bannerWithPlaylist_sliderVertical.slider( "value" , 100 + parseInt( new_top * 100 / MAX_TOP ) );
			allinone_bannerWithPlaylist_thumbsHolder.animate({
			    opacity: 1,
			    top:new_top+'px'
			  }, 500, 'easeOutCubic', function() {
			    // Animation complete.
				  current_obj.isCarouselScrolling=false;
			});
		}
	};
	
	
    
	
	
	
	
	$.fn.allinone_bannerWithPlaylist = function(options) {
	

		var options = $.extend({},$.fn.allinone_bannerWithPlaylist.defaults, options);

		return this.each(function() {
			var allinone_bannerWithPlaylist_the = $(this);
			
			//the controllers
			var allinone_bannerWithPlaylist_wrapBorder = $('<div></div>').addClass('allinone_bannerWithPlaylistBorder');
			var allinone_bannerWithPlaylist_wrap = $('<div></div>').addClass('allinone_bannerWithPlaylist').addClass(options.skin);
			var bannerControls = $('<div class="bannerControls">   <div class="leftNav"></div>   <div class="rightNav"></div>    <div class="thumbsHolderWrapper"><div class="thumbsHolderVisibleWrapper"><div class="thumbsHolder"></div></div></div>  <div class="slider-vertical"></div>     </div>');						
			allinone_bannerWithPlaylist_the.wrap(allinone_bannerWithPlaylist_wrap);
			allinone_bannerWithPlaylist_the.after(bannerControls);
			
			
			 
			if (!options.showAllControllers)
				bannerControls.css("display","none");
			
			//the elements
			var allinone_bannerWithPlaylist_container = allinone_bannerWithPlaylist_the.parent('.allinone_bannerWithPlaylist');
			var bannerControls = $('.bannerControls', allinone_bannerWithPlaylist_container);
			
			allinone_bannerWithPlaylist_container.wrap(allinone_bannerWithPlaylist_wrapBorder);
			var allinone_bannerWithPlaylist_border = allinone_bannerWithPlaylist_container.parent('.allinone_bannerWithPlaylistBorder');
			
			var allinone_bannerWithPlaylist_leftNav = $('.leftNav', allinone_bannerWithPlaylist_container);
			var allinone_bannerWithPlaylist_rightNav = $('.rightNav', allinone_bannerWithPlaylist_container);
			allinone_bannerWithPlaylist_leftNav.css("display","none");
			allinone_bannerWithPlaylist_rightNav.css("display","none");			
			if (options.showNavArrows) {
				if (options.showOnInitNavArrows) {
					allinone_bannerWithPlaylist_leftNav.css("display","block");
					allinone_bannerWithPlaylist_rightNav.css("display","block");
				}
			}
			

			var allinone_bannerWithPlaylist_thumbsHolderWrapper = $('.thumbsHolderWrapper', allinone_bannerWithPlaylist_container);
			var allinone_bannerWithPlaylist_thumbsHolderVisibleWrapper = $('.thumbsHolderVisibleWrapper', allinone_bannerWithPlaylist_container);
			var allinone_bannerWithPlaylist_thumbsHolder = $('.thumbsHolder', allinone_bannerWithPlaylist_container);
			var allinone_bannerWithPlaylist_sliderVertical = $('.slider-vertical', allinone_bannerWithPlaylist_container);
			

			
		

			var current_effect=options.defaultEffect;
			var total_images=0;
			var current_obj = {
					current_img_no:0,
					currentImg:0,
					isCarouselScrolling:false,
					effectIsRunning:false
				};	
			var timeoutID; // the autoplay timeout ID
			var mouseOverBanner=false;

			var i = 0;
			

			
			//set banner size
			allinone_bannerWithPlaylist_border.width(options.width);			
			allinone_bannerWithPlaylist_border.height(options.height);
			allinone_bannerWithPlaylist_border.css("background",options.borderColor);
			
			allinone_bannerWithPlaylist_container.width(options.width - 3*options.borderWidth - options.playlistWidth);
			allinone_bannerWithPlaylist_container.height(options.height - 2*options.borderWidth);
			allinone_bannerWithPlaylist_container.css("left",options.borderWidth+'px');
			allinone_bannerWithPlaylist_container.css("top",options.borderWidth+'px');
			
			bannerControls.width('100%');
			bannerControls.height('100%');
			
			
			//alert (allinone_bannerWithPlaylist_thumbsHolderVisibleWrapper.width());
			allinone_bannerWithPlaylist_thumbsHolderVisibleWrapper.width(options.playlistWidth);
			allinone_bannerWithPlaylist_thumbsHolderVisibleWrapper.height(allinone_bannerWithPlaylist_container.height());
			//allinone_bannerWithPlaylist_thumbsHolderVisibleWrapper.css('top',0);
			
			
			allinone_bannerWithPlaylist_thumbsHolderWrapper.width(options.playlistWidth);
			allinone_bannerWithPlaylist_thumbsHolderWrapper.height(allinone_bannerWithPlaylist_container.height());
			allinone_bannerWithPlaylist_thumbsHolderWrapper.css("top",0);
			allinone_bannerWithPlaylist_thumbsHolderWrapper.css("right",(-1)*(options.borderWidth+options.playlistWidth)+'px');			
			
			
			allinone_bannerWithPlaylist_thumbsHolder.width(options.playlistWidth);
			allinone_bannerWithPlaylist_thumbsHolder.css('top',options.borderWidth+'px');
			
			var thumbMarginTop=0;			
			
			//get images
			var imgs = allinone_bannerWithPlaylist_the.children();
			var thumbsHolder_Thumb;
			var thumbsHolder_MarginTop=0;
			var image_name='';
			var thumbUnit='';
			imgs.each(function() {
	            current_obj.currentImg = $(this);
	            if(!current_obj.currentImg.is('img')){
	            	current_obj.currentImg = current_obj.currentImg.find('img:first');
	            }
	            	
	            if(current_obj.currentImg.is('img')){
	            	current_obj.currentImg.css('display','none');
	            	total_images++;

	            
		            //generate thumbsHolder
					image_name = current_obj.currentImg.attr('src').substr(current_obj.currentImg.attr('src').lastIndexOf('/'),current_obj.currentImg.attr('src').length);
					thumbUnit='';
					if (options.showThumbs)
						thumbUnit='<img src="'+ options.thumbsFolder + image_name + '">';
					thumbsHolder_Thumb = $('<div class="thumbsHolder_ThumbOFF" rel="'+ (total_images-1) +'"><div class="padding">'+thumbUnit+'<span class="title">'+current_obj.currentImg.attr('data-title')+'</span><br><span class="reg">'+current_obj.currentImg.attr('data-desc')+'</span></div></div>');
		            allinone_bannerWithPlaylist_thumbsHolder.append(thumbsHolder_Thumb);
		            
		            thumbMarginTop=Math.floor( (allinone_bannerWithPlaylist_thumbsHolderWrapper.height()-thumbsHolder_Thumb.height()*options.numberOfThumbsPerScreen)/(options.numberOfThumbsPerScreen-1) );
		            //alert(allinone_bannerWithPlaylist_thumbsHolderWrapper.height());
		            allinone_bannerWithPlaylist_thumbsHolder.css('height',allinone_bannerWithPlaylist_thumbsHolder.height()+thumbMarginTop+thumbsHolder_Thumb.height()+'px');
		            if ( total_images<=1 ) {
		            	thumbsHolder_Thumb.css('margin-top',Math.floor( ( allinone_bannerWithPlaylist_thumbsHolderWrapper.height()-2*options.borderWidth-(thumbMarginTop+thumbsHolder_Thumb.height())*(options.numberOfThumbsPerScreen-1) - thumbsHolder_Thumb.height() )/2 )+'px');
		            } else {
// ana 3'ayart hena 
						thumbsHolder_Thumb.css('margin-top','12px');
		            }
		            	
		            
		            thumbsHolder_MarginTop=parseInt((allinone_bannerWithPlaylist_thumbsHolderWrapper.height()-parseInt(thumbsHolder_Thumb.css('height').substring(0, thumbsHolder_Thumb.css('height').length-2)))/2);
	            }
	            


	        });
			
            
            //the scroller
			if (total_images>options.numberOfThumbsPerScreen) {
				allinone_bannerWithPlaylist_sliderVertical.slider({
					orientation: "vertical",
					range: "min",
					min: 1,
					max: 100,
					step:1,
					value: 100,
					slide: function( event, ui ) {
						//alert( ui.value );
						carouselScroll(ui.value,thumbsHolder_Thumb,thumbMarginTop,total_images,allinone_bannerWithPlaylist_thumbsHolder,options,current_obj,allinone_bannerWithPlaylist_sliderVertical);
					}
				});
				allinone_bannerWithPlaylist_sliderVertical.css('display','block');
            	allinone_bannerWithPlaylist_sliderVertical.height(allinone_bannerWithPlaylist_thumbsHolderWrapper.height()-25); // 25 is the height of  .slider-vertical.ui-slider .ui-slider-handle 
            	allinone_bannerWithPlaylist_sliderVertical.css('left',Math.floor(options.width-2*options.borderWidth+(options.borderWidth-allinone_bannerWithPlaylist_sliderVertical.width())/2)+'px');
            }
		    
            
            
			//var img_inside = $('.thumbsHolder_ThumbOFF').find('img:first');
			//img_inside.css("margin-top",thumbsHolder_MarginTop+"px");
			
		
			
	        //initialize first number image
			current_obj.current_img_no = options.firstImg;
			if (options.firstImg>total_images)
				current_obj.current_img_no=total_images;
			if (options.firstImg<0)
				current_obj.current_img_no=0;			
           
        
			//initialize first image number if randomize option is set
			if(options.randomizeImages){
	        	current_obj.current_img_no = Math.floor(Math.random() * total_images);
	        }
	        

	        
	        //Get first image (using initialized above current_obj.current_img_no) and init first bg
	        if($(imgs[current_obj.current_img_no]).is('img')){
	            current_obj.currentImg = $(imgs[current_obj.current_img_no]);
	        } else {
	            current_obj.currentImg = $(imgs[current_obj.current_img_no]).find('img:first');
	        }
	        allinone_bannerWithPlaylist_container.css('background','url("'+ current_obj.currentImg.attr('src') +'") no-repeat');
	        
	  


	        
			if (options.enableTouchScreen) {
				var randomNo=Math.floor(Math.random()*100000);
				
				allinone_bannerWithPlaylist_container.wrap('<div id="bannerWithPlaylistParent_'+randomNo+'" style="position:relative;" />');
				$('#bannerWithPlaylistParent_'+randomNo).width(allinone_bannerWithPlaylist_container.width());
				$('#bannerWithPlaylistParent_'+randomNo).height(options.height-2*options.borderWidth+1);
				//$('#bannerWithPlaylistParent_'+randomNo).css('overflow','hidden');
				$('#bannerWithPlaylistParent_'+randomNo).css("left",options.borderWidth+'px');
				$('#bannerWithPlaylistParent_'+randomNo).css("top",options.borderWidth+'px');
				//$('#bannerWithPlaylistParent_'+randomNo).css('border','1px solid #ff0000');
				
				allinone_bannerWithPlaylist_container.css('cursor','url(skins/hand.cur),url(skins/hand.cur),move');
				allinone_bannerWithPlaylist_container.css("left",0+'px');
				allinone_bannerWithPlaylist_container.css("top",0+'px');
				allinone_bannerWithPlaylist_container.css('position','absolute');
				//alert(allinone_bannerWithPlaylist_container.parent().attr('id'));
				
				//$("body").css("overflow", "hidden");
				
				/*allinone_bannerWithPlaylist_container.mousedown(function() {
					bannerControls.css("display","none");
				});	*/				
				
				allinone_bannerWithPlaylist_container.draggable({ 
					axis: 'y',
					containment: 'parent',
					start: function(event, ui) {
						origTop=$(this).css('top');
					},
					stop: function(event, ui) {
						if (!current_obj.effectIsRunning) {
							finalTop=$(this).css('top');
							direction=1;
							if (origTop>=finalTop) {
								direction=-1;
							}	
							//alert (origTop+'<'+finalTop+'-'+direction);
							allinone_bannerWithPlaylist_navigation(direction,current_obj,options,total_images,thumbsHolder_Thumbs,allinone_bannerWithPlaylist_container,thumbsHolder_Thumb,thumbMarginTop,allinone_bannerWithPlaylist_thumbsHolder,allinone_bannerWithPlaylist_sliderVertical,imgs);
						}
						$(this).css('top',0+'px');
					}
					
				});
			}		        
	        
			

	        
	        
	        //generate the text for first image
	        animate_texts(current_obj,allinone_bannerWithPlaylist_the,bannerControls);
	        
	        
	        
		
			

			

	        //Event when Animation finishes
			allinone_bannerWithPlaylist_container.bind('effectComplete', function(){
				current_obj.effectIsRunning=false;
				allinone_bannerWithPlaylist_container.css('background','url("'+ current_obj.currentImg.attr('src') +'") no-repeat');

				//alert (current_obj.currentImg.attr('data-text-id'));
				animate_texts(current_obj,allinone_bannerWithPlaylist_the,bannerControls);
				
				if (options.autoPlay>0 && total_images>1 && !mouseOverBanner) {
					clearTimeout(timeoutID);
					timeoutID=setTimeout(function(){ allinone_bannerWithPlaylist_navigation(1,current_obj,options,total_images,thumbsHolder_Thumbs,allinone_bannerWithPlaylist_container,thumbsHolder_Thumb,thumbMarginTop,allinone_bannerWithPlaylist_thumbsHolder,allinone_bannerWithPlaylist_sliderVertical,imgs)},options.autoPlay*1000);
				}				
	        }); //bind
			
			
			
			

			
			
			//pause on hover
			allinone_bannerWithPlaylist_container.mouseenter(function() {
				mouseOverBanner=true;
				clearTimeout(timeoutID);
				if (options.autoHideNavArrows && options.showNavArrows) {
					allinone_bannerWithPlaylist_leftNav.css("display","block");
					allinone_bannerWithPlaylist_rightNav.css("display","block");
				}
		
			});
			
			allinone_bannerWithPlaylist_container.mouseleave(function() {
				mouseOverBanner=false;
				if (options.autoHideNavArrows && options.showNavArrows) {
					allinone_bannerWithPlaylist_leftNav.css("display","none");
					allinone_bannerWithPlaylist_rightNav.css("display","none");
				}
			
				if (options.autoPlay>0 && total_images>1) {
					clearTimeout(timeoutID);
					timeoutID=setTimeout(function(){ allinone_bannerWithPlaylist_navigation(1,current_obj,options,total_images,thumbsHolder_Thumbs,allinone_bannerWithPlaylist_container,thumbsHolder_Thumb,thumbMarginTop,allinone_bannerWithPlaylist_thumbsHolder,allinone_bannerWithPlaylist_sliderVertical,imgs)},options.autoPlay*1000);
				}
			});
			
			/*//a href
			allinone_bannerWithPlaylist_container.click(function() {
				alert("a");
			
			});*/
			
			
			
			
			
			//controllers
			allinone_bannerWithPlaylist_leftNav.click(function() {
				if (!current_obj.effectIsRunning) {
					//mouseOverBanner=false;
					clearTimeout(timeoutID);
					allinone_bannerWithPlaylist_navigation(-1,current_obj,options,total_images,thumbsHolder_Thumbs,allinone_bannerWithPlaylist_container,thumbsHolder_Thumb,thumbMarginTop,allinone_bannerWithPlaylist_thumbsHolder,allinone_bannerWithPlaylist_sliderVertical,imgs);
				}
			});
			allinone_bannerWithPlaylist_rightNav.click(function() {
				if (!current_obj.effectIsRunning) {
					//mouseOverBanner=false;
					clearTimeout(timeoutID);
					allinone_bannerWithPlaylist_navigation(1,current_obj,options,total_images,thumbsHolder_Thumbs,allinone_bannerWithPlaylist_container,thumbsHolder_Thumb,thumbMarginTop,allinone_bannerWithPlaylist_thumbsHolder,allinone_bannerWithPlaylist_sliderVertical,imgs);
				}
			});
			
			
			
			
			
			//tumbs nav
			//var thumbsHolder_Thumbs=$(".thumbsHolder_ThumbOFF");
			var thumbsHolder_Thumbs=$('.thumbsHolder_ThumbOFF', allinone_bannerWithPlaylist_container);
			thumbsHolder_Thumbs.click(function() {
				if (!current_obj.effectIsRunning) {
					var currentBut=$(this);
					var i=currentBut.attr('rel');
					//deactivate previous 
					$(thumbsHolder_Thumbs[current_obj.current_img_no]).removeClass('thumbsHolder_ThumbON');
					
					current_obj.current_img_no=i-1;
					allinone_bannerWithPlaylist_navigation(1,current_obj,options,total_images,thumbsHolder_Thumbs,allinone_bannerWithPlaylist_container,thumbsHolder_Thumb,thumbMarginTop,allinone_bannerWithPlaylist_thumbsHolder,allinone_bannerWithPlaylist_sliderVertical,imgs);
					//alert (i+'  --  '+current_obj.current_img_no+'  --  '+total_images);
				}
			});
			
			thumbsHolder_Thumbs.mouseenter(function() {
				var currentBut=$(this);
				var i=currentBut.attr('rel');
				
				currentBut.addClass('thumbsHolder_ThumbON');
			});
			
			thumbsHolder_Thumbs.mouseleave(function() {
				var currentBut=$(this);
				var i=currentBut.attr('rel');

				if (current_obj.current_img_no!=i)
					currentBut.removeClass('thumbsHolder_ThumbON');
			});		
			


			
			
			// mouse wheel
			allinone_bannerWithPlaylist_thumbsHolderVisibleWrapper.mousewheel(function(event, delta, deltaX, deltaY) {
				event.preventDefault();
				var currentScrollVal=allinone_bannerWithPlaylist_sliderVertical.slider( "value");
				//alert (currentScrollVal+' -- '+delta);
				if ( (parseInt(currentScrollVal)>1 && parseInt(delta)==-1) || (parseInt(currentScrollVal)<100 && parseInt(delta)==1) ) {
					currentScrollVal = currentScrollVal + delta;
					allinone_bannerWithPlaylist_sliderVertical.slider( "value", currentScrollVal);
					carouselScroll(currentScrollVal,thumbsHolder_Thumb,thumbMarginTop,total_images,allinone_bannerWithPlaylist_thumbsHolder,options,current_obj,allinone_bannerWithPlaylist_sliderVertical);
					//alert (currentScrollVal);
				}
				
			});
			
			

			//first start autoplay
			$(thumbsHolder_Thumbs[current_obj.current_img_no]).addClass('thumbsHolder_ThumbON');
			if (options.autoPlay>0 && total_images>1) {
				timeoutID=setTimeout(function(){ allinone_bannerWithPlaylist_navigation(1,current_obj,options,total_images,thumbsHolder_Thumbs,allinone_bannerWithPlaylist_container,thumbsHolder_Thumb,thumbMarginTop,allinone_bannerWithPlaylist_thumbsHolder,allinone_bannerWithPlaylist_sliderVertical,imgs)},options.autoPlay*1000);
			}			
			
			
		});
	};

	//reverse effect
	$.fn.myReverse = [].reverse;
	
	//
	// plugin skins
	//
	$.fn.allinone_bannerWithPlaylist.defaults = {
			skin: 'attractive',
			width:960,
			height:384,
			randomizeImages: false,
			firstImg:0,
			numberOfStripes:20,
			numberOfRows:5,
			numberOfColumns:10,
			defaultEffect:'random',
			effectDuration:0.5,
			autoPlay:4,
			loop:true,
			showAllControllers:true,
			showNavArrows:true,
			showOnInitNavArrows:true, // o1
			autoHideNavArrows:true, // o1
			//thumbsFolder: 'images/thumbs',
			showThumbs:false,
			borderWidth: 15,
			//borderColor: '#e9e9e9',
			playlistWidth: 300,
			numberOfThumbsPerScreen:3,
			enableTouchScreen:true
	};
	


})(jQuery);




