from django.conf import settings
from django.views.generic import TemplateView, ListView, DetailView
from en.models import MuseumModel, PostModel, TopicModel



class IndexView(TemplateView):
    template_name = 'enindex/index.html'



class BlogListView(ListView):
    template_name = 'enblog/newsfeed.html'
    model = PostModel
    queryset = PostModel.objects.order_by('-date')[:25]
    artwork = MuseumModel.objects.latest('date')
    topics = TopicModel.objects.all()
    # paginate_by = ...

    def get_context_data(self, **kwargs):
        kwargs['post_list'] = self.queryset
        kwargs['artwork'] = self.artwork
        kwargs['topic_list'] = self.topics
        return super(BlogListView, self).get_context_data(**kwargs)




class BlogDetailView(DetailView):
    template_name = 'enblog/post.html'
    model = PostModel
