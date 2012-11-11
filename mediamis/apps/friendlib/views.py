import datetime

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.db.models.query_utils import Q
from django.shortcuts import get_object_or_404
from django.utils.decorators import method_decorator
from django.views.generic.simple import direct_to_template, redirect_to
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView

from friendlib.forms import MediaSearchForm
from friendlib.models import Media, MediaRequest
from friendlib.forms import MediaRequestForm
from friendlib.models import BoardGame, Divx, Book, DVD, Movie

################################################################################
# Views for public pages

def home(request, **kwargs):
    lastbook_list = Book.objects.all().order_by('-pk').select_related()[:10]
    lastgames_list = BoardGame.objects.all().order_by('-pk').select_related()[:10]
    lastdvd_list = DVD.objects.all().order_by('-pk').select_related()[:10]
    user_list = User.objects.all()

    context = {
        'lastbook_list': lastbook_list,
        'lastboardgame_list': lastgames_list,
        'lastdvd_list': lastdvd_list,
        'user_list': user_list
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
    search_form = MediaSearchForm(my_request)
    filter_qs = search_form.filter_queryset()

    paginator = Paginator(filter_qs, 5) # Show 5 per page

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

    nb_users = User.objects.all().count()
    nb_medias = Media.objects.all().count()
    
    user_context = {
        'user_activity': user_activity,
        'nb_users': nb_users,
        'nb_medias': nb_medias,
    }
    return user_context


################################################################################
# Views for private user pages

@login_required
def myaccount(request, **kwargs):
    user = request.user.pk

    # Number of Media
    counting = {
        'nb_book': Book.objects.filter(owner=user).count(),
        'nb_dvd': DVD.objects.filter(owner=user).count(),
        'nb_divx': Divx.objects.filter(owner=user).count(),
        'nb_boardgame': BoardGame.objects.filter(owner=user).count()
    }

    context = {}
    context.update(counting)

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
    return redirect_to(request, mediarequest.get_detail_url())

@login_required
def mediarequest_set_declined(request, reqid, **kwargs):
    mediarequest = get_object_or_404(MediaRequest, id=reqid)
    mediarequest.status = 'D'
    mediarequest.date_answered = datetime.datetime.now()
    mediarequest.save()
    return redirect_to(request, mediarequest.get_detail_url())

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

    return redirect_to(request, mediarequest.get_detail_url())

@login_required
def mediarequest_set_returned(request, reqid, **kwargs):
    mediarequest = get_object_or_404(MediaRequest, id=reqid)
    mediarequest.status = 'R'
    mediarequest.save()

    # Update Media as well
    mediarequest.media.borrower = None
    mediarequest.media.borrowed = False
    mediarequest.media.save()

    return redirect_to(request, mediarequest.get_detail_url())
