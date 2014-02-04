_author__ = 'kamal.s'
from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from report.api import PortfolioResource, UserResource
from tastypie.api import Api
from .views import *

api = Api(api_name="v1")
api.register(PortfolioResource())
api.register(UserResource())

# Uncomment the next two lines to enable the     admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
                       # Examples:
                       # url(r'^$', 'report_easy.views.home', name='home'),
                       # url(r'^report_easy/', include('report_easy.foo.urls')),

                       # Uncomment the admin/doc line below to enable admin documentation:
                       # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

                       # Uncomment the next line to enable the admin:
                       # url(r'^admin/', include(admin.site.urls)),
                       (r'^api/', include(api.urls)),
                       (r'^login/', user_login),
                       (r'^adduser/', add_user),
)