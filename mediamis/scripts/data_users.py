#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file has been automatically generated, changes may be lost if you
# go and generate it again. It was generated with the following command:
# mediamis/manage.py dumpscript auth.User

import datetime
from decimal import Decimal
from django.contrib.contenttypes.models import ContentType

def run():
    from django.contrib.auth.models import User

    auth_user_1 = User()
    auth_user_1.username = u'alice'
    auth_user_1.first_name = u''
    auth_user_1.last_name = u''
    auth_user_1.email = u''
    auth_user_1.password = u'sha1$9235f$5e8d6d4d61224eec4020f9ff627f41de2dab0d1b'
    auth_user_1.is_staff = False
    auth_user_1.is_active = True
    auth_user_1.is_superuser = False
    auth_user_1.last_login = datetime.datetime(2012, 11, 7, 18, 11, 56, 627668)
    auth_user_1.date_joined = datetime.datetime(2012, 10, 19, 4, 33, 45, 501602)

    auth_user_1.save()

    auth_user_2 = User()
    auth_user_2.username = u'admin'
    auth_user_2.first_name = u''
    auth_user_2.last_name = u''
    auth_user_2.email = u'admin@admin.fr'
    auth_user_2.password = u'sha1$509de$45ec22f10561e8d3a3e2a89c71b6ec19f472bec8'
    auth_user_2.is_staff = True
    auth_user_2.is_active = True
    auth_user_2.is_superuser = True
    auth_user_2.last_login = datetime.datetime(2012, 11, 7, 20, 24, 35, 821631)
    auth_user_2.date_joined = datetime.datetime(2011, 7, 30, 12, 14, 49)
    auth_user_2.save()

    auth_user_3 = User()
    auth_user_3.username = u'steph'
    auth_user_3.first_name = u''
    auth_user_3.last_name = u''
    auth_user_3.email = u''
    auth_user_3.password = u'sha1$457c2$d1ca65eae410788ab8839166f08153cb89f6366d'
    auth_user_3.is_staff = False
    auth_user_3.is_active = True
    auth_user_3.is_superuser = False
    auth_user_3.last_login = datetime.datetime(2012, 11, 7, 20, 25, 23, 952727)
    auth_user_3.date_joined = datetime.datetime(2012, 10, 19, 2, 49, 44, 681549)

    auth_user_3.save()

