from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
admin.autodiscover()

urlpatterns = patterns(''
	, url(r'^admin_tools/', include('admin_tools.urls'))
    , url(r'^admin/', include(admin.site.urls))
    , url(r'^', include('cms.urls'))
    , url(r'^forms/', include('form_designer.urls'))

    , url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT, 'show_indexes': True})
    , url(r'', include('django.contrib.staticfiles.urls'))
)

urlpatterns += patterns('', (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT }))
urlpatterns += patterns('', (r'^(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.PROJECT_ROOT }))