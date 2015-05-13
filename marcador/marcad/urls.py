from django.conf.urls import url


urlpatterns = [
    url(r'^user/(?P<username>[-\w]+)/$', 'marcad.views.bookmark_user',name='marcador_bookmark_user'),
    url(r'^create/$', 'marcad.views.bookmark_create',name='marcador_bookmark_create'),
    url(r'^edit/(?P<pk>\d+)/$', 'marcad.views.bookmark_edit',name='marcador_bookmark_edit'),
    url(r'^$', 'marcad.views.bookmark_list', name='marcador_bookmark_list'),
]
