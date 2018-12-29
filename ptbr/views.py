from django.conf import settings
from django.views.generic import TemplateView, ListView, DetailView
from ptbr.models import MuseumModel, PostModel, TopicModel



class IndexView(TemplateView):
    template_name = 'ptbrindex/index.html'



class BlogListView(ListView):
    template_name = 'ptbrblog/newsfeed.html'
    artwork = MuseumModel.objects.latest('date')
    topics = TopicModel.objects.all()
    posts = PostModel.objects.order_by('-date')[:25]
    # paginate_by = ...

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['artwork'] = self.artwork
        context['post_list'] = self.posts
        context['topic_list'] = self.topics
        return context



class BlogDetailView(DetailView):
    template_name = 'ptbrblog/post.html'
    model = PostModel

