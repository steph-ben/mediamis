from django.forms.widgets import HiddenInput
import re

from django import forms
from django.utils.translation import ugettext_lazy as _

from django.contrib.auth.models import User
import friendlib.models
from friendlib.models import BoardGame, DVD, Book, Media, MediaRequest


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        widgets = {
            'specialization_type': HiddenInput(),
            'owner': HiddenInput(),
            'borrower': HiddenInput(),
            'borrowed': HiddenInput(),
        }
        
class MediaRequestForm(forms.ModelForm):
    class Meta:
        model = MediaRequest
        widgets = {
            'borrower' : HiddenInput(),
            'status': HiddenInput(),
            'date_answered': HiddenInput(),
            'date_media_rented': HiddenInput(),
            'date_return_due': HiddenInput(),
        }

    def __init__(self, *args, **kwargs):
        super(MediaRequestForm, self).__init__(*args, **kwargs)

        #self.fields['datatype'].choices = choices
        #self.fields['datatype'].initial = (c[0] for c in choices)

class MediaRequestAcceptForm(forms.ModelForm):
    """
    TODO here:
      - show correct field and unmodifiables
      - widget de selection de date de retour voulu
      - pouvoir choisir entre Accept / Deny only (plus de 'Pending' possible)
    """
    #
    class Meta:
        model = MediaRequest
        widgets = {
            'borrower' : HiddenInput(),
            'date_answered': HiddenInput(),
            'date_media_rented': HiddenInput(),
        }

class MediaSearchForm(forms.Form):
    CHOICES_MEDIATYPE = (
        ('', _('All types')),
        (Book.__name__, _('Book')),
        (DVD.__name__, _('DVD')),
        (BoardGame.__name__, _('Boardgames')),
    )
    keywords = forms.CharField(label=_('keywords'), required=False)
    media_type = forms.ChoiceField(label=_('media type'), required=False,
                                   initial='',
                                   choices=CHOICES_MEDIATYPE)
    owner = forms.ModelChoiceField(label=_('owner'),
                                    queryset=User.objects.all(),
                                    empty_label=_('All users'),
                                    required=False)
#    only_available = forms.BooleanField(label=_('only available media'),
#                                       initial=False,
#                                       required=False,
#                                       help_text=_('If checked, display ' \
#                                                   'only media which are ' \
#                                                   'not currently on loan'))
    
    def clean_keywords(self):
        """ Clean data for field 'keywords' when submitting """
        keywords = self.cleaned_data['keywords']
        keywords = re.sub(r'\s+', ' ', keywords) # Replace multiple spaces
        return keywords

    def clean_media_type(self):
        media_type = self.cleaned_data['media_type']
        spec = media_type
        
        if media_type:
            #Get class object from media_type
            media_class = getattr(friendlib.models, media_type)
            spec = media_class.model_specialization

        return spec

    def filter_queryset(self):
        """ Filter QuerySet of Media with user selection"""
        #TODO:
        #   1) Use custom FilterSet applying for all Media models
        #   2) Use QueryJoin to join all queries

        self.is_valid()     # Init self.cleaned_data ...
        data = self.clean()
        keywords = data.get('keywords', None)
        owner = data.get('owner', None)
        media_type = data.get('media_type', None)

        print media_type
        
        queryset = Media.objects.all()
        if keywords:
            queryset = queryset.filter(title__contains=keywords)
        if owner:
            queryset = queryset.filter(owner=owner)
        if media_type:
            queryset = queryset.filter(specialization_type=media_type)
            
        return queryset

"""
from friendlib.forms import MediaSearchForm
f = MediaSearchForm()
f.is_valid()
f.clean()
f.filter_queryset()
"""