from tastypie.resources import ModelResource
from .models import Job
from tastypie.authentication import Authentication
from tastypie.authorization import Authorization


class JobResource(ModelResource):
    """
    API Facet
    """
    class Meta:
        queryset = Job.objects.all()
        resource_name = 'job'
        allowed_methods = ['post', 'get', 'patch', 'delete']
        authentication = Authentication()
        authorization = Authorization()
        always_return_data = True

