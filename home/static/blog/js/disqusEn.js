var disqus_config = function () {
    this.page.url = 'https://marcelo.page/en/blog/{{object.id}}';
    this.page.identifier = '{{object.id}}';
    this.page.title = '{{object.title}}';
};

(function() {
    var d = document, s = d.createElement('script');
    s.src = 'https://marcelo-page.disqus.com/embed.js';
    s.setAttribute('data-timestamp', +new Date());
    (d.head || d.body).appendChild(s);
})();