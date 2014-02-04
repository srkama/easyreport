from django.conf.urls import patterns, include, url



# Uncomment the next two lines to enable the     admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'report_easy.views.home', name='home'),
    # url(r'^report_easy/', include('report_easy.foo.urls')),

    # Uncomment the admin/doc line below to enabl   e admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:s
    # url(r'^admin/', include(admin.site.urls)),
    (r'^forum/$', include('forums.urls')),
    (r'^', include('report.urls'))


)
