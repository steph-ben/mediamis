from django.conf.urls.defaults import *
from django.contrib.auth.models import User

from friendlib.models import Book, MediaRequest, DVD, BoardGame
from friendlib.views import *
from friendlib.views import home, search, myaccount
from friendlib.views import mediarequest_set_accepted, mediarequest_set_declined,\
    mediarequest_set_borrowed, mediarequest_set_returned

from friendlib.views import MediaRequestCreateView, MediaRequestDetailView
from friendlib.views import BookCreateView, BookDetailView, BookUpdateView, BookDeleteView
from friendlib.views import DVDCreateView
from friendlib.views import BoardGameCreateView
from friendlib.forms import MediaRequestForm
from friendlib.forms import MediaRequestAcceptForm, BookForm
from django.views.generic import DetailView, UpdateView

urlpatterns = patterns('',
    url(r'^$', home, name="home"),
    url(r'^search/$', search, name="search"),
    url(r'^account/$', myaccount, name="user_home"),
    url(r'^account/medias$', user_medias, name="user_medias"),
    url(r'^account/requests/incoming', user_requests_incoming, name="user_requests_incoming"),
    url(r'^account/requests/outgoing', user_requests_outgoing, name="user_requests_outgoing"),

    url(r'requestmedia/(?P<mediaid>[0-9]+)/$',
        MediaRequestCreateView.as_view(model=MediaRequest,
                           form_class=MediaRequestForm,
                           template_name='friendlib/private/mediarequest_create.html'),
        name='mediarequest_create'),
    url(r'request/(?P<slug>[0-9]+)/$',
        MediaRequestDetailView.as_view(model=MediaRequest,
                                       slug_field='id',
                                       template_name='friendlib/private/mediarequest_detail.html'),
        name='mediarequest_detail'
    ),
    url(r'request/(?P<reqid>[0-9]+)/accept/$', mediarequest_set_accepted, name='mediarequest_accept'),
    url(r'request/(?P<reqid>[0-9]+)/decline/$', mediarequest_set_declined, name='mediarequest_decline'),
    url(r'request/(?P<reqid>[0-9]+)/borrow/$', mediarequest_set_borrowed, name='mediarequest_borrow'),
    url(r'request/(?P<reqid>[0-9]+)/return/$', mediarequest_set_returned, name='mediarequest_return'),

    url(r'^users/(?P<slug>[a-zA-Z]+)/$',
        DetailView.as_view(model=User,
                           slug_field='username',
                           template_name='friendlib/user/user_detail.html'),
        name='user_detail'),
    url(r'^users/(?P<slug>[a-zA-Z]+)/edit$',
        UpdateView.as_view(model=User,
                           slug_field='username',
                           success_url='./',
                           template_name='friendlib/user/user_edit.html'),
        name='user_update'),


    url(r'^books/create/$',
        BookCreateView.as_view(model=Book,
                               form_class=BookForm,
                               template_name='friendlib/media/book/book_create.html'),
        name='book_create'),
    url(r'^books/websearch/$', book_websearch, name='book_websearch'),
    url(r'^books/websearch/(?P<web_id>[a-zA-Z0-9-]+)/$', book_websearch_detail, name='book_websearch_detail'),

    url(r'^books/(?P<pk>[0-9]+)/$',
        BookDetailView.as_view(model=Book,
                               template_name='friendlib/media/book/book_detail.html'),
        name='book_detail'),
    url(r'^books/(?P<pk>[0-9]+)/edit/$',
        BookUpdateView.as_view(model=Book,
                               form_class=BookForm,
                               template_name='friendlib/media/book/book_edit.html'),
        name='book_update'),
    url(r'^books/(?P<pk>[0-9]+)/delete/$',
        BookDeleteView.as_view(model=Book,
                               template_name='friendlib/media/book/book_confirm_delete.html',
                               success_url='/friendlib/account'),
        name='book_delete'),

    url(r'^dvds/create/$', DVDCreateView.as_view(model=DVD), name='dvd_create'),

    url(r'^boardgame/create/$', BoardGameCreateView.as_view(model=BoardGame), name='boardgame_create'),

)