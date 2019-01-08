$(document).ready(function() {
    $.fn.bodyFadeOut = function() {
        var body = $('body');
        body.css('animation-name', 'fadeOut');
        body.css('animation-duration', '200ms');
        body.css('animation-timing-function', 'ease-in-out');
        body.css('animation-iteration-count', '1');
        body.css('animation-fill-mode', 'forwards');
        body.css('animation-play-state', 'running');
    };
});

$(document).ready(function() { 
    var blogButton = $('#blog-button');
    var toggleContainer = $('#toggle-container');
    var lastScroll = 0;

    blogButton.click(function() {
        $.fn.bodyFadeOut();
        setTimeout(function() {
            window.location.href='/en/blog/'},
        200);
    });

    $(document).scroll(function() {
        var currentScroll = $(this).scrollTop();
        if (currentScroll > lastScroll) {
            toggleContainer.css('padding', '25px 30px');
        } else { 
            toggleContainer.css('padding', '30px');
        }
        lastScroll = currentScroll;  
    });
}); 