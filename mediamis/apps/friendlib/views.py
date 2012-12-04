import datetime
import urllib2
import json
import contextlib
import httplib

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.db.models.query_utils import Q
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.utils.decorators import method_decorator
from django.views.generic.simple import direct_to_template, redirect_to
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView
from django.conf import settings
from django.template.defaultfilters import truncatewords

from forms import MediaSearchForm, MediaRequestForm
from models import Media, MediaRequest
from models import BoardGame, Divx, Book, DVD, Movie

################################################################################
# Views for public pages

def home(request, **kwargs):
    max_items = 5
    lastbook_list = Book.objects.all().order_by('-pk').select_related()[:max_items]
    lastgames_list = BoardGame.objects.all().order_by('-pk').select_related()[:max_items]
    lastdvd_list = DVD.objects.all().order_by('-pk').select_related()[:max_items]

    context = {
        'lastbook_list': lastbook_list,
        'lastboardgame_list': lastgames_list,
        'lastdvd_list': lastdvd_list,
    }

    context.update(kwargs.get('extra_context', {}))
    return direct_to_template(request, 'friendlib/public/index.html', context)

def search(request, **kwargs):
    context = {}
    context.update(kwargs.get('extra_context', {}))
    return direct_to_template(request, 'friendlib/public/search.html', context)


################################################################################
# Additional context, through middleware

def get_search_context(my_request):
    """
    Get extra context to be added to the template for search form
    """
    items_per_page = 5
    search_form = MediaSearchForm(my_request)
    filter_qs = search_form.filter_queryset()

    # Type of view
    view_type = my_request.get('view_type', 'classic')
    if view_type == 'list':
        items_per_page = 20
    elif view_type == 'icon':
        items_per_page = 12
    elif view_type == 'classic':
        items_per_page = 5

    paginator = Paginator(filter_qs, items_per_page) # Show 5 per page

    # Make sure page request is an int. If not, deliver first page.
    try:
        page = int(my_request.get('page', '1'))
    except ValueError:
        page = 1

    # If page request (9999) is out of range, deliver last page of results.
    try:
        qs = paginator.page(page)
    except (EmptyPage, InvalidPage):
        qs = paginator.page(paginator.num_pages)

    context = {
        'search_form': search_form,
        'media_list': qs.object_list,
        'pager': qs,
        'view_type': view_type,
    }
    return context

def get_user_context(user):
    """
    Get extra context to display user activity and so on all pages
    when the user is logged in
    """
    user_activity = {}
    if user.is_authenticated():
        query = Q(borrower=user) | Q(media__owner=user)
        user_activity = MediaRequest.objects.filter(query).order_by('-date_status_updated').select_related()

    user_list = User.objects.all()
    nb_users = user_list.count()
    nb_medias = Media.objects.all().count()
    
    user_context = {
        'user_activity': user_activity,
        'user_list': user_list,
        'nb_users': nb_users,
        'nb_medias': nb_medias,
    }
    return user_context


################################################################################
# Views for private user pages

@login_required
def myaccount(request, **kwargs):
    MAX_OBJECTS = 5
    user = request.user.pk

    # Last stuffs ...
    inc_pending_requests = MediaRequest.objects.filter(media__owner=user, status__in=['P'])\
                            .order_by('-date_status_updated')\
                            .select_related('media__owner__username')[:MAX_OBJECTS]
    inc_accepted_requests = MediaRequest.objects.filter(media__owner=user, status__in=['A'])\
                            .order_by('-date_status_updated').select_related()[:MAX_OBJECTS]
    out_accepted_requests = MediaRequest.objects.filter(borrower=user, status__in=['A'])\
                            .order_by('-date_status_updated')\
                            .select_related()[:MAX_OBJECTS]
    last = {
        'requests_incoming_pending': inc_pending_requests,
        'requests_incoming_accepted': inc_accepted_requests,
        'requests_outgoing_accepted': out_accepted_requests,
    }
    
    # Number of Media
    counting = {
        'nb_book': Book.objects.filter(owner=user).count(),
        'nb_dvd': DVD.objects.filter(owner=user).count(),
        'nb_divx': Divx.objects.filter(owner=user).count(),
        'nb_boardgame': BoardGame.objects.filter(owner=user).count()
    }

    context = {}
    context.update(counting)
    context.update(last)

    context.update(kwargs.get('extra_context', {}))
    return direct_to_template(request, 'friendlib/private/index.html', context)

@login_required
def user_medias(request, **kwargs):
    user = request.user.pk

