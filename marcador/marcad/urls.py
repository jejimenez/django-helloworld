from django.conf.urls import url


urlpatterns = [
    url(r'^user/(?P<username>[-\w]+)/$', 'marcad.views.bookmark_user',
        name='marcador_bookmark_user'),
    url(r'^$', 'marcad.views.bookmark_list', name='marcador_bookmark_list'),
]