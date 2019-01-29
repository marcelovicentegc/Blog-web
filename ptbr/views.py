from django.conf import settings
from django.views.generic import TemplateView, ListView, DetailView
from ptbr.models import MuseumModel, PostModel, TopicModel
from django.db.utils import OperationalError



class IndexView(TemplateView):
    template_name = 'ptbrindex/index.html'



class BlogListView(ListView):
    template_name = 'ptbrblog/newsfeed.html'
    model = PostModel
    queryset = PostModel.objects.order_by('-date')[:25]
    try: 
        artwork = MuseumModel.objects.latest('date')
    except OperationalError:
        pass
    except MuseumModel.DoesNotExist:
        pass
    topics = TopicModel.objects.all()

    def get_context_data(self, **kwargs):
        kwargs['post_list'] = self.queryset
        try:
            kwargs['artwork'] = self.artwork
        except AttributeError:
            pass
        kwargs['topic_list'] = self.topics
        return super(BlogListView, self).get_context_data(**kwargs)



class BlogDetailView(DetailView):
    template_name = 'ptbrblog/post.html'
    model = PostModel

