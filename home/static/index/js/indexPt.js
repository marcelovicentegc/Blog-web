$(document).ready(function() {
    var blogButton = $('#blog-button');
    
    blogButton.click(function() {
        $.fn.bodyFadeOut();
        setTimeout(function() {
            window.location.href='/pt-br/blog/'},
        200);
    });
});