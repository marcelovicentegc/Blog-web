$(document).ready(function() {
    $.fn.insideFadeOut = function() {
        var front = $('#front');
        front.css('animation-name', 'fadeOut');
        front.css('animation-duration', '200ms');
        front.css('animation-timing-function', 'ease-in-out');
        front.css('animation-iteration-count', '1');
        front.css('animation-fill-mode', 'forwards');
        front.css('animation-play-state', 'running');
        front.css('animation-transition', '100ms');
    };

    $.fn.bodyFadeOut = function() {
        var body = $('body');
        body.css('animation-name', 'fadeOut');
        body.css('animation-duration', '200ms');
        body.css('animation-timing-function', 'ease-in-out');
        body.css('animation-iteration-count', '1');
        body.css('animation-fill-mode', 'forwards');
        body.css('animation-play-state', 'running');
    };

    $.fn.openBox = function(box) {
        setTimeout(function() {
            box.css('display', 'block');
        }, 200);
        box.css('animation-name', 'fadeIn');
        box.css('animation-duration', '200ms');
        box.css('animation-timing-function', 'ease-in-out');
        box.css('animation-iteration-count', '1');
        box.css('animation-direction', 'alternate');
        box.css('animation-fill-mode', 'forwards');
        box.css('animation-play-state', 'running');
    };

    $.fn.closeBox = function(box) {
        box.css('animation-name', 'fadeOut');
        box.css('animation-duration', '200ms');
        box.css('animation-timing-function', 'ease-in-out');
        box.css('animation-iteration-count', '1');
        box.css('animation-direction', 'alternate');
        box.css('animation-fill-mode', 'forwards');
        box.css('animation-play-state', 'running');
        setTimeout(function() {
            box.css('display', 'none');	
        }, 200);
    };
});

$(document).ready(function() {
    var homeButton = $('#home-button');
    var contactButton = $('#contact-button');
    var contactMenu = $('#contact-menu');
    var h1 = $('h1');

    homeButton.click(function() {
        $.fn.bodyFadeOut();
        setTimeout(function() {
            window.location.href='/'},
        200);
    });

    contactButton.click(function() {
        if (contactMenu.css('display') == 'none') {
            $.fn.closeBox(h1); 
            $.fn.openBox(contactMenu); 
        } else {
            $.fn.openBox(h1);
            $.fn.closeBox(contactMenu);
        }
    });
});