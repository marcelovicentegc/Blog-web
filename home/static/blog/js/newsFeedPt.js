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

$(document).ready(function () {
    $.fn.closePublicationContained = function(publicationContained) {
        publicationContained.css('animation-name', 'fadeOut');
        publicationContained.css('animation-duration', '200ms');
        publicationContained.css('animation-timing-function', 'ease-in-out');
        publicationContained.css('animation-iteration-count', '1');
        publicationContained.css('animation-direction', 'alternate');
        publicationContained.css('animation-fill-mode', 'forwards');
        publicationContained.css('animation-play-state', 'running');
        setTimeout(function() {
            publicationContained.css('display', 'none');
        }, 200);
    };

    $.fn.openPublicationContained = function(publicationContained) {
        setTimeout(function() {
            publicationContained.css('display', 'block');
        }, 200);
        publicationContained.css('position', 'absolute');
        publicationContained.css('animation-name', 'fadeIn');
        publicationContained.css('animation-duration', '200ms');
        publicationContained.css('animation-timing-function', 'ease-in-out');
        publicationContained.css('animation-iteration-count', '1');
        publicationContained.css('animation-direction', 'alternate');
        publicationContained.css('animation-fill-mode', 'forwards');
        publicationContained.css('animation-play-state', 'running');
    };
});

$(document).ready(function() { 
    var toggleContainer = $('#toggle-container');
    var sideBarWrapper = $('#sidebar-wrapper');
    var toggleButton = $('#toggle-button');
    var indexButton = $('#index-button');
    var essayButton = $('.essay-title');
    var closeSidebarButton = $('.close-sidebar-button');
    var closeSidebarPostButton = $('.close-sidebar-button-post');
    var lastScroll = 0;
    var scrollLink = $('.scroll');

    toggleButton.click(function() {
        sideBarWrapper.css('right', '0px');
        toggleContainer.css('display', 'none');
    });

    indexButton.click(function() {
        $.fn.bodyFadeOut();
        setTimeout(function() {
            window.location.href='/pt-br/'},
        200);
    });

    essayButton.click(function() {
        $.fn.bodyFadeOut();
        setTimeout(function() {
            window.location.href='/pt-br/blog/{{post.id}}'},
        200);
    });

    closeSidebarButton.click(function () {
        sideBarWrapper.css('right', '-424px');
        toggleContainer.css('display', 'block');
        toggleContainer.css('width', '80px');  
        toggleContainer.css('height', '80px');  
        toggleContainer.css('padding', '25px 30px');
    });
    
    closeSidebarPostButton.click(function () {
        sideBarWrapper.css('right', '-424px');
        toggleContainer.css('display', 'block');
        toggleContainer.css('width', '80px');  
        toggleContainer.css('height', '80px');  
        toggleContainer.css('padding', '25px 30px');
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

    scrollLink.click(function(e) {
        e.preventDefault();
        $('body, html').animate({
          scrollTop: $(this.hash).offset().top
        }, 1500);
    });
});