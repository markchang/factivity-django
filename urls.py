from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^$', 'Factivity.annual.views.index'),
    (r'^login/$', 'Factivity.annual.views.login_view'),
    (r'^authenticate/$', 'Factivity.annual.views.authenticate_view'),
    (r'^logout/$', 'Factivity.annual.views.logout_view'),
    (r'^add/$', 'Factivity.annual.views.add'),
    (r'^delete/(?P<activity_id>\d+)/$', 'Factivity.annual.views.delete'),
    (r'^admin/', include(admin.site.urls)),
    (r'^(?P<username>\w+)/$', 'Factivity.annual.views.user'),
 )
