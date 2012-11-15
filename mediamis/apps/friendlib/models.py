# -*- coding: latin-1 -*-

from django.contrib.auth.models import User
from django.core import urlresolvers
from django.db import models
from django.utils.html import escape
from django.utils.translation import ugettext_lazy as _
from django.utils.safestring import mark_safe, mark_for_escaping

from djeneralize.models import BaseGeneralizationModel


class Media(BaseGeneralizationModel):
    title = models.CharField(_('title'), max_length=255)
    description = models.TextField(_('description'), blank=True)
    
    owner = models.ForeignKey(User, related_name='owned_medias')
    borrower = models.ForeignKey(User, related_name='borrowed_medias',
                                 blank=True, null=True, default=None)
    borrowed = models.BooleanField(_('borrowed'), default=False)

    def __unicode__(self):
        return u'%s' % self.title

    @models.permalink
    def get_absolute_url(self):
        return self.get_as_specialization().get_absolute_url

    @property
    def get_detail_url(self):
        url = '#'
        try:
            url = self.get_as_specialization().get_detail_url
        except:
            pass
        return url
    
    @property
    def get_update_url(self):
        url = '#'
        try:
            url = self.get_as_specialization().get_update_url
        except:
            pass
        return url

    @property
    def get_delete_url(self):
        url = '#'
        try:
            url = self.get_as_specialization().get_delete_url
        except:
            pass
        return url

    @property
    def borrowed_status(self):
        status = u"At home"
        if self.borrowed:
            status = u"Borrowed"

        return status

    @property
    def html_link(self):
        return mark_safe(self.get_as_specialization().html_link)


class Book(Media):
    author = models.CharField(_('author name'), max_length=255, null=True, blank=True)
    size = models.CharField(_('size of the book'), max_length=255, null=True, blank=True)
    nb_pages = models.PositiveIntegerField(_('number of pages'), null=True, blank=True)

    class Meta:
        specialization = 'book'

    def __unicode__(self):
        return u'%s' % self.title

    @models.permalink
    def get_absolute_url(self):
        return ('book_detail', [self.pk,])

    @property
    def get_detail_url(self):
        return urlresolvers.reverse('book_detail', args=[self.pk])
    
    @property
    def get_update_url(self):
        return urlresolvers.reverse('book_update', args=[self.pk])

    @property
    def get_delete_url(self):
        return urlresolvers.reverse('book_delete', args=[self.pk])

    @property
    def shortDetails(self):
        return self.description
    
    @property
    def html_link(self):
        html = u'<a href="%s" class="btn-link">%s</a>' % (
            self.get_absolute_url(),
            self.title.capitalize())
        return mark_safe(html)

    
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
        
    @models.permalink
    def get_absolute_url(self):
        return ('user_home',)

    @property
    def get_update_url(self):
        return urlresolvers.reverse('user_home',)

    @property
    def get_delete_url(self):
        return urlresolvers.reverse('user_home',)

    @property
    def html_link(self):
        html = u'<a href="#" class="btn-link">%s</a>' % (
            #self.get_absolute_url(),
            self.title.capitalize())
        return mark_safe(html)


class Divx(Movie):
    QUALITY_CHOICES = (
        (u'G', _('Good')),
        (u'B', _('Bad')),
    )
    
    quality = models.CharField(_('quality'), max_length=1, blank=True,
                               choices = QUALITY_CHOICES)

    class Meta:
        specialization = 'divx'

    @models.permalink
    def get_absolute_url(self):
        return ('user_home',)

    @property
    def get_update_url(self):
        return urlresolvers.reverse('user_home',)

    @property
    def get_delete_url(self):
        return urlresolvers.reverse('user_home',)

    @property
    def html_link(self):
        html = u'<a href="#" class="btn-link">%s</a>' % (
            #self.get_absolute_url(),
            self.title.capitalize())
        return mark_safe(html)


