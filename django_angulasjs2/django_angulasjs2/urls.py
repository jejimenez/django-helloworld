from django.conf.urls import patterns, url, include
from django_angulasjs2.views import IndexView
from rest_framework_nested import routers
from authentication.views import AccountViewSet
from django.contrib import admin

router = routers.SimpleRouter()
router.register(r'accounts', AccountViewSet)

urlpatterns = patterns(
    '',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/v1/', include(router.urls)),

    url('^.*$', IndexView.as_view(), name='index'),
)
