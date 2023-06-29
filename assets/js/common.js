/*
 * Author: Ali Niyazi (Netita)
 * Template Name: vCard 4
 * Version: 1.1.0
*/

$(document).ready(function() {

    'use strict';

    /*-----------------------------------------------------------------
      Detect device mobile
    -------------------------------------------------------------------*/
	
    var isMobile = false; 
    if( /Android|webOS|iPhone|iPod|iPad|BlackBerry|IEMobile|Opera Mini/i.test(navigator.userAgent)) {
        $('html').addClass('touch');
        isMobile = true;
    }
    else {
        $('html').addClass('no-touch');
        isMobile = false;
    }


    /*-----------------------------------------------------------------
      Show/hide additional info
    -------------------------------------------------------------------*/

    $('.js-btn-toggle').on('click', function(e) {     
        $('.js-show').toggle('slow');
        e.preventDefault();
    });
    

    /*-----------------------------------------------------------------
      Carousel
    -------------------------------------------------------------------*/	
    
	  // Testimonials
	  $('.js-carousel-review').each(function() {
		    var testimonialsCarousel = new Swiper('.js-carousel-review', {
            slidesPerView: 2,
			      spaceBetween: 30,
			      speed: 300,
			      grabCursor: true,
			      watchOverflow: true,
            pagination: {
                el: '.swiper-pagination',
		            clickable: true
            },
			      /*autoplay: {
                delay: 5000,
            },*/
			      breakpoints: {
                580: {
					          slidesPerView: 1,
                    spaceBetween: 20
                },
                991: {
                    slidesPerView: 1
                }
            }
		    });
	  });
	
	  // Clients
	  $('.js-carousel-clients').each(function() {
		    var clientCarousel = new Swiper('.js-carousel-clients', {
            slidesPerView: 4,
			      spaceBetween: 30,
			      //loop: true,
			      grabCursor: true,
			      watchOverflow: true,
            pagination: {
                el: '.swiper-pagination',
		            clickable: true
            },
			      breakpoints: {
                320: {
                    slidesPerView: 2,
                    spaceBetween: 0
                },				
                580: {
                    slidesPerView: 3,
                    spaceBetween: 30
                },				
                991: {
                    slidesPerView: 3,
                    spaceBetween: 30
                }
            }
		    });
	  });
	
	  // Project carousel
	  $('.js-carousel-project').each(function() {
		    var projectCarousel = new Swiper('.js-carousel-project', {
            loop: true,
            slidesPerView: 'auto',
            spaceBetween: 30,
            centeredSlides: true,
			      speed: 300,
			      grabCursor: true,
			      watchOverflow: true,
            pagination: {
                el: '.swiper-pagination',
		            clickable: true
            },
			      /*autoplay: {
                delay: 5000,
            },*/
			      breakpoints: {
                580: {
					          slidesPerView: 1,
                    spaceBetween: 20
                },
                991: {
                    slidesPerView: 1
                }
            }
		    });
	  });


    /*-----------------------------------------------------------------
      Sticky sidebar
    -------------------------------------------------------------------*/

    function activeStickyKit() {
        $('.sticky-column').stick_in_parent({
            parent: '.sticky-parent'
        });

        // bootstrap col position
        $('.sticky-column')
        .on('sticky_kit:bottom', function(e) {
            $(this).parent().css('position', 'static');
        })
        .on('sticky_kit:unbottom', function(e) {
            $(this).parent().css('position', 'relative');
        });
    };
    activeStickyKit();

    function detachStickyKit() {
        $('.sticky-column').trigger("sticky_kit:detach");
    };

    //  stop sticky kit
    //  based on your window width

    var screen = 1200;

    var windowHeight, windowWidth;
    windowWidth = $(window).width();
    if ((windowWidth < screen)) {
        detachStickyKit();
    } else {
        activeStickyKit();
    }

    // windowSize
    // window resize
    function windowSize() {
        windowHeight = window.innerHeight ? window.innerHeight : $(window).height();
        windowWidth = window.innerWidth ? window.innerWidth : $(window).width();
    }
    windowSize();

    function debounce(func, wait, immediate) {
        var timeout;
        return function() {
            var context = this, args = arguments;
            var later = function() {
                timeout = null;
                if (!immediate) func.apply(context, args);
            };
            var callNow = immediate && !timeout;
            clearTimeout(timeout);
            timeout = setTimeout(later, wait);
            if (callNow) func.apply(context, args);
        };
    };

    $(window).resize(debounce(function(){
        windowSize();
        $(document.body).trigger("sticky_kit:recalc");
        if (windowWidth < screen) {
            detachStickyKit();
        } else {
            activeStickyKit();
        }
    }, 250));


    /*-----------------------------------------------------------------
      Progress bar
    -------------------------------------------------------------------*/
    
	  function progressBar() {
	      $('.progress').each(function() {
		        var ctrl = new ScrollMagic.Controller();
		        new ScrollMagic.Scene({
                triggerElement: '.progress',
	              triggerHook: 'onEnter',
	              duration: 300
            })
            .addTo(ctrl)
		        .on("enter", function (e) {
			          var progressBar = $('.progress-bar span');
                progressBar.each(function(indx){
                    $(this).css({'width': $(this).attr('aria-valuenow') + '%', 'z-index': '2'});
                });
		        });
        });
    }
	  
    progressBar(); //Init
	
    /*-----------------------------------------------------------------
      Scroll indicator
    -------------------------------------------------------------------*/
  
    function scrollIndicator() {
        $(window).on('scroll', function() {
            var wintop = $(window).scrollTop(), docheight = 
            $(document).height(), winheight = $(window).height();
 	          var scrolled = (wintop/(docheight-winheight))*100;
  	        $('.scroll-line').css('width', (scrolled + '%'));
        });
    }
	
	  scrollIndicator(); //Init
	
	
    /*-----------------------------------------------------------------
      ScrollTo
    -------------------------------------------------------------------*/
	
    function scrollToTop() {
        var $backToTop = $('.back-to-top'),
            $showBackTotop = $(window).height();
			
        $backToTop.hide();

        $(window).scroll( function() {
            var windowScrollTop = $(window).scrollTop();
            if( windowScrollTop > $showBackTotop ) {
                $backToTop.fadeIn('fast');
            } else {
                $backToTop.fadeOut('fast');
            }
        });
        
		    $backToTop.on('click', function (e) {
            e.preventDefault();
            $(' body, html ').animate( {scrollTop : 0}, 'fast' );
        });
    }
	
	  scrollToTop(); //Init


    /*-----------------------------------------------------------------
      Style background image
    -------------------------------------------------------------------*/	
  
    $('.js-image').each(function(){
        var dataImage = $(this).attr('data-image');
        $(this).css('background-image', 'url(' + dataImage + ')');
    });
    
	
    /*-----------------------------------------------------------------
      Autoresize textarea
    -------------------------------------------------------------------*/	

    $('textarea').each(function(){
        autosize(this);
    });


    /*-----------------------------------------------------------------
      Switch categories & Filter mobile
    -------------------------------------------------------------------*/	
  
    $('.select').on('click','.placeholder',function(){
        var parent = $(this).closest('.select');
        if ( ! parent.hasClass('is-open')){
            parent.addClass('is-open');
            $('.select.is-open').not(parent).removeClass('is-open');
        } else{
            parent.removeClass('is-open');
        }
    }).on('click','ul>li',function(){
        var parent = $(this).closest('.select');
        parent.removeClass('is-open').find('.placeholder').text( $(this).text() );
        parent.find('input[type=hidden]').attr('value', $(this).attr('data-value') );
	
	      $('.filter__item').removeClass('active');
	      $(this).addClass('active');
	      var selector = $(this).attr('data-filter');
		
	      $('.js-filter-container').isotope({
	          filter: selector
	      });
	      return false;	
    });


    /*-----------------------------------------------------------------
      Masonry
    -------------------------------------------------------------------*/	
	
    // Portfolio
    var $portfolioMasonry = $('.js-masonry').isotope({
        itemSelector: '.gallery-grid__item',
	      layoutMode: 'fitRows',
        percentPosition: true,
        resizable: false,
	      transitionDuration: '0.5s',
        hiddenStyle: {
            opacity: 0,
            transform: 'scale(0.001)'
        },
        visibleStyle: {
            opacity: 1,
            transform: 'scale(1)'
        },
        fitRows: {
            gutter: '.gutter-sizer'
        },	
        masonry: {
	          columnWidth: '.gallery-grid__item',
            gutter: '.gutter-sizer',
            isAnimated: true
        }
    });
  
    $portfolioMasonry.imagesLoaded().progress( function() {
        $portfolioMasonry.isotope ({
	          columnWidth: '.gallery-grid__item',
            gutter: '.gutter-sizer',
            isAnimated: true,
	          layoutMode: 'fitRows',
            resizable: false,
            fitRows: {
                gutter: '.gutter-sizer'
            }
	      });
    });
 
  
    /*-----------------------------------------------------------------
	  Tabs
    -------------------------------------------------------------------*/	
    
    // on load of the page: switch to the currently selected tab
    var hash = document.location.hash; //var hash = window.location.hash;
    var prefix = "tab_";
    if (hash) {
        $('.nav a[href="'+hash.replace(prefix,"")+'"]').tab('show');
    } 
    // Change hash for page-reload 
    $('ul.nav > li > a').on('shown.bs.tab', function (e) {
        window.location.hash = e.target.hash.replace("#", "#" + prefix);
    });

    $('a[data-bs-toggle=tab]').each(function () {
        var $this = $(this);
        $this.on('shown.bs.tab', function () {
            $portfolioMasonry.isotope ({
                itemSelector: '.gallery-grid__item',
                columnWidth: '.gallery-grid__item',
                gutter: '.gutter-sizer',
                isAnimated: true
            });
        }); //end shown
    });  //end each


    /*-----------------------------------------------------------------
      niceScroll
    -------------------------------------------------------------------*/		

    $('textarea').niceScroll({
		    horizrailenabled: false,
        cursorcolor: "#383838",
        cursorborder: '0',
        cursorwidth: '3px',
        railpadding: { top: 10, right: 2, left: 0, bottom: 10 }
	  });


    /*-----------------------------------------------------------------
      emoji add in textarea
    -------------------------------------------------------------------*/
	
    $(function() {
        $('.emoji-wrap img').on('click', function(){
            var emoji = $(this).attr('title');
            $('#commentForm').val($('#commentForm').val()+" "+emoji+" ");
        });
    });


    /*-----------------------------------------------------------------
	  mediumZoom
    -------------------------------------------------------------------*/
  
    mediumZoom('[data-zoom]', {
        margin: 30
    });

	/*-----------------------------------------------------------------
	  magnificPopup
    -------------------------------------------------------------------*/

    $('.js-open-review').magnificPopup({
        type: 'inline',
        midClick: true,
        fixedContentPos:true,
        removalDelay: 500, //delay removal by X to allow out-animation
        callbacks: {
            beforeOpen: function() {
                this.st.mainClass = this.st.el.attr('data-effect');
            }
        },
    });

    /*-----------------------------------------------------------------
      Lazyload
    -------------------------------------------------------------------*/

    lazySizes.init();

	
    /*-----------------------------------------------------------------
      Polyfill object-fit
    -------------------------------------------------------------------*/	
	
    var $someImages = $('img.cover');
    objectFitImages($someImages);
	

    /*-----------------------------------------------------------------
      Contacts form
    -------------------------------------------------------------------*/

    $("#contact-form").validator().on("submit", function (event) {
        if (event.isDefaultPrevented()) {
            formError();
            submitMSG(false, "Please fill in the form...");
        } else {
            event.preventDefault();
            submitForm();
        }
    });

    function submitForm(){
        var name = $("#nameContact").val(),
            email = $("#emailContact").val(),
            message = $("#messageContact").val();
			
        var url = "assets/php/form-contact.php";
		
        $.ajax({
            type: "POST",
            url: url,
            data: "name=" + name + "&email=" + email + "&message=" + message,
            success : function(text){
                if (text == "success"){
                    formSuccess();
                } else {
                    formError();
                    submitMSG(false,text);
                }
            }
        });
    }

    function formSuccess(){
        $("#contact-form")[0].reset();
        submitMSG(true, "Thanks! Your message has been sent.");
    }
  
    function formError(){
        $("#contactForm").removeClass().addClass('shake animated').one('webkitAnimationEnd mozAnimationEnd MSAnimationEnd oanimationend animationend', function(){
            $(this).removeClass();
        });
    }  
  
    function submitMSG(valid, msg){
		var msgClasses;
        if(valid){
            msgClasses = "validation-success";
        } else {
           msgClasses = "validation-danger";
        }
        $("#validator-contact").removeClass().addClass(msgClasses).text(msg);
    }


    /*-----------------------------------------------------------------
      PhotoSwiper
    -------------------------------------------------------------------*/

    var initPhotoSwipeFromDOM = function(gallerySelector) {
        // parse slide data (url, title, size ...) from DOM elements
        // (children of gallerySelector)
        var parseThumbnailElements = function(el) {
          var thumbElements = el.childNodes,
              numNodes = thumbElements.length,
              items = [],
              figureEl,
              linkEl,
              size,
              item;
      
          for (var i = 0; i < numNodes; i++) {
            figureEl = thumbElements[i]; // <figure> element
      
            // include only element nodes
            if (figureEl.nodeType !== 1) {
              continue;
            }
      
            linkEl = figureEl.children[0]; // <a> element
      
            size = linkEl.getAttribute("data-size").split("x");
      
            // create slide object
            item = {
              src: linkEl.getAttribute("href"),
              w: parseInt(size[0], 10),
              h: parseInt(size[1], 10)
            };
      
            if (figureEl.children.length > 1) {
              // <figcaption> content
              item.title = figureEl.children[1].innerHTML;
            }
      
            if (linkEl.children.length > 0) {
              // <img> thumbnail element, retrieving thumbnail url
              item.msrc = linkEl.children[0].getAttribute("src");
            }
      
            item.el = figureEl; // save link to element for getThumbBoundsFn
            items.push(item);
          }
      
          return items;
        };
      
        // find nearest parent element
        var closest = function closest(el, fn) {
          return el && (fn(el) ? el : closest(el.parentNode, fn));
        };
      
        // triggers when user clicks on thumbnail
        var onThumbnailsClick = function(e) {
          e = e || window.event;
          e.preventDefault ? e.preventDefault() : (e.returnValue = false);
      
          var eTarget = e.target || e.srcElement;
      
          // find root element of slide
          var clickedListItem = closest(eTarget, function(el) {
            return el.tagName && el.tagName.toUpperCase() === "FIGURE";
          });
      
          if (!clickedListItem) {
            return;
          }
      
          // find index of clicked item by looping through all child nodes
          // alternatively, you may define index via data- attribute
          var clickedGallery = clickedListItem.parentNode,
              childNodes = clickedListItem.parentNode.childNodes,
              numChildNodes = childNodes.length,
              nodeIndex = 0,
              index;
      
          for (var i = 0; i < numChildNodes; i++) {
            if (childNodes[i].nodeType !== 1) {
              continue;
            }
      
            if (childNodes[i] === clickedListItem) {
              index = nodeIndex;
              break;
            }
            nodeIndex++;
          }
      
          if (index >= 0) {
            // open PhotoSwipe if valid index found
            openPhotoSwipe(index, clickedGallery);
          }
          return false;
        };
      
        // parse picture index and gallery index from URL (#&pid=1&gid=2)
        var photoswipeParseHash = function() {
          var hash = window.location.hash.substring(1),
              params = {};
      
          if (hash.length < 5) {
            return params;
          }
      
          var vars = hash.split("&");
          for (var i = 0; i < vars.length; i++) {
            if (!vars[i]) {
              continue;
            }
            var pair = vars[i].split("=");
            if (pair.length < 2) {
              continue;
            }
            params[pair[0]] = pair[1];
          }
      
          if (params.gid) {
            params.gid = parseInt(params.gid, 10);
          }
      
          return params;
        };
      
        var openPhotoSwipe = function(
        index,
         galleryElement,
         disableAnimation,
         fromURL
        ) {
          var pswpElement = document.querySelectorAll(".pswp")[0],
              gallery,
              options,
              items;
      
          items = parseThumbnailElements(galleryElement);
          options = {
            // Buttons/elements
            closeEl: true,
            captionEl: true,
            fullscreenEl: true,
            zoomEl: true,
            shareEl: false,
            counterEl: false,
            arrowEl: true,
            preloaderEl: true,
            // define gallery index (for URL)
            galleryUID: galleryElement.getAttribute("data-pswp-uid"),
            getThumbBoundsFn: function(index) {
              // See Options -> getThumbBoundsFn section of documentation for more info
              var thumbnail = items[index].el.getElementsByTagName("img")[0], // find thumbnail
                  pageYScroll =
                  window.pageYOffset || document.documentElement.scrollTop,
                  rect = thumbnail.getBoundingClientRect();
      
              return { x: rect.left, y: rect.top + pageYScroll, w: rect.width };
            }
          };
      
          // PhotoSwipe opened from URL
          if (fromURL) {
            if (options.galleryPIDs) {
              for (var j = 0; j < items.length; j++) {
                if (items[j].pid == index) {
                  options.index = j;
                  break;
                }
              }
            } else {
              // in URL indexes start from 1
              options.index = parseInt(index, 10) - 1;
            }
          } else {
            options.index = parseInt(index, 10);
          }
      
          // exit if index not found
          if (isNaN(options.index)) {
            return;
          }
      
          if (disableAnimation) {
            options.showAnimationDuration = 0;
          }
      
          // Pass data to PhotoSwipe and initialize it
          gallery = new PhotoSwipe(pswpElement, PhotoSwipeUI_Default, items, options);
          gallery.init();
      
          gallery.listen("unbindEvents", function() {
            // The index of the current photoswipe slide
            var getCurrentIndex = gallery.getCurrentIndex();
            // Update position of the slider
            //projectCarousel.slideTo(getCurrentIndex, 0, false);
            // 2/2. Start swiper autoplay (on close - if swiper autoplay is true)
            //projectCarousel.autoplay.start();
          });
          // 2/2. Extra Code (Not from photoswipe) - swiper autoplay stop when image in zoom mode (When lightbox is open) */
          /*gallery.listen('initialZoomIn', function() {
            if(projectCarousel.autoplay.running){
                projectCarousel.autoplay.stop();
            }
          });*/
        };
      
        // loop through all gallery elements and bind events
        var galleryElements = document.querySelectorAll(gallerySelector);
      
        for (var i = 0, l = galleryElements.length; i < l; i++) {
          galleryElements[i].setAttribute("data-pswp-uid", i + 1);
          galleryElements[i].onclick = onThumbnailsClick;
        }
      
        // Parse URL and open gallery if it contains #&pid=3&gid=1
        var hashData = photoswipeParseHash();
        if (hashData.pid && hashData.gid) {
          openPhotoSwipe(hashData.pid, galleryElements[hashData.gid - 1], true, true);
        }
      };
      
      // execute above function
      initPhotoSwipeFromDOM(".project-gallery");
});