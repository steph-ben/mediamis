from django.conf.urls.defaults import *

from friendlib.models import Book, MediaRequest, DVD, BoardGame
from friendlib.views import home, search, myaccount
from friendlib.views import MediaRequestCreateView, BookCreateView
from friendlib.views import BookCreateView
from friendlib.views import DVDCreateView
from friendlib.views import BoardGameCreateView

urlpatterns = patterns('',
    url(r'^$', home, name="home"),
    url(r'^search/$', search, name="search"),
    url(r'^myaccount/$', myaccount, name="myaccount"),

    url(r'request/$', MediaRequestCreateView.as_view(model=MediaRequest), name='mediarequest_create'),

    url(r'^books/create/$', BookCreateView.as_view(model=Book), name='book_create'),

    url(r'^dvds/create/$', DVDCreateView.as_view(model=DVD), name='dvd_create'),

    url(r'^boardgame/create/$', BoardGameCreateView.as_view(model=BoardGame), name='boardgame_create'),
    
#    url(r'^books/(?P<slug>[0-9A-Za-z-]+)/$',
#        BookDetailView.as_view(model=Book, slug_field='id'), name='book_detail'),
#    url(r'^books/update/(?P<slug>[0-9A-Za-z-]+)/$',
#        BookUpdateView.as_view(model=Book, slug_field='id'), name='book_update'),
#    url(r'^books/delete/(?P<slug>[0-9A-Za-z-]+)/$',
#        BookDeleteView.as_view(model=Book, slug_field='id'), name='book_delete'),
)