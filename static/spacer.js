(function($) {
    $(function() {
        $('.spacer').jcarousel({
            wrap: 'circular',
        });
                
        $('.spacer').jcarouselAutoscroll({
            'interval': 1000,
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