class BoardGame(Media):
    number_players = models.PositiveSmallIntegerField(_('number of player'), null=True, blank=True)

    class Meta:
        specialization = 'boardgame'

    @models.permalink
    def get_absolute_url(self):
        return ('user_home',)

    @property
    def get_update_url(self):
        return urlresolvers.reverse('user_home',)

    @property
    def get_delete_url(self):
        return urlresolvers.reverse('user_home',)

    @property
    def html_link(self):
        html = u'<a href="#" class="btn-link">%s</a>' % (
            #self.get_absolute_url(),
            self.title.capitalize())
        return mark_safe(html)


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
    date_status_updated = models.DateTimeField(auto_now=True, )    # Last update of the request
    date_requested = models.DateTimeField(auto_now_add=True)     # Creation of the request
    date_answered = models.DateTimeField(null=True, blank=True)      # When the owner answered yes or no
    date_media_rented = models.DateTimeField(null=True, blank=True)  # (set by owner) When the media could be rented
    date_return_due = models.DateTimeField(null=True, blank=True)    # (set by owner) When the Media has to be returned

    def __unicode__(self):
        label = u'Error in the status ...'
        if self.status == 'P':
            label = u'%s asks to borrow <%s> from %s' % (
                self.borrower.__unicode__().capitalize(),
                self.media,
                self.media.owner.__unicode__().capitalize())
        elif self.status == 'D':
            label = u'%s has denied <%s> from %s' % (
                self.media.owner.__unicode__().capitalize(),
                self.media,
                self.borrower.__unicode__().capitalize())
        elif self.status == 'A':
            label = u'%s has accepted to borrow <%s> to %s, but not borrowed yet' % (
                self.media.owner.__unicode__().capitalize(),
                self.media,
                self.borrower.__unicode__().capitalize())
        elif self.status == 'B':
            label = u'%s is currently borrowing <%s> from %s' % (
                self.borrower.__unicode__().capitalize(),
                self.media,
                self.media.owner.__unicode__().capitalize())
        elif self.status == 'R':
            label = u'%s has returned <%s> to %s' % (
                self.borrower.__unicode__().capitalize(),
                self.media,
                self.media.owner.__unicode__().capitalize())

        return escape(label)

    @property
    def owner_short_status(self):
        status = self.__unicode__()
        if self.status == 'P':
            status = u'%s asked to borrow' % self.borrower.__unicode__().capitalize()
        elif self.status == 'D':
            status = u'You declined.'
        elif self.status == 'A':
            status = u'You accepted.'
        elif self.status == 'B':
            status = u'You actually borrow it'
        elif self.status == 'R':
            status = u'%s returned it to you' % self.borrower.__unicode__().capitalize()
        return status

    @property
    def borrower_short_status(self):
        status = self.__unicode__()
        if self.status == 'P':
            status = u'You ask to borrow'
        elif self.status == 'D':
            status = u'Your request was denied'
        elif self.status == 'A':
            status = u'Your request was accepted. Get it now!'
        elif self.status == 'B':
            status = u'You have it at home'
        elif self.status == 'R':
            status = u'You returned it'
        return status

    def owner_activity_history(self):
        return self.activity_history(for_owner=True)

    def borrower_activity_history(self):
        return self.activity_history(for_owner=False)

    def activity_history(self, for_owner=True):
        if for_owner:
            user_owner = 'you'
            user_borrower = self.borrower.__unicode__().capitalize()
        else:
            user_owner = self.media.owner.__unicode__().capitalize()
            user_borrower = 'you'
        
        history = [{
            'date': self.date_requested,
            'label': mark_safe(u'%s asked to borrow.<br><em>%s</em>' % (user_borrower.capitalize(), self.message))
        }]

        if self.status == 'D':
            history += [{
                'date': self.date_answered,
                'label': u'%s denied to borrow to %s' % (user_owner.capitalize(), user_borrower)
            }]
        if self.status in 'RBA':
            history += [{
                'date': self.date_answered,
                'label': u'%s agreed to borrow to %s ' % (user_owner.capitalize(), user_borrower)
            }]
        if self.status in 'RB':
            label = u'%s took this media from %s.' % (user_borrower.capitalize(), user_owner)
            if self.date_return_due:
                label += u' Agreed return date was %s' % self.date_return_due

            history += [{
                'date': self.date_media_rented,
                'label': label
            }]

        if self.status in 'R':
            history += [{
                'date': self.date_status_updated,
                'label': u'%s returned it to %s.' % (user_borrower.capitalize(), user_owner)
            }]

        history.reverse()
        return history

    @models.permalink
    def get_absolute_url(self):
        return ('mediarequest_detail', [self.pk,])

    @property
    def get_detail_url(self):
        return urlresolvers.reverse('mediarequest_detail', args=[self.pk,])

    @property
    def html_link(self):
        html = u'%s (<a href="%s" class="btn-link">View</a>)' % (
            self.__unicode__(),
            self.get_detail_url)
        return mark_safe(html)

    @property
    def css_class(self):
        """
        Get a css class to show this object in a table or so
        Could be understood by Bootstrap
        """
        css_class = u''
        if self.status == 'P':
            css_class = u''
        elif self.status == 'D':
            css_class = u'error'
        elif self.status == 'A':
            css_class = u'success'
        elif self.status == 'B':
            css_class = u'warning'
        elif self.status == 'R':
            css_class = u'info'

        return css_class

    def generate_history(self):
        history_list = {}
        if self.date_requested:
            history_list.update({
                'date': self.date_requested,
                'media': self.media,
                'borrower': self.borrower,
                'status': 'P',
            })
        if self.date_answered and (self.status == 'D'):
            history_list.update({
                'date': self.date_answered,
                'media': self.media,
                'borrower': self.borrower,
                'status': 'D'
            })
        if self.date_answered and (self.status != 'D'):
            history_list.update({
                'date': self.date_answered,
                'media': self.media,
                'borrower': self.borrower,
                'status': 'A'
            })
        if self.date_answered and (self.status != 'D'):
            history_list.update({
                'date': self.date_answered,
                'media': self.media,
                'borrower': self.borrower,
                'status': 'A'
            })
            
        return history_list
