from django.conf.urls.defaults import *

from friendlib.models import Book, MediaRequest, DVD, BoardGame
from friendlib.views import home, search, myaccount
from friendlib.views import mediarequest_set_borrowed, mediarequest_set_back
from friendlib.views import MediaRequestCreateView, MediaRequestAcceptView, MediaRequestUpdateView
from friendlib.views import BookCreateView
from friendlib.views import DVDCreateView
from friendlib.views import BoardGameCreateView
from friendlib.forms import MediaRequestForm
from friendlib.forms import MediaRequestAcceptForm

urlpatterns = patterns('',
    url(r'^$', home, name="home"),
    url(r'^search/$', search, name="search"),
    url(r'^myaccount/$', myaccount, name="myaccount"),

    url(r'requestmedia/(?P<mediaid>[0-9]+)/$',
        MediaRequestCreateView.as_view(model=MediaRequest,
                           form_class=MediaRequestForm,
                           template_name='friendlib/private/mediarequest_create.html'),
        name='mediarequest_create'),

    url(r'request/(?P<slug>[0-9]+)/accept/$',
        MediaRequestAcceptView.as_view(model=MediaRequest,
                                       slug_field='id',
                                       form_class=MediaRequestAcceptForm,
                                       template_name='friendlib/private/mediarequest_accept.html'),
        name='mediarequest_accept'
    ),
    #url(r'request/(?P<slug>[0-9]+)/deny/$',
    url(r'request/(?P<reqid>[0-9]+)/borrowed/$', mediarequest_set_borrowed, name='mediarequest_set_borrowed'),
    url(r'request/(?P<reqid>[0-9]+)/back/$', mediarequest_set_back, name='mediarequest_set_back'),



    url(r'req/(?P<slug>[0-9]+)/$',
        MediaRequestUpdateView.as_view(model=MediaRequest, slug_field='id'),
        name='mediarequest_update'),

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