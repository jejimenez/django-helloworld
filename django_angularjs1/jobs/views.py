from django.shortcuts import render
from .forms import JobForm
from django.views.generic import TemplateView

class JobFormView(TemplateView):
    template_name = "jobs/index.html"

    #def get_context_data(self, **kwargs):
        #context = super(JobFormView, self).get_context_data(**kwargs)
        #context.update(JobForm=JobForm())
        #return context
        
class JobView(TemplateView):
    template_name = "jobs/new.html"

    def get_context_data(self, **kwargs):
        context = super(JobView, self).get_context_data(**kwargs)
        context.update(JobForm=JobForm())
        return context