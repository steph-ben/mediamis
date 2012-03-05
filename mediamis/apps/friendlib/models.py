from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import ugettext_lazy as _

from djeneralize.models import BaseGeneralizationModel

class Media(BaseGeneralizationModel):
    title = models.CharField(_('title'), max_length=255)
    description = models.TextField(_('description'), blank=True)
    
    owner = models.ForeignKey(User, related_name='owned_medias')
    borrower = models.ForeignKey(User, related_name='borrowed_medias',
                                 blank=True, null=True, default=None)
    borrowed = models.BooleanField(_('borrowed'), default=False)

    def __unicode__(self):
        return u'%s: %s' % (self.title, self.description)


class Book(Media):
    author = models.CharField(_('author name'), max_length=255, null=True, blank=True)
    size = models.CharField(_('size of the book'), max_length=255, null=True, blank=True)
    nb_pages = models.PositiveIntegerField(_('number of pages'), null=True, blank=True)

    class Meta:
        specialization = 'book'

    def __unicode__(self):
        return u'%s' % self.title

    @property
    def shortDetails(self):
        return self.description

    
class Movie(Media):
    allocine_id = models.PositiveIntegerField(_('allocine id'), null=True, blank=True)

    class Meta:
        specialization = 'movie'

    def __unicode__(self):
        return u'%s' % self.title

    @property
    def shortDetails(self):
        return self.synopsis


class DVD(Movie):
    number_of_disc = models.PositiveSmallIntegerField(_('number of disc'), null=True, blank=True)

    class Meta:
        specialization = 'dwd'
        

class Divx(Movie):
    QUALITY_CHOICES = (
        (u'G', _('Good')),
        (u'B', _('Bad')),
    )
    
    quality = models.CharField(_('quality'), max_length=1, blank=True,
                               choices = QUALITY_CHOICES)

    class Meta:
        specialization = 'divx'


class BoardGame(Media):
    number_players = models.PositiveSmallIntegerField(_('number of player'), null=True, blank=True)

    class Meta:
        specialization = 'boardgame'

