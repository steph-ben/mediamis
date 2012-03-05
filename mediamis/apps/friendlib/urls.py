from django.conf.urls.defaults import *
from friendlib.views import home, search, myaccount, mymedias

urlpatterns = patterns('',
    url(r'^$', home, name="home"),
    url(r'^search/$', search, name="search"),
    url(r'^myaccount/$', myaccount, name="myaccount"),
    url(r'^myaccount/medias/$', mymedias, name="mymedias"),
    
)
"""
url(r'^books/create/$', BookCreateView.as_view(model=Book), name='book_create'),
url(r'^books/(?P<slug>[0-9A-Za-z-]+)/$',
    DetailView.as_view(model=Book, slug_field='id'), name='book_detail'),
url(r'^books/update/(?P<slug>[0-9A-Za-z-]+)/$',
    UpdateView.as_view(model=Book, slug_field='id'), name='book_update'),
url(r'^books/delete/(?P<slug>[0-9A-Za-z-]+)/$',
    DeleteView.as_view(model=Book, slug_field='id'), name='book_delete'),
"""