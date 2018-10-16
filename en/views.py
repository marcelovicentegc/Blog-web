from django.conf import settings
from django.views.generic import TemplateView, ListView, DetailView
from en.models import PostModel, TopicModel



class IndexView(TemplateView):
    template_name = 'enindex/index.html'





class BlogListView(ListView):
    template_name = 'enblog/newsfeed.html'
    posts = PostModel.objects.all()
    topics = TopicModel.objects.all()
    # paginate_by = ...
    queryset = posts.order_by('-date') # [:25]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post_list'] = self.queryset
        context['topic_list'] = self.topics
        return context






class BlogDetailView(DetailView):
    template_name = 'enblog/post.html'
    model = PostModel
