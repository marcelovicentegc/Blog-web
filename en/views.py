from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.views.generic import TemplateView, ListView, FormView, DetailView
from en.models import PostModel, TopicModel
#from en.static.toothbrush.scripts.toothbrush import frequency_distribution
from django.core.mail import send_mail
from django.core.paginator import Paginator



class IndexView(TemplateView):
    template_name = 'enindex/index.html'





class BlogListView(ListView):
    template_name = 'enblog/newsfeed.html'
    posts = PostModel.objects.all()
    topics = TopicModel.objects.all()
    # paginate_by = 3
    queryset = posts.order_by('-date') # [:25]
    
#    def get_queryset(self):
 #       self.postmodel = get_object_or_404(PostModel)
  #      self.topicmodel = get_object_or_404(TopicModel)
   #     return self.postmodel, self.topicmodel

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post_list'] = self.queryset
        context['topic_list'] = self.topics
        return context






class BlogDetailView(DetailView):
    template_name = 'enblog/post.html'
    model = PostModel
