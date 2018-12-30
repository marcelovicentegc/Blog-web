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
    var buttonClass = $('.button');
    var buttonEn = $('#en');
    var buttonPt = $('#pt');
    var buttonFr = $('#fr');
    var buttonEs = $('#es');
    var body = $('body');

    buttonClass.mouseover(function() {
         body.css('background-color', 'black'); 
    });

    buttonClass.mouseout(function() {
        body.css('background-color', 'white');
    })

    buttonEn.click(function() {
        $.fn.bodyFadeOut();
        setTimeout(function() {
            window.location.href='/en/'},
        200);
    });
    
    buttonPt.click(function() {
        $.fn.bodyFadeOut();
        setTimeout(function() {
            window.location.href='/pt-br/'},
        200);
    });
});