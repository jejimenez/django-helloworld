from tastypie.resources import ModelResource
from .models import Seeker
from tastypie.authentication import Authentication
from tastypie.authorization import Authorization


class SeekerResource(ModelResource):
    """
    API Facet
    """
    class Meta:
        queryset = Seeker.objects.all()
        resource_name = 'seeker'
        allowed_methods = ['post', 'get', 'patch', 'delete']
        authentication = Authentication()
        authorization = Authorization()
        always_return_data = True

