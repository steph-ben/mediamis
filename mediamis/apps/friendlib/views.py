from django.views.generic.simple import direct_to_template
from django.core.paginator import Paginator, InvalidPage, EmptyPage

from friendlib.forms import MediaSearchForm
from friendlib.filters import MediaFilterSet
from friendlib.models import Media, MediaRequest

def home(request):
    filter = MediaFilterSet(request.GET or None)
    qs = Media.objects.all()[:2]

    context = {
        'search_form': filter.form,
        'lastmedia_list': qs,
        'lastevent_list': [],
    }
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

def myaccount(request):
    #TODO: how to get user's id here ?!
    user = 3

    # Medias people want to borrow from me
    wanted_medias = MediaRequest.objects.filter(borrower=user)
    # Medias I want to borrow
    requested_medias = MediaRequest.objects.filter(media__owner=user)
    # Media search form & results
    search_context = get_search_context({'owner':user})
    
    context = {
        'wanted_medias': wanted_medias,
        'requested_medias': requested_medias
    }
    context.update(search_context)
 
    return direct_to_template(request, 'friendlib/private/index.html', context)

def add_media(request):
    context = {}
    context.update(search_context)
    return direct_to_template(request, 'friendlib/private/index.html', context)