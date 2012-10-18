# -*- coding: latin-1 -*-

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

    def has_been_requested_by(self, user):
        b = MediaRequest.objects.filter(borrower=user, media=media)
        if b:
            return True
        else:
            return False

        
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


class MediaRequest(models.Model):
    """ Symbolize the request of one user to catch another user's Media
    Could have different status:
        - (P) Pending
        - (D) Declined
        - (A) Accepted but not borrowed yet
        - (B) Accepted and currently borrowed
        - (R) Accepted, borrowed and returned back

    TODO: If status is Accepted, Media status need to be set as "borrowed"
    """
    STATUS_CHOICES = (
        (u'P', _('Pending')),
        (u'D', _('Declined')),
        (u'A', _('Accepted but not borrowed yet')),
        (u'B', _('Currently borrowed')),
        (u'R', _('Returned'))
    )

    media = models.ForeignKey(Media, related_name='requests', blank=False, null=False)
    borrower = models.ForeignKey(User, related_name='requested_medias', blank=False, null=False)
    message = models.TextField()
    status = models.CharField(_('status'), max_length=1, blank=False,
                               choices = STATUS_CHOICES)
    date_requested = models.DateTimeField(auto_now_add=True)     # Creation of the request
    date_answered = models.DateTimeField(null=True, blank=True)      # When the owner answered yes or no
    date_media_rented = models.DateTimeField(null=True, blank=True)  # (set by owner) When the media could be rented
    date_return_due = models.DateTimeField(null=True, blank=True)    # (set by owner) When the Media has to be returned

    def __unicode__(self):
        if self.status == 'P':
            return u'%s is asking to borrow <<%s>> from %s' % (self.borrower, self.media, self.media.owner)
        elif self.status == 'D':
            return u'%s has denied <<%s>> from %s' % (self.media.owner, self.media, self.borrower)
        
        elif self.status == 'A':
            return u'%s has accepted to borrow <<%s>> to %s, but not borrowed yet' % \
                   (self.media.owner, self.media, self.borrower)
        elif self.status == 'B':
            return u'%s is currently borrowing <<%s>> from %s' % (self.borrower, self.media, self.media.owner)
        elif self.status == 'R':
            return u'%s has returned <<%s>> to %s' % (self.borrower, self.media, self.media.owner)
        else:
            return u'Error in the status ...'

    @models.permalink
    def get_absolute_url(self):
        return ('myaccount',)
   