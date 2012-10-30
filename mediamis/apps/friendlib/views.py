from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models.query_utils import Q
from django.shortcuts import get_object_or_404
from django.views.generic.simple import direct_to_template, redirect_to
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView

from friendlib.forms import MediaSearchForm
from friendlib.models import Media, MediaRequest
from friendlib.forms import MediaRequestForm
from friendlib.models import BoardGame, Divx, Book, DVD

################################################################################
# Views for public pages

def home(request, **kwargs):
    lastmedia_list = Media.objects.all().order_by('-pk')[:5]
    nb_users = User.objects.all().count()
    nb_medias = Media.objects.all().count()

    context = {
        'lastmedia_list': lastmedia_list,
        'nb_users': nb_users,
        'nb_medias': nb_medias,
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
        user_activity = MediaRequest.objects.filter(query).order_by('-date_status_updated')
    
    user_context = {
        'user_activity': user_activity
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
                            .order_by('-date_status_updated')
    history_requests = MediaRequest.objects.filter(media__owner=user)\
                            .order_by('-date_status_updated')

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
    pending_requests = MediaRequest.objects.filter(borrower=user, status__in=['P','A','B'])
    #TODO: History = all CHANGES of this object .. check this out !
    history_requests = MediaRequest.objects.filter(borrower=user).order_by('-date_status_updated')

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

class MediaDetailView(DetailView):
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

class BookCreateView(CreateView):
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
class BookUpdateView(UpdateView):
    pass
class BookDeleteView(DeleteView):
    pass

class DVDCreateView(CreateView):
    pass

class BoardGameCreateView(CreateView):
    pass


################################################################################
# Views to handle MediaRequest

class MediaRequestCreateView(CreateView):
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

class MediaRequestAcceptView(UpdateView):
    pass
class MediaRequestUpdateView(UpdateView):
    pass

@login_required
def mediarequest_set_accepted(request, reqid):
    mediarequest = get_object_or_404(MediaRequest, id=reqid)
    mediarequest.status = 'A'
    mediarequest.save()
    return redirect_to(request, '/friendlib/account')

@login_required
def mediarequest_set_declined(request, reqid):
    mediarequest = get_object_or_404(MediaRequest, id=reqid)
    mediarequest.status = 'D'
    mediarequest.save()
    return redirect_to(request, '/friendlib/account')

@login_required
def mediarequest_set_borrowed(request, reqid):
    mediarequest = get_object_or_404(MediaRequest, id=reqid)
    mediarequest.status = 'B'
    mediarequest.save()

    # Update Media as well
    mediarequest.media.borrower = mediarequest.borrower
    mediarequest.media.borrowed = True
    mediarequest.media.save()

    return redirect_to(request, '/friendlib/account')

@login_required
def mediarequest_set_returned(request, reqid):
    mediarequest = get_object_or_404(MediaRequest, id=reqid)
    mediarequest.status = 'R'
    mediarequest.save()

    # Update Media as well
    mediarequest.media.borrower = None
    mediarequest.media.borrowed = False
    mediarequest.media.save()

    return redirect_to(request, '/friendlib/account')
