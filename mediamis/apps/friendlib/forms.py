from django.forms.widgets import HiddenInput
import re

from django import forms
from django.utils.translation import ugettext_lazy as _

from django.contrib.auth.models import User
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
        (None, _('All types')),
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
    only_available = forms.BooleanField(label=_('only available media'),
                                       initial=False,
                                       required=False,
                                       help_text=_('If checked, display ' \
                                                   'only media which are ' \
                                                   'not currently on loan'))
    
    def clean_keywords(self):
        """ Clean data for field 'keywords' when submitting """
        keywords = self.cleaned_data['keywords']
        keywords = re.sub(r'\s+', ' ', keywords) # Replace multiple spaces
        return keywords
    
    def clean(self):
        """ Check form consistency, raise error to user if needed """
        return self.cleaned_data
    
    def filter_queryset(self):
        """ Filter QuerySet of Media with user selection"""
        #TODO:
        #   1) Use custom FilterSet applying for all Media models
        #   2) Use QueryJoin to join all queries

        data = self.cleaned_data
        keywords = data.get('keywords', None)

        queryset = Media.objectsAll()
        if keywords:
            queryset = queryset.filter(title__contains=keywords)
        return queryset