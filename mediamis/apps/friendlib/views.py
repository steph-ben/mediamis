from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django.views.generic.simple import direct_to_template, redirect_to
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView

from friendlib.forms import MediaSearchForm
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

def search(request):
    context = get_search_context(request.GET or None)
    return direct_to_template(request, 'friendlib/public/search.html', context)

@login_required
def myaccount(request):
    user = request.user.pk

    # Medias I want to borrow
    req_iv_made = MediaRequest.objects.filter(borrower=user)
    myrequests = {
        'myrequests_pending': req_iv_made.filter(status='P'),
        'myrequests_declined': req_iv_made.filter(status='D'),
        'myrequests_accepted': req_iv_made.filter(status='A'),
        'myrequests_borrowed': req_iv_made.filter(status='B'),
        'myrequests_history': req_iv_made.filter(status='R'),
    }

    # Medias people want to borrow from me
    req_on_my_medias = MediaRequest.objects.filter(media__owner=user)
    mymedias = {
        'mymedias_pending': req_on_my_medias.filter(status='P'),
        'mymedias_declined': req_on_my_medias.filter(status='D'),
        'mymedias_accepted': req_on_my_medias.filter(status='A'),
        'mymedias_borrowed': req_on_my_medias.filter(status='B'),
        'mymedias_history': req_on_my_medias.filter(status='R'),
    }

    # Media search form & results
    search_args = request.GET or {}
    #Todo: put user as owner
    search_args.update({'owner':user})
    search_context = get_search_context(search_args)
    
    context = {}
    context.update(myrequests)
    context.update(mymedias)
    context.update(search_context)
 
    return direct_to_template(request, 'friendlib/private/index.html', context)

def add_media(request):
    context = {}
    context.update(search_context)
    return direct_to_template(request, 'friendlib/private/index.html', context)


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

class BookDetailView(DetailView):
    pass
class BookUpdateView(UpdateView):
    pass
class BookDeleteView(DeleteView):
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
    pass

class MediaRequestUpdateView(UpdateView):
    pass

@login_required
def mediarequest_set_accepted(request, reqid):
    mediarequest = get_object_or_404(MediaRequest, id=reqid)
    mediarequest.status = 'A'
    mediarequest.save()
    return redirect_to(request, '/friendlib/myaccount')

@login_required
def mediarequest_set_declined(request, reqid):
    mediarequest = get_object_or_404(MediaRequest, id=reqid)
    mediarequest.status = 'D'
    mediarequest.save()
    return redirect_to(request, '/friendlib/myaccount')

@login_required
def mediarequest_set_borrowed(request, reqid):
    mediarequest = get_object_or_404(MediaRequest, id=reqid)
    mediarequest.status = 'B'
    mediarequest.save()

    # Update Media as well
    mediarequest.media.borrower = mediarequest.borrower
    mediarequest.media.borrowed = True
    mediarequest.media.save()

    return redirect_to(request, '/friendlib/myaccount')

@login_required
def mediarequest_set_returned(request, reqid):
    mediarequest = get_object_or_404(MediaRequest, id=reqid)
    mediarequest.status = 'R'
    mediarequest.save()

    # Update Media as well
    mediarequest.media.borrower = None
    mediarequest.media.borrowed = False
    mediarequest.media.save()

    return redirect_to(request, '/friendlib/myaccount')
