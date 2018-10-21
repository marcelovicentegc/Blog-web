from django.views.generic import TemplateView
from django.shortcuts import render


# Comment out or delete this file in production
class Error400(TemplateView):
    template_name = '400.html'

    def get(self, request):
        return render(request, self.template_name, status=400)



class Error403(TemplateView):
    template_name = '500.html'

    def get(self, request):
        return render(request, self.template_name, status=403)



class Error404(TemplateView):
    template_name = '404.html'

    def get(self, request):
        return render(request, self.template_name, status=404)



class Error500(TemplateView):
    template_name = '500.html'

    def get(self, request):
        return render(request, self.template_name, status=500)