#   TODO: Set current user as proper filter for search
#    # Media search form & results
#    search_args = request.GET or {}
#    search_args.update({'owner':user})
#    search_context = get_search_context(search_args)

    context = {}
    context.update(kwargs.get('extra_context', {}))
    return direct_to_template(request, 'friendlib/private/medias.html', context)

@login_required
def user_requests_incoming(request, **kwargs):
    user = request.user.pk

    # Medias people want to borrow from me
    pending_requests = MediaRequest.objects.filter(media__owner=user, status__in=['P','A','B'])\
                            .order_by('-date_status_updated')\
                            .select_related('media__owner__username')
    history_requests = MediaRequest.objects.filter(media__owner=user)\
                            .order_by('-date_status_updated').select_related()

    context = {
        'requests_incoming_pending': pending_requests,
        'requests_incoming_history': history_requests
    }
    context.update(kwargs.get('extra_context', {}))
    return direct_to_template(request, 'friendlib/private/requests_incoming.html', context)

@login_required
def user_requests_outgoing(request, **kwargs):
    user = request.user.pk

    # Medias I want to borrow
    pending_requests = MediaRequest.objects.filter(borrower=user, status__in=['P','A','B'])\
                            .order_by('-date_status_updated')\
                            .select_related()
    #TODO: History = all CHANGES of this object .. check this out !
    history_requests = MediaRequest.objects.filter(borrower=user).order_by('-date_status_updated').select_related()

    context = {
        'requests_outgoing_pending': pending_requests,
        'requests_outgoing_history': history_requests
    }
    context.update(kwargs.get('extra_context', {}))
    return direct_to_template(request, 'friendlib/private/requests_outgoing.html', context)

#def add_media(request, **kwargs):
#    context = {}
#    context.update(kwargs.get('extra_context', {}))
#    return direct_to_template(request, 'friendlib/private/index.html', context)


################################################################################
# Class-based views for Medias Create/Detail/Update/Delete

class MediaCreateView(CreateView):
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        """ User need to be logged to access create form """
        return super(MediaCreateView, self).dispatch(request, *args, **kwargs)

class MediaUpdateView(UpdateView):
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        """ User need to be logged to access update form """
        return super(MediaUpdateView, self).dispatch(request, *args, **kwargs)

class MediaDeleteView(DeleteView):
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        """ User need to be logged to access delete form """
        return super(MediaDeleteView, self).dispatch(request, *args, **kwargs)

    
class MediaDetailView(DetailView):
    def post(self, request, *args, **kwargs):
        """
        Only useful because when we log-in on Media detail pages
        The request is a POST, but handled by the registration Middleware
        TODO: Maybe there's a better solution for this ?!
        """
        return self.get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(MediaDetailView, self).get_context_data(**kwargs)

        # With this we can add some stuff in template context

        # Add media requests activity
        media = self.get_object()
        media_pending_request = MediaRequest.objects.filter(media=media, status__in=['P','A','B'])\
                                    .order_by('-date_status_updated')
        media_history_request = MediaRequest.objects.filter(media=media).order_by('-date_status_updated')

        context['media_pending_request'] = media_pending_request
        context['media_history_request'] = media_history_request

        # Object can be called by {{ media }} in every templates
        context['media'] = media
        
        return context

