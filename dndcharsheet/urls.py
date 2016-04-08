from django.conf.urls import patterns, include, url

import session_csrf
session_csrf.monkeypatch()

from django.contrib import admin
admin.autodiscover()

from charsheet import views

urlpatterns = patterns('',
    # Examples:
     url(r'^$', views.IndexView.as_view(), name='index'),
     url(r'^create/', views.CharacterCreateView.as_view(), name='create'),
     url(r'^(?P<pk>[0-9]+)/$', views.CharacterDetailView.as_view(), name='detail'),
     url(r'^(?P<pk>[0-9]+)/update$', views.CharacterUpdateView.as_view(), name='update'),

    # url(r'^blog/', include('blog.urls')),
    url(r'^_ah/', include('djangae.urls')),

    # Note that by default this is also locked down with login:admin in app.yaml
    url(r'^admin/', include(admin.site.urls)),

    url(r'^csp/', include('cspreports.urls')),

    url(r'^auth/', include('djangae.contrib.gauth.urls')),
)
