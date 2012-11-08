#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file has been automatically generated, changes may be lost if you
# go and generate it again. It was generated with the following command:
# mediamis/manage.py dumpscript friendlib

import datetime
from decimal import Decimal
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import User


def run():
    from friendlib.models import BoardGame


    from friendlib.models import MediaRequest


    from friendlib.models import Media


    from friendlib.models import Book

    friendlib_book_1 = Book()
    friendlib_book_1.specialization_type = '/book/'
    friendlib_book_1.title = u'Alice au pays des merveilles'
    friendlib_book_1.description = u''
    friendlib_book_1.borrower = None
    friendlib_book_1.borrowed = False
    friendlib_book_1.author = u''
    friendlib_book_1.size = u''
    friendlib_book_1.nb_pages = None
    friendlib_book_1.owner = User.objects.get(username='steph')
    friendlib_book_1.save()

    friendlib_book_2 = Book()
    friendlib_book_2.specialization_type = '/book/'
    friendlib_book_2.title = u'Les milles et unes nuits'
    friendlib_book_2.description = u''
    friendlib_book_2.borrower = None
    friendlib_book_2.borrowed = False
    friendlib_book_2.author = u''
    friendlib_book_2.size = u''
    friendlib_book_2.nb_pages = None
    friendlib_book_2.owner = User.objects.get(username='alice')
    friendlib_book_2.save()

    friendlib_book_3 = Book()
    friendlib_book_3.specialization_type = '/book/'
    friendlib_book_3.title = u'Alicette à phuket'
    friendlib_book_3.description = u''
    friendlib_book_3.borrower = None
    friendlib_book_3.borrowed = False
    friendlib_book_3.author = u''
    friendlib_book_3.size = u''
    friendlib_book_3.nb_pages = None
    friendlib_book_3.owner = User.objects.get(username='alice')
    friendlib_book_3.save()

    friendlib_book_4 = Book()
    friendlib_book_4.specialization_type = '/book/'
    friendlib_book_4.title = u'Bernard l\'herbite'
    friendlib_book_4.description = u''
    friendlib_book_4.borrower = None
    friendlib_book_4.borrowed = False
    friendlib_book_4.author = u''
    friendlib_book_4.size = u''
    friendlib_book_4.nb_pages = None
    friendlib_book_4.owner = User.objects.get(username='steph')
    friendlib_book_4.save()

    from friendlib.models import Movie


    from friendlib.models import DVD


    from friendlib.models import Divx




