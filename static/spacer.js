(function($) {
    $(function() {
        $('.spacer').jcarousel({
            wrap: 'circular',
            animation: 1000,
        });
                
        $('.spacer').jcarouselAutoscroll({
            'interval': 2000,
    		'target': '+=1',
			create: $('.spacer').hover(function() {   // stop autoscroll on mousehover
                          $(this).jcarouselAutoscroll('stop');
                    },
                    function() {
                          $(this).jcarouselAutoscroll('start');
                    })
	    });
       
       
        $('.spacer-control-prev')
            .on('active.jcarouselcontrol', function() {
                $(this).removeClass('inactive');
            })
            .on('inactive.jcarouselcontrol', function() {
                $(this).addClass('inactive');
            })
            .jcarouselControl({
                target: '-=1'
            });

        $('.spacer-control-next')
            .on('active.jcarouselcontrol', function() {
                $(this).removeClass('inactive');
            })
            .on('inactive.jcarouselcontrol', function() {
                $(this).addClass('inactive');
            })
            .jcarouselControl({
                target: '+=1'
            });

        $('.spacer-pagination')
            .on('active.jcarouselpagination', 'a', function() {
                $(this).addClass('active');
            })
            .on('inactive.jcarouselpagination', 'a', function() {
                $(this).removeClass('active');
            })
            .jcarouselPagination();
    });
})(jQuery);
