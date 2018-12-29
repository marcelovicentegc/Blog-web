$(document).ready(function() {
    var blogButton = $('#blog-button');
    
    blogButton.click(function() {
        $.fn.bodyFadeOut();
        setTimeout(function() {
            window.location.href='/en/blog/'},
        200);
    });
});