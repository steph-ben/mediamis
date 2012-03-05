from django.conf.urls.defaults import *
from django.contrib.auth.views import logout
from django.contrib.auth.decorators import login_required
from django.views.generic.simple import redirect_to, direct_to_template
from django.core.urlresolvers import reverse

urlpatterns = patterns('',
    
#    url(r'^login/$',    redirect_to,        name='login',    kwargs={'url' :       reverse('home')}),
#    url(r'^logout/$',   logout,             name='logout',   kwargs={'next_page' : reverse('home')}),
#    url(r'^profile/$',  redirect_to,        name='profile',  kwargs={'url' :       reverse('home')}),

    url(r'^login/$',    redirect_to,        name='login',    kwargs={'url' :       '/friendlib/'}),
    url(r'^logout/$',   logout,             name='logout',   kwargs={'next_page' : '/friendlib/'}),
    url(r'^profile/$',  redirect_to,        name='profile',  kwargs={'url' :       '/friendlib/'}),
    
    url(r'^messages/$', login_required(direct_to_template), 
                                            name='messages', kwargs={'template': 'messages.html'}),
)

