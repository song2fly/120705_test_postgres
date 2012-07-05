from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'test_postgres.views.home', name='home'),
    # url(r'^test_postgres/', include('test_postgres.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    (r'^$', 'storage.views.main_page'),
    (r'^ls/$', 'storage.views.ls'),
    (r'^poster/$', 'storage.views.poster'),
    (r'^getter/$', 'storage.views.getter'),
    (r'^preview/$', 'storage.views.preview'),
    (r'upload_success/', 'storage.views.upload_success'),
)
