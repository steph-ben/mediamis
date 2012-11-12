from django.conf.urls.defaults import patterns, include, url
from django.conf import settings

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'myfriendlylibrary.views.home', name='home'),
    url(r'^friendlib/', include('friendlib.urls')),
    url(r'^accounts/',  include('registration.urls', namespace='registration', app_name='registration')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)

if settings.SERVE_STATIC_FILES:
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$',
            'django.views.static.serve',
            dict(
                document_root = settings.MEDIA_ROOT,
                show_indexes = True
            )
        ),
        url(r'^specs/(?P<path>.*)$',
            'django.views.static.serve',
            dict(
                document_root = '../specs/',
                show_indexes = True
            )
        ),

    )

#urlpatterns += patterns('',
#(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
#)
