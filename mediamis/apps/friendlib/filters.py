import django_filters

from friendlib.models import Media, Book
from friendlib.forms import MediaSearchForm


class MediaFilterSet(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_type='contains')

    class Meta:
        model = Media
        #form = MediaSearchForm
        fields = ['title', 'description', 'owner', 'specialization_type']

