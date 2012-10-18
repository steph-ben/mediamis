from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django.views.generic.simple import direct_to_template
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView

from friendlib.forms import MediaSearchForm
from friendlib.filters import MediaFilterSet
from friendlib.models import Media, MediaRequest
from friendlib.forms import MediaRequestForm

def home(request):
    media_list = Media.objects.all()[:5]
    nb_users = User.objects.all().count()
    nb_medias = Media.objects.all().count()
    search_context = get_search_context({})       # Media search form & results

    context = {
        'media_list': media_list,
        'nb_users': nb_users,
        'nb_medias': nb_medias
    }
    context.update(search_context)

    return direct_to_template(request, 'friendlib/public/index.html', context)

def _search(request):
    qs = None
    
    if not request.GET:
        form = MediaSearchForm()
    else:
        form = MediaSearchForm(request.GET)
        if form.is_valid():
            qs = form.filter_queryset()
            
    context = {
        'search_form': form,
        'media_list': qs,
    }
    return direct_to_template(request, 'friendlib/public/search.html', context)

def get_search_context(my_request):
    filter = MediaFilterSet(my_request or None)
    paginator = Paginator(filter.qs, 5) # Show 25 per page

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
        'search_form': filter.form,
        'media_list': qs.object_list,
        'pager': qs,
    }
    return context

def search(request):
    context = get_search_context(request.GET or None)
    return direct_to_template(request, 'friendlib/public/search.html', context)

@login_required
def myaccount(request):
    user = request.user.pk
    req_on_my_medias = MediaRequest.objects.filter(media__owner=user)

    # Medias people want to borrow from me
    requests_for_my_medias_pending = req_on_my_medias.filter(status='P')
    requests_ive_accepted_but_still_home = req_on_my_medias.filter(status='A', media__borrowed=False)
    requests_ive_accepted_and_borrowed = req_on_my_medias.filter(status='A', media__borrowed=True)

    # Medias I want to borrow
    requests_medias_i_want = MediaRequest.objects.filter(borrower=user, status='P')

    # Media search form & results
    search_context = get_search_context({'owner':user})
    
    context = {
        'requests_for_my_medias_pending': requests_for_my_medias_pending,
        'requests_ive_accepted_but_still_home': requests_ive_accepted_but_still_home,
        'requests_ive_accepted_and_borrowed': requests_ive_accepted_and_borrowed,
        'requests_medias_i_want': requests_medias_i_want
    }
    context.update(search_context)
 
    return direct_to_template(request, 'friendlib/private/index.html', context)

def add_media(request):
    context = {}
    context.update(search_context)
    return direct_to_template(request, 'friendlib/private/index.html', context)


#####
###TODO: How to initialize the view correctly, eg. with predefined Media, Borrower and so on
#####
class BookCreateView(CreateView):
    pass
class DVDCreateView(CreateView):
    pass
class BoardGameCreateView(CreateView):
    pass


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
    template_name = 'friendlib/snippets/mediarequest_accept.html'

class MediaRequestUpdateView(UpdateView):
    pass

#@login_required
#def mediarequest_create(request, media_id):
#    media = get_object_or_404(Media, id=media_id)
#    user = request.user
#
#    initial = {
#        'media': media,
#        'borrower': user,
#        'status': 'P',
#    }
#    form = MediaRequestForm(initial=initial)
#
#    context = {
#        'form': form
#    }
#    return direct_to_template(request, 'friendlib/private/mediarequest_create.html', context)
