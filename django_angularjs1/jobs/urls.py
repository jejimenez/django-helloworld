from django.contrib.auth.decorators import login_required 
from django.conf.urls import include, url
from django.contrib import admin
from tastypie.api import Api
from api import JobResource
from .views import JobFormView, JobView


v1_api = Api(api_name='v1')
v1_api.register(JobResource())

urlpatterns = [
    #url(r'^login/$', 'django.contrib.auth.views.login', name='admin_login'),
    url(r'^api/', include(v1_api.urls)),
    url(r'^job-form/$',login_required(JobFormView.as_view()),name='job_form'),
    url(r'^job/$',login_required(JobView.as_view()),name='job'),
]

