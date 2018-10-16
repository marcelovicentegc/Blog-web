from django.views.generic import TemplateView
from django.shortcuts import render



class Error404(TemplateView):
    template_name = '404.html'

    def get(self, request):
        return render(request, self.template_name)



class Error500(TemplateView):
    template_name = '500.html'

    def get(self, request):
        return render(request, self.template_name)