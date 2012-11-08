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
    friendlib_book_1.title = u'Plouf'
    friendlib_book_1.description = u'plouf'
    friendlib_book_1.borrower = None
    friendlib_book_1.borrowed = False
    friendlib_book_1.author = u''
    friendlib_book_1.size = u''
    friendlib_book_1.nb_pages = None
    friendlib_book_1.save()

    from friendlib.models import Movie


    from friendlib.models import DVD


    from friendlib.models import Divx



    friendlib_book_1.owner = User.objects.get(id=1)
    friendlib_book_1.save()