class BookCreateView(MediaCreateView):
    def post(self, request, *args, **kwargs):
        return super(BookCreateView, self).post(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        # Set up form data from requests
        user = request.user

        # Define default form data
        specialization = '/book/'

        # Fill form with correct infos
        self.initial.update({
            'owner': user,
            'specialization_type': specialization
        })
        return super(BookCreateView, self).get(request, *args, **kwargs)

    def form_valid(self, form):
        media = form.instance
        thumb_type = form.data.get('thumbnail_type')
        thumb_url = form.data.get('thumbnail_url')
        thumb_file = form.data.get('thumbnail')
        if thumb_type == 'url':
            print "download the file here !"
            print media.thumbnail
            print media.thumbnail.field.upload_to
            print thumb_url

            from django.core.files import File
            from django.core.files.temp import NamedTemporaryFile

            img_temp = NamedTemporaryFile(dir='/tmp')
            try:
                # Set user agent, gbook doesn't like bots
                headers = { 'User-Agent' : 'Mozilla/5.0' }
                req = urllib2.Request(thumb_url, None, headers)
                con = urllib2.urlopen(req)
                img_temp.write(con.read())
            except Exception, e:
                print str(e)
            img_temp.flush()

            media.thumbnail.save('dummy', File(img_temp))

        return super(BookCreateView, self).form_valid(form)


class BookDetailView(MediaDetailView):
    pass
class BookUpdateView(MediaUpdateView):
    pass
class BookDeleteView(MediaDeleteView):
    pass

class DVDCreateView(MediaCreateView):
    pass

class BoardGameCreateView(MediaCreateView):
    pass

################################################################################
# Views and helpers to make book search from internet database (eg. Google Books, Amazone, etc.)

def book_websearch(request, **kwargs):
    """ Return a <ul> list with search result from the woueb
    Check Google Books API docs for more info
    cf. https://developers.google.com/books/docs/v1/using#st_params
    """
    DUMMY = False     # Dev offline ...
    
    GOOGLE_URL = "https://www.googleapis.com/books/v1/volumes"
    MAX_ITEMS = 5

    pagination = '<ul class="pager">'
    html = '<ul class="thumbnails">'
    page = request.POST.get('page', '0') or request.GET.get('page', '0')
    query = request.POST.get('query', None) or request.GET.get('query', None)

    ###### Generate URL #########
    if query:
        # Take care of pagination
        startIndex = 0
        maxResults = MAX_ITEMS
        page = int(page) or 0
        nextPage = page + 1
        link_next = '<a id="webresult_next" href="#" data-query="%s" data-page="%s">Next</a>' % (query, nextPage)

        if page != 0:
            # For current search
            startIndex = page * MAX_ITEMS
            previousPage = page - 1
            link_prev = '<li class="previous"><a id="webresult_prev" href="#" data-query="%s" data-page="%s">Previous</a></li>' % (query, previousPage)
            pagination += '<li class="previous">%s</li>' % link_prev

        query_url = "%s?q=%s&startIndex=%s&maxResults=%s&country=US" % (GOOGLE_URL, query, startIndex, maxResults)

        # Make it safe from ' ' and so on, cf. http://stackoverflow.com/a/845595/554374
        # TODO: handle french chars
        query_url = urllib2.quote(query_url, safe="%/:=&?~#+!$,;'@()*[]")
        print query_url


        ###### Open connexion ###########
        try:
            response = urllib2.urlopen(query_url)
            with contextlib.closing(response) as pt:
                # Decode json
                data_object = json.load(pt)
                print data_object

                items = data_object.get('items', [])
                nb_items = data_object.get('totalItems', None)
                if nb_items != None:
                    pagination += ('<li>%s items found</li>' % nb_items)
                if not items:
                    html += '<li class="media">No results.</li>'
                for r in items:
                    details = _read_gbooks_search(r)
                    if not details:
                        continue

                    html += '<li class="span2">'
                    html += '<a id="load_details" web_id="%s" href="#">' % details['web_id']
                    html += '<img src="%s" ></img>%s - %s' % \
                            (details['thumbnail'], truncatewords(details['title'], 4), truncatewords(details['authors'], 2))
                    html += '</a></li>'

        except urllib2.HTTPError, e:
            html += '<li class="media">HTTPError: %s</li>' % str(e.code)
        except urllib2.URLError, e:
            html += '<li class="media">URLError: %s</li>' % str(e.reason)
        except httplib.HTTPException, e:
            html += '<li class="media">HTTPException: %s</li>' % str(e)
        except ValueError, e:
            html += '<li class="media">ValueError: %s</li>' % str(e)
        except Exception:
            import traceback
            html += '<li class="media">generic exception: <pre>%s</pre></li>' % traceback.format_exc()

        pagination += '<li class="next">%s</li>' % link_next
    else:
        # If query empty
        html += '<li class="media">No results.</li>'

    html += '</ul>'
    pagination += '</ul>'
    html +=  pagination

    response = HttpResponse(html)
    return response

def _read_gbooks_search(r):
    """ Decode items of https://www.googleapis.com/books/v1/volumes?q=isbn:9781905686247&projection=lite
    """
    DEFAULT_PICTURE = settings.MEDIA_URL + '/img/book_default.jpg'

    infos = r.get('volumeInfo', None)
    if not infos:
        # If no title and stuff, try next entry
        return {}
    title = infos.get('title', 'Unknown')
    description = infos.get('description', None)
    authors = infos.get('authors', 'Unknown')
    if type(authors) == list:
        # Only the first one
        authors = authors[0]

    nb_pages = infos.get('pageCount', None)
    size = infos.get('dimensions', None)
    if size:
        size = str(size)

    image_links = infos.get('imageLinks', None)
    thumbnail = DEFAULT_PICTURE
    if image_links:
        thumbnail = image_links.get('thumbnail', DEFAULT_PICTURE)

    # TODO: get isbn and google identifier
    #isbn = r['volumeInfo']['industryIdentifiers']
    isbn = ''
    web_id = r.get('id', 'unknown')

    return {
        'title': title,
        'description': description,
        'nb_pages': nb_pages,
        'size': size,
        'authors': authors,
        'thumbnail': thumbnail,
        'web_id': web_id
    }

def book_websearch_detail(request, **kwargs):
    """
    Read this kind of url :  https://www.googleapis.com/books/v1/volumes/zyTCAlFPjgYC
    """
    GOOGLE_URL = "https://www.googleapis.com/books/v1/volumes/"

    print kwargs

    detail = {}
    web_id = kwargs.get('web_id', None) or request.POST.get('web_id', None) or request.GET.get('web_id', None)
    if web_id:
        url_data = GOOGLE_URL + web_id + "?country=US"

        # Use contextlib to close correctly
        # cf. http://stackoverflow.com/questions/1522636/should-i-call-close-after-urllib-urlopen/1522709#1522709
        try:
           # Set user agent, gbook doesn't like bots
            headers = { 'User-Agent' : 'Mozilla/5.0' }
            req = urllib2.Request(url_data, None, headers)
            con = urllib2.urlopen(req)
            with contextlib.closing(con) as pt:
                data_object = json.load(pt)
                print data_object
                detail = _read_gbooks_search(data_object)

                # TODO: put this in _read_gbooks_search()
                industryIds = data_object.get('industryIdentifiers', None)
                if industryIds:
                    detail.update({'isbn': str(industryIds)})

        except urllib2.HTTPError, e:
            detail = {'error': 'HTTPError: %s' % str(e.code)}
        except urllib2.URLError, e:
            detail = {'error': 'URLError: %s' % str(e.reason)}
        except httplib.HTTPException, e:
            detail = {'error': 'HTTPException: %s' % str(e)}
        except Exception:
            import traceback
            detail = {'error': 'Generic exception: %s' % traceback.format_exc()}

    s = json.dumps(detail, indent=4)
    return HttpResponse(s)
    

################################################################################
# Views to handle MediaRequest

class MediaRequestCreateView(CreateView):
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(MediaRequestCreateView, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        # Set up form data from requests
        user = request.user
        slug = kwargs.get('mediaid')
        media = get_object_or_404(Media, id=slug)

        # Define default form data
        status = 'P'
        
        # Fill form with correct infos
        self.initial.update({
            'borrower': user,
            'media': media,
            'status': status,
        })
        return super(MediaRequestCreateView, self).get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(MediaRequestCreateView, self).get_context_data(**kwargs)

        # With this we can add some stuff in template context
        context['mediaid'] = self.get_initial().get('media').pk
        return context

class MediaRequestDetailView(DetailView):
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(MediaRequestDetailView, self).dispatch(request, *args, **kwargs)

@login_required
def mediarequest_set_accepted(request, reqid, **kwargs):
    mediarequest = get_object_or_404(MediaRequest, id=reqid)
    mediarequest.status = 'A'
    mediarequest.date_answered = datetime.datetime.now()
    mediarequest.save()
    return redirect_to(request, mediarequest.get_detail_url)

@login_required
def mediarequest_set_declined(request, reqid, **kwargs):
    mediarequest = get_object_or_404(MediaRequest, id=reqid)
    mediarequest.status = 'D'
    mediarequest.date_answered = datetime.datetime.now()
    mediarequest.save()
    return redirect_to(request, mediarequest.get_detail_url)

@login_required
def mediarequest_set_borrowed(request, reqid, **kwargs):
    date_return_due = kwargs.get('date_return', None)

    mediarequest = get_object_or_404(MediaRequest, id=reqid)
    mediarequest.status = 'B'
    mediarequest.date_media_rented = datetime.datetime.now()
    if date_return_due:
        mediarequest.date_return_due = date_return_due
    mediarequest.save()

    # Update Media as well
    mediarequest.media.borrower = mediarequest.borrower
    mediarequest.media.borrowed = True
    mediarequest.media.save()

    return redirect_to(request, mediarequest.get_detail_url)

@login_required
def mediarequest_set_returned(request, reqid, **kwargs):
    mediarequest = get_object_or_404(MediaRequest, id=reqid)
    mediarequest.status = 'R'
    mediarequest.save()

    # Update Media as well
    mediarequest.media.borrower = None
    mediarequest.media.borrowed = False
    mediarequest.media.save()

    return redirect_to(request, mediarequest.get_detail_url)
