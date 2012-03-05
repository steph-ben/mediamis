#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file has been automatically generated, changes may be lost if you
# go and generate it again. It was generated with the following command:
# ./manage.py dumpscript

import datetime
from decimal import Decimal
from django.contrib.contenttypes.models import ContentType

def run():
    from django.contrib.auth.models import Permission

    auth_permission_1 = Permission()
    auth_permission_1.name = u'Can add log entry'
    auth_permission_1.content_type = ContentType.objects.get(app_label="admin", model="logentry")
    auth_permission_1.codename = u'add_logentry'
    auth_permission_1.save()

    auth_permission_2 = Permission()
    auth_permission_2.name = u'Can change log entry'
    auth_permission_2.content_type = ContentType.objects.get(app_label="admin", model="logentry")
    auth_permission_2.codename = u'change_logentry'
    auth_permission_2.save()

    auth_permission_3 = Permission()
    auth_permission_3.name = u'Can delete log entry'
    auth_permission_3.content_type = ContentType.objects.get(app_label="admin", model="logentry")
    auth_permission_3.codename = u'delete_logentry'
    auth_permission_3.save()

    auth_permission_4 = Permission()
    auth_permission_4.name = u'Can add group'
    auth_permission_4.content_type = ContentType.objects.get(app_label="auth", model="group")
    auth_permission_4.codename = u'add_group'
    auth_permission_4.save()

    auth_permission_5 = Permission()
    auth_permission_5.name = u'Can change group'
    auth_permission_5.content_type = ContentType.objects.get(app_label="auth", model="group")
    auth_permission_5.codename = u'change_group'
    auth_permission_5.save()

    auth_permission_6 = Permission()
    auth_permission_6.name = u'Can delete group'
    auth_permission_6.content_type = ContentType.objects.get(app_label="auth", model="group")
    auth_permission_6.codename = u'delete_group'
    auth_permission_6.save()

    auth_permission_7 = Permission()
    auth_permission_7.name = u'Can add message'
    auth_permission_7.content_type = ContentType.objects.get(app_label="auth", model="message")
    auth_permission_7.codename = u'add_message'
    auth_permission_7.save()

    auth_permission_8 = Permission()
    auth_permission_8.name = u'Can change message'
    auth_permission_8.content_type = ContentType.objects.get(app_label="auth", model="message")
    auth_permission_8.codename = u'change_message'
    auth_permission_8.save()

    auth_permission_9 = Permission()
    auth_permission_9.name = u'Can delete message'
    auth_permission_9.content_type = ContentType.objects.get(app_label="auth", model="message")
    auth_permission_9.codename = u'delete_message'
    auth_permission_9.save()

    auth_permission_10 = Permission()
    auth_permission_10.name = u'Can add permission'
    auth_permission_10.content_type = ContentType.objects.get(app_label="auth", model="permission")
    auth_permission_10.codename = u'add_permission'
    auth_permission_10.save()

    auth_permission_11 = Permission()
    auth_permission_11.name = u'Can change permission'
    auth_permission_11.content_type = ContentType.objects.get(app_label="auth", model="permission")
    auth_permission_11.codename = u'change_permission'
    auth_permission_11.save()

    auth_permission_12 = Permission()
    auth_permission_12.name = u'Can delete permission'
    auth_permission_12.content_type = ContentType.objects.get(app_label="auth", model="permission")
    auth_permission_12.codename = u'delete_permission'
    auth_permission_12.save()

    auth_permission_13 = Permission()
    auth_permission_13.name = u'Can add user'
    auth_permission_13.content_type = ContentType.objects.get(app_label="auth", model="user")
    auth_permission_13.codename = u'add_user'
    auth_permission_13.save()

    auth_permission_14 = Permission()
    auth_permission_14.name = u'Can change user'
    auth_permission_14.content_type = ContentType.objects.get(app_label="auth", model="user")
    auth_permission_14.codename = u'change_user'
    auth_permission_14.save()

    auth_permission_15 = Permission()
    auth_permission_15.name = u'Can delete user'
    auth_permission_15.content_type = ContentType.objects.get(app_label="auth", model="user")
    auth_permission_15.codename = u'delete_user'
    auth_permission_15.save()

    auth_permission_16 = Permission()
    auth_permission_16.name = u'Can add content type'
    auth_permission_16.content_type = ContentType.objects.get(app_label="contenttypes", model="contenttype")
    auth_permission_16.codename = u'add_contenttype'
    auth_permission_16.save()

    auth_permission_17 = Permission()
    auth_permission_17.name = u'Can change content type'
    auth_permission_17.content_type = ContentType.objects.get(app_label="contenttypes", model="contenttype")
    auth_permission_17.codename = u'change_contenttype'
    auth_permission_17.save()

    auth_permission_18 = Permission()
    auth_permission_18.name = u'Can delete content type'
    auth_permission_18.content_type = ContentType.objects.get(app_label="contenttypes", model="contenttype")
    auth_permission_18.codename = u'delete_contenttype'
    auth_permission_18.save()

    auth_permission_19 = Permission()
    auth_permission_19.name = u'Can add board game'
    auth_permission_19.content_type = ContentType.objects.get(app_label="friendlib", model="boardgame")
    auth_permission_19.codename = u'add_boardgame'
    auth_permission_19.save()

    auth_permission_20 = Permission()
    auth_permission_20.name = u'Can change board game'
    auth_permission_20.content_type = ContentType.objects.get(app_label="friendlib", model="boardgame")
    auth_permission_20.codename = u'change_boardgame'
    auth_permission_20.save()

    auth_permission_21 = Permission()
    auth_permission_21.name = u'Can delete board game'
    auth_permission_21.content_type = ContentType.objects.get(app_label="friendlib", model="boardgame")
    auth_permission_21.codename = u'delete_boardgame'
    auth_permission_21.save()

    auth_permission_22 = Permission()
    auth_permission_22.name = u'Can add book'
    auth_permission_22.content_type = ContentType.objects.get(app_label="friendlib", model="book")
    auth_permission_22.codename = u'add_book'
    auth_permission_22.save()

    auth_permission_23 = Permission()
    auth_permission_23.name = u'Can change book'
    auth_permission_23.content_type = ContentType.objects.get(app_label="friendlib", model="book")
    auth_permission_23.codename = u'change_book'
    auth_permission_23.save()

    auth_permission_24 = Permission()
    auth_permission_24.name = u'Can delete book'
    auth_permission_24.content_type = ContentType.objects.get(app_label="friendlib", model="book")
    auth_permission_24.codename = u'delete_book'
    auth_permission_24.save()

    auth_permission_25 = Permission()
    auth_permission_25.name = u'Can add divx'
    auth_permission_25.content_type = ContentType.objects.get(app_label="friendlib", model="divx")
    auth_permission_25.codename = u'add_divx'
    auth_permission_25.save()

    auth_permission_26 = Permission()
    auth_permission_26.name = u'Can change divx'
    auth_permission_26.content_type = ContentType.objects.get(app_label="friendlib", model="divx")
    auth_permission_26.codename = u'change_divx'
    auth_permission_26.save()

    auth_permission_27 = Permission()
    auth_permission_27.name = u'Can delete divx'
    auth_permission_27.content_type = ContentType.objects.get(app_label="friendlib", model="divx")
    auth_permission_27.codename = u'delete_divx'
    auth_permission_27.save()

    auth_permission_28 = Permission()
    auth_permission_28.name = u'Can add dvd'
    auth_permission_28.content_type = ContentType.objects.get(app_label="friendlib", model="dvd")
    auth_permission_28.codename = u'add_dvd'
    auth_permission_28.save()

    auth_permission_29 = Permission()
    auth_permission_29.name = u'Can change dvd'
    auth_permission_29.content_type = ContentType.objects.get(app_label="friendlib", model="dvd")
    auth_permission_29.codename = u'change_dvd'
    auth_permission_29.save()

    auth_permission_30 = Permission()
    auth_permission_30.name = u'Can delete dvd'
    auth_permission_30.content_type = ContentType.objects.get(app_label="friendlib", model="dvd")
    auth_permission_30.codename = u'delete_dvd'
    auth_permission_30.save()

    auth_permission_31 = Permission()
    auth_permission_31.name = u'Can add media'
    auth_permission_31.content_type = ContentType.objects.get(app_label="friendlib", model="media")
    auth_permission_31.codename = u'add_media'
    auth_permission_31.save()

    auth_permission_32 = Permission()
    auth_permission_32.name = u'Can change media'
    auth_permission_32.content_type = ContentType.objects.get(app_label="friendlib", model="media")
    auth_permission_32.codename = u'change_media'
    auth_permission_32.save()

    auth_permission_33 = Permission()
    auth_permission_33.name = u'Can delete media'
    auth_permission_33.content_type = ContentType.objects.get(app_label="friendlib", model="media")
    auth_permission_33.codename = u'delete_media'
    auth_permission_33.save()

    auth_permission_34 = Permission()
    auth_permission_34.name = u'Can add movie'
    auth_permission_34.content_type = ContentType.objects.get(app_label="friendlib", model="movie")
    auth_permission_34.codename = u'add_movie'
    auth_permission_34.save()

    auth_permission_35 = Permission()
    auth_permission_35.name = u'Can change movie'
    auth_permission_35.content_type = ContentType.objects.get(app_label="friendlib", model="movie")
    auth_permission_35.codename = u'change_movie'
    auth_permission_35.save()

    auth_permission_36 = Permission()
    auth_permission_36.name = u'Can delete movie'
    auth_permission_36.content_type = ContentType.objects.get(app_label="friendlib", model="movie")
    auth_permission_36.codename = u'delete_movie'
    auth_permission_36.save()

    auth_permission_37 = Permission()
    auth_permission_37.name = u'Can add session'
    auth_permission_37.content_type = ContentType.objects.get(app_label="sessions", model="session")
    auth_permission_37.codename = u'add_session'
    auth_permission_37.save()

    auth_permission_38 = Permission()
    auth_permission_38.name = u'Can change session'
    auth_permission_38.content_type = ContentType.objects.get(app_label="sessions", model="session")
    auth_permission_38.codename = u'change_session'
    auth_permission_38.save()

    auth_permission_39 = Permission()
    auth_permission_39.name = u'Can delete session'
    auth_permission_39.content_type = ContentType.objects.get(app_label="sessions", model="session")
    auth_permission_39.codename = u'delete_session'
    auth_permission_39.save()

    auth_permission_40 = Permission()
    auth_permission_40.name = u'Can add site'
    auth_permission_40.content_type = ContentType.objects.get(app_label="sites", model="site")
    auth_permission_40.codename = u'add_site'
    auth_permission_40.save()

    auth_permission_41 = Permission()
    auth_permission_41.name = u'Can change site'
    auth_permission_41.content_type = ContentType.objects.get(app_label="sites", model="site")
    auth_permission_41.codename = u'change_site'
    auth_permission_41.save()

    auth_permission_42 = Permission()
    auth_permission_42.name = u'Can delete site'
    auth_permission_42.content_type = ContentType.objects.get(app_label="sites", model="site")
    auth_permission_42.codename = u'delete_site'
    auth_permission_42.save()

    auth_permission_43 = Permission()
    auth_permission_43.name = u'Can add migration history'
    auth_permission_43.content_type = ContentType.objects.get(app_label="south", model="migrationhistory")
    auth_permission_43.codename = u'add_migrationhistory'
    auth_permission_43.save()

    auth_permission_44 = Permission()
    auth_permission_44.name = u'Can change migration history'
    auth_permission_44.content_type = ContentType.objects.get(app_label="south", model="migrationhistory")
    auth_permission_44.codename = u'change_migrationhistory'
    auth_permission_44.save()

    auth_permission_45 = Permission()
    auth_permission_45.name = u'Can delete migration history'
    auth_permission_45.content_type = ContentType.objects.get(app_label="south", model="migrationhistory")
    auth_permission_45.codename = u'delete_migrationhistory'
    auth_permission_45.save()

    from django.contrib.auth.models import Group


    from django.contrib.auth.models import User

    auth_user_1 = User()
    auth_user_1.username = u'admin'
    auth_user_1.first_name = u''
    auth_user_1.last_name = u''
    auth_user_1.email = u'admin@admin.fr'
    auth_user_1.password = u'sha1$509de$45ec22f10561e8d3a3e2a89c71b6ec19f472bec8'
    auth_user_1.is_staff = True
    auth_user_1.is_active = True
    auth_user_1.is_superuser = True
    auth_user_1.last_login = datetime.datetime(2011, 8, 2, 7, 36, 30, 179917)
    auth_user_1.date_joined = datetime.datetime(2011, 7, 30, 12, 14, 49)
    auth_user_1.save()

    auth_user_2 = User()
    auth_user_2.username = u'steph'
    auth_user_2.first_name = u''
    auth_user_2.last_name = u''
    auth_user_2.email = u''
    auth_user_2.password = u'sha1$c017c$4a9b1d1ea8bafc5e5292252af26d3f382bc006e9'
    auth_user_2.is_staff = True
    auth_user_2.is_active = True
    auth_user_2.is_superuser = False
    auth_user_2.last_login = datetime.datetime(2011, 7, 30, 15, 24, 13, 635878)
    auth_user_2.date_joined = datetime.datetime(2011, 7, 30, 15, 20, 21)
    auth_user_2.save()

    auth_user_2.user_permissions.add(auth_permission_13)
    auth_user_2.user_permissions.add(auth_permission_14)
    auth_user_2.user_permissions.add(auth_permission_15)
    auth_user_2.user_permissions.add(auth_permission_19)
    auth_user_2.user_permissions.add(auth_permission_20)
    auth_user_2.user_permissions.add(auth_permission_21)
    auth_user_2.user_permissions.add(auth_permission_22)
    auth_user_2.user_permissions.add(auth_permission_23)
    auth_user_2.user_permissions.add(auth_permission_24)
    auth_user_2.user_permissions.add(auth_permission_25)
    auth_user_2.user_permissions.add(auth_permission_26)
    auth_user_2.user_permissions.add(auth_permission_27)
    auth_user_2.user_permissions.add(auth_permission_28)
    auth_user_2.user_permissions.add(auth_permission_29)
    auth_user_2.user_permissions.add(auth_permission_30)
    auth_user_2.user_permissions.add(auth_permission_31)
    auth_user_2.user_permissions.add(auth_permission_32)
    auth_user_2.user_permissions.add(auth_permission_33)
    auth_user_2.user_permissions.add(auth_permission_34)
    auth_user_2.user_permissions.add(auth_permission_35)
    auth_user_2.user_permissions.add(auth_permission_36)

    auth_user_3 = User()
    auth_user_3.username = u'alice'
    auth_user_3.first_name = u''
    auth_user_3.last_name = u''
    auth_user_3.email = u''
    auth_user_3.password = u'sha1$3cec6$30583ae6aeb0344fb7306f1f203739858a0dd7f5'
    auth_user_3.is_staff = True
    auth_user_3.is_active = True
    auth_user_3.is_superuser = False
    auth_user_3.last_login = datetime.datetime(2011, 8, 3, 13, 30, 33, 61992)
    auth_user_3.date_joined = datetime.datetime(2011, 7, 30, 15, 20, 29)
    auth_user_3.save()

    auth_user_3.user_permissions.add(auth_permission_13)
    auth_user_3.user_permissions.add(auth_permission_14)
    auth_user_3.user_permissions.add(auth_permission_15)
    auth_user_3.user_permissions.add(auth_permission_19)
    auth_user_3.user_permissions.add(auth_permission_20)
    auth_user_3.user_permissions.add(auth_permission_21)
    auth_user_3.user_permissions.add(auth_permission_22)
    auth_user_3.user_permissions.add(auth_permission_23)
    auth_user_3.user_permissions.add(auth_permission_24)
    auth_user_3.user_permissions.add(auth_permission_25)
    auth_user_3.user_permissions.add(auth_permission_26)
    auth_user_3.user_permissions.add(auth_permission_27)
    auth_user_3.user_permissions.add(auth_permission_28)
    auth_user_3.user_permissions.add(auth_permission_29)
    auth_user_3.user_permissions.add(auth_permission_30)
    auth_user_3.user_permissions.add(auth_permission_31)
    auth_user_3.user_permissions.add(auth_permission_32)
    auth_user_3.user_permissions.add(auth_permission_33)
    auth_user_3.user_permissions.add(auth_permission_34)
    auth_user_3.user_permissions.add(auth_permission_35)
    auth_user_3.user_permissions.add(auth_permission_36)

    auth_user_4 = User()
    auth_user_4.username = u'benji'
    auth_user_4.first_name = u''
    auth_user_4.last_name = u''
    auth_user_4.email = u''
    auth_user_4.password = u'sha1$10c06$5747bbe294a092da31ad4580292f444e5e595118'
    auth_user_4.is_staff = True
    auth_user_4.is_active = True
    auth_user_4.is_superuser = False
    auth_user_4.last_login = datetime.datetime(2011, 7, 31, 1, 29, 49, 390886)
    auth_user_4.date_joined = datetime.datetime(2011, 7, 30, 15, 20, 55)
    auth_user_4.save()

    auth_user_4.user_permissions.add(auth_permission_19)
    auth_user_4.user_permissions.add(auth_permission_20)
    auth_user_4.user_permissions.add(auth_permission_21)
    auth_user_4.user_permissions.add(auth_permission_22)
    auth_user_4.user_permissions.add(auth_permission_23)
    auth_user_4.user_permissions.add(auth_permission_24)
    auth_user_4.user_permissions.add(auth_permission_25)
    auth_user_4.user_permissions.add(auth_permission_26)
    auth_user_4.user_permissions.add(auth_permission_27)
    auth_user_4.user_permissions.add(auth_permission_28)
    auth_user_4.user_permissions.add(auth_permission_29)
    auth_user_4.user_permissions.add(auth_permission_30)
    auth_user_4.user_permissions.add(auth_permission_31)
    auth_user_4.user_permissions.add(auth_permission_32)
    auth_user_4.user_permissions.add(auth_permission_33)
    auth_user_4.user_permissions.add(auth_permission_34)
    auth_user_4.user_permissions.add(auth_permission_35)
    auth_user_4.user_permissions.add(auth_permission_36)

    from django.contrib.auth.models import Message


    """
    from django.contrib.sessions.models import Session

    django_session_1 = Session()
    django_session_1.session_key = u'2f605327687254e6d3291e8744d8366c'
    django_session_1.session_data = u'YzMwOGE1NmIyODgxMzEyY2RjMWY1ZDk0NDhmZGJhYTdhY2FhODE3NTqAAn1xAVUKdGVzdGNvb2tp\nZXECVQZ3b3JrZWRxA3Mu\n'
    django_session_1.expire_date = datetime.datetime(2011, 8, 13, 14, 38, 52, 326694)
    django_session_1.save()

    django_session_2 = Session()
    django_session_2.session_key = u'e742eb77d409b66ff2bc7e1db2c3aea8'
    django_session_2.session_data = u'OGU5NGI5ZGQ2NWZiODVmMGQ3ZGViZWU1YTcwZDA3NjRhNzI2ZmIzNzqAAn1xAShVCnRlc3Rjb29r\naWVxAlUGd29ya2VkcQNVEl9hdXRoX3VzZXJfYmFja2VuZHEEVSlkamFuZ28uY29udHJpYi5hdXRo\nLmJhY2tlbmRzLk1vZGVsQmFja2VuZHEFVQ1fYXV0aF91c2VyX2lkcQZLAXUu\n'
    django_session_2.expire_date = datetime.datetime(2011, 8, 13, 16, 14, 31, 240976)
    django_session_2.save()

    django_session_3 = Session()
    django_session_3.session_key = u'e121ec9bc7110ccd018c5954e4e3f92e'
    django_session_3.session_data = u'Y2M2OGYzNmUyNTg4ZjExMjZkNWE5MjE4NWI4MmM3YzlmMmI4NjlhMzqAAn1xAShVCnRlc3Rjb29r\naWVxAlUGd29ya2VkcQNVEl9hdXRoX3VzZXJfYmFja2VuZHEEVSlkamFuZ28uY29udHJpYi5hdXRo\nLmJhY2tlbmRzLk1vZGVsQmFja2VuZHEFVQ1fYXV0aF91c2VyX2lkcQZLBHUu\n'
    django_session_3.expire_date = datetime.datetime(2011, 8, 14, 1, 29, 49, 480522)
    django_session_3.save()

    django_session_4 = Session()
    django_session_4.session_key = u'c3ddadb75f654b7c329e97472ac70f91'
    django_session_4.session_data = u'Njc1YzE3NjFjM2QyYmFmMGU5NmI2MGU3ODUyOTZhZmQzZDdmMTgyMTqAAn1xAShVCnRlc3Rjb29r\naWVxAlUGd29ya2VkcQNVEl9hdXRoX3VzZXJfYmFja2VuZHEEVSlkamFuZ28uY29udHJpYi5hdXRo\nLmJhY2tlbmRzLk1vZGVsQmFja2VuZHEFVQ1fYXV0aF91c2VyX2lkcQZLA3Uu\n'
    django_session_4.expire_date = datetime.datetime(2011, 8, 15, 11, 18, 7, 362026)
    django_session_4.save()

    django_session_5 = Session()
    django_session_5.session_key = u'001534640548a2d6a5dc21334960e024'
    django_session_5.session_data = u'OGU5NGI5ZGQ2NWZiODVmMGQ3ZGViZWU1YTcwZDA3NjRhNzI2ZmIzNzqAAn1xAShVCnRlc3Rjb29r\naWVxAlUGd29ya2VkcQNVEl9hdXRoX3VzZXJfYmFja2VuZHEEVSlkamFuZ28uY29udHJpYi5hdXRo\nLmJhY2tlbmRzLk1vZGVsQmFja2VuZHEFVQ1fYXV0aF91c2VyX2lkcQZLAXUu\n'
    django_session_5.expire_date = datetime.datetime(2011, 8, 16, 7, 36, 30, 276712)
    django_session_5.save()

    django_session_6 = Session()
    django_session_6.session_key = u'67240ce3f821552fa576f4a81175c67c'
    django_session_6.session_data = u'Njc1YzE3NjFjM2QyYmFmMGU5NmI2MGU3ODUyOTZhZmQzZDdmMTgyMTqAAn1xAShVCnRlc3Rjb29r\naWVxAlUGd29ya2VkcQNVEl9hdXRoX3VzZXJfYmFja2VuZHEEVSlkamFuZ28uY29udHJpYi5hdXRo\nLmJhY2tlbmRzLk1vZGVsQmFja2VuZHEFVQ1fYXV0aF91c2VyX2lkcQZLA3Uu\n'
    django_session_6.expire_date = datetime.datetime(2011, 8, 17, 13, 30, 33, 156042)
    django_session_6.save()

    from django.contrib.sites.models import Site

    django_site_1 = Site()
    django_site_1.domain = u'example.com'
    django_site_1.name = u'example.com'
    django_site_1.save()

    """

    from django.contrib.admin.models import LogEntry

    django_admin_log_1 = LogEntry()
    django_admin_log_1.action_time = datetime.datetime(2011, 8, 1, 11, 19, 29, 432465)
    django_admin_log_1.user = auth_user_3
    django_admin_log_1.content_type = ContentType.objects.get(app_label="friendlib", model="book")
    django_admin_log_1.object_id = u'9'
    django_admin_log_1.object_repr = u"C'est vert et \xe7a marche"
    django_admin_log_1.action_flag = 1
    django_admin_log_1.change_message = u''
    django_admin_log_1.save()

    django_admin_log_2 = LogEntry()
    django_admin_log_2.action_time = datetime.datetime(2011, 7, 30, 15, 25, 26, 715194)
    django_admin_log_2.user = auth_user_2
    django_admin_log_2.content_type = ContentType.objects.get(app_label="friendlib", model="divx")
    django_admin_log_2.object_id = u'8'
    django_admin_log_2.object_repr = u'Un divx de pi\xe8tre qualit\xe9'
    django_admin_log_2.action_flag = 1
    django_admin_log_2.change_message = u''
    django_admin_log_2.save()

    django_admin_log_3 = LogEntry()
    django_admin_log_3.action_time = datetime.datetime(2011, 7, 30, 15, 25, 1, 37549)
    django_admin_log_3.user = auth_user_2
    django_admin_log_3.content_type = ContentType.objects.get(app_label="friendlib", model="divx")
    django_admin_log_3.object_id = u'7'
    django_admin_log_3.object_repr = u"Un bon gros divx \xe0 l'ancienne !"
    django_admin_log_3.action_flag = 1
    django_admin_log_3.change_message = u''
    django_admin_log_3.save()

    django_admin_log_4 = LogEntry()
    django_admin_log_4.action_time = datetime.datetime(2011, 7, 30, 15, 24, 2, 929999)
    django_admin_log_4.user = auth_user_1
    django_admin_log_4.content_type = ContentType.objects.get(app_label="auth", model="user")
    django_admin_log_4.object_id = u'3'
    django_admin_log_4.object_repr = u'alice'
    django_admin_log_4.action_flag = 2
    django_admin_log_4.change_message = u'Changed user_permissions.'
    django_admin_log_4.save()

    django_admin_log_5 = LogEntry()
    django_admin_log_5.action_time = datetime.datetime(2011, 7, 30, 15, 23, 45, 58043)
    django_admin_log_5.user = auth_user_1
    django_admin_log_5.content_type = ContentType.objects.get(app_label="auth", model="user")
    django_admin_log_5.object_id = u'4'
    django_admin_log_5.object_repr = u'benji'
    django_admin_log_5.action_flag = 2
    django_admin_log_5.change_message = u'No fields changed.'
    django_admin_log_5.save()

    django_admin_log_6 = LogEntry()
    django_admin_log_6.action_time = datetime.datetime(2011, 7, 30, 15, 23, 34, 377109)
    django_admin_log_6.user = auth_user_1
    django_admin_log_6.content_type = ContentType.objects.get(app_label="auth", model="user")
    django_admin_log_6.object_id = u'2'
    django_admin_log_6.object_repr = u'steph'
    django_admin_log_6.action_flag = 2
    django_admin_log_6.change_message = u'Changed is_staff.'
    django_admin_log_6.save()

    django_admin_log_7 = LogEntry()
    django_admin_log_7.action_time = datetime.datetime(2011, 7, 30, 15, 23, 26, 11247)
    django_admin_log_7.user = auth_user_1
    django_admin_log_7.content_type = ContentType.objects.get(app_label="auth", model="user")
    django_admin_log_7.object_id = u'2'
    django_admin_log_7.object_repr = u'steph'
    django_admin_log_7.action_flag = 2
    django_admin_log_7.change_message = u'Changed user_permissions.'
    django_admin_log_7.save()

    django_admin_log_8 = LogEntry()
    django_admin_log_8.action_time = datetime.datetime(2011, 7, 30, 15, 23, 3, 710155)
    django_admin_log_8.user = auth_user_1
    django_admin_log_8.content_type = ContentType.objects.get(app_label="auth", model="user")
    django_admin_log_8.object_id = u'4'
    django_admin_log_8.object_repr = u'benji'
    django_admin_log_8.action_flag = 2
    django_admin_log_8.change_message = u'Changed is_staff and user_permissions.'
    django_admin_log_8.save()

    django_admin_log_9 = LogEntry()
    django_admin_log_9.action_time = datetime.datetime(2011, 7, 30, 15, 22, 38, 607202)
    django_admin_log_9.user = auth_user_1
    django_admin_log_9.content_type = ContentType.objects.get(app_label="auth", model="user")
    django_admin_log_9.object_id = u'3'
    django_admin_log_9.object_repr = u'alice'
    django_admin_log_9.action_flag = 2
    django_admin_log_9.change_message = u'Changed is_staff.'
    django_admin_log_9.save()

    django_admin_log_10 = LogEntry()
    django_admin_log_10.action_time = datetime.datetime(2011, 7, 30, 15, 20, 55, 989965)
    django_admin_log_10.user = auth_user_1
    django_admin_log_10.content_type = ContentType.objects.get(app_label="auth", model="user")
    django_admin_log_10.object_id = u'4'
    django_admin_log_10.object_repr = u'benji'
    django_admin_log_10.action_flag = 1
    django_admin_log_10.change_message = u''
    django_admin_log_10.save()

    django_admin_log_11 = LogEntry()
    django_admin_log_11.action_time = datetime.datetime(2011, 7, 30, 15, 20, 29, 209863)
    django_admin_log_11.user = auth_user_1
    django_admin_log_11.content_type = ContentType.objects.get(app_label="auth", model="user")
    django_admin_log_11.object_id = u'3'
    django_admin_log_11.object_repr = u'alice'
    django_admin_log_11.action_flag = 1
    django_admin_log_11.change_message = u''
    django_admin_log_11.save()

    django_admin_log_12 = LogEntry()
    django_admin_log_12.action_time = datetime.datetime(2011, 7, 30, 15, 20, 21, 515118)
    django_admin_log_12.user = auth_user_1
    django_admin_log_12.content_type = ContentType.objects.get(app_label="auth", model="user")
    django_admin_log_12.object_id = u'2'
    django_admin_log_12.object_repr = u'steph'
    django_admin_log_12.action_flag = 1
    django_admin_log_12.change_message = u''
    django_admin_log_12.save()

    django_admin_log_13 = LogEntry()
    django_admin_log_13.action_time = datetime.datetime(2011, 7, 30, 12, 50, 53, 166268)
    django_admin_log_13.user = auth_user_1
    django_admin_log_13.content_type = ContentType.objects.get(app_label="friendlib", model="boardgame")
    django_admin_log_13.object_id = u'6'
    django_admin_log_13.object_repr = u'Doooble: Be fast'
    django_admin_log_13.action_flag = 1
    django_admin_log_13.change_message = u''
    django_admin_log_13.save()

    django_admin_log_14 = LogEntry()
    django_admin_log_14.action_time = datetime.datetime(2011, 7, 30, 12, 49, 54, 859698)
    django_admin_log_14.user = auth_user_1
    django_admin_log_14.content_type = ContentType.objects.get(app_label="friendlib", model="dvd")
    django_admin_log_14.object_id = u'5'
    django_admin_log_14.object_repr = u'Film-de-merde'
    django_admin_log_14.action_flag = 1
    django_admin_log_14.change_message = u''
    django_admin_log_14.save()

    django_admin_log_15 = LogEntry()
    django_admin_log_15.action_time = datetime.datetime(2011, 7, 30, 12, 49, 41, 777152)
    django_admin_log_15.user = auth_user_1
    django_admin_log_15.content_type = ContentType.objects.get(app_label="friendlib", model="dvd")
    django_admin_log_15.object_id = u'4'
    django_admin_log_15.object_repr = u'Film-de-ouf'
    django_admin_log_15.action_flag = 1
    django_admin_log_15.change_message = u''
    django_admin_log_15.save()

    django_admin_log_16 = LogEntry()
    django_admin_log_16.action_time = datetime.datetime(2011, 7, 30, 12, 48, 0, 408357)
    django_admin_log_16.user = auth_user_1
    django_admin_log_16.content_type = ContentType.objects.get(app_label="friendlib", model="book")
    django_admin_log_16.object_id = u'3'
    django_admin_log_16.object_repr = u'Alice au pays de merveilles'
    django_admin_log_16.action_flag = 1
    django_admin_log_16.change_message = u''
    django_admin_log_16.save()

    django_admin_log_17 = LogEntry()
    django_admin_log_17.action_time = datetime.datetime(2011, 7, 30, 12, 47, 44, 817660)
    django_admin_log_17.user = auth_user_1
    django_admin_log_17.content_type = ContentType.objects.get(app_label="friendlib", model="book")
    django_admin_log_17.object_id = u'2'
    django_admin_log_17.object_repr = u'Le Zahir'
    django_admin_log_17.action_flag = 1
    django_admin_log_17.change_message = u''
    django_admin_log_17.save()

    django_admin_log_18 = LogEntry()
    django_admin_log_18.action_time = datetime.datetime(2011, 7, 30, 12, 47, 33, 215524)
    django_admin_log_18.user = auth_user_1
    django_admin_log_18.content_type = ContentType.objects.get(app_label="friendlib", model="book")
    django_admin_log_18.object_id = u'1'
    django_admin_log_18.object_repr = u'mes couilles'
    django_admin_log_18.action_flag = 2
    django_admin_log_18.change_message = u'No fields changed.'
    django_admin_log_18.save()

    django_admin_log_19 = LogEntry()
    django_admin_log_19.action_time = datetime.datetime(2011, 7, 30, 12, 45, 3, 600576)
    django_admin_log_19.user = auth_user_1
    django_admin_log_19.content_type = ContentType.objects.get(app_label="friendlib", model="dvd")
    django_admin_log_19.object_id = u'2'
    django_admin_log_19.object_repr = u''
    django_admin_log_19.action_flag = 3
    django_admin_log_19.change_message = u''
    django_admin_log_19.save()

    """
    from south.models import MigrationHistory

    south_migrationhistory_1 = MigrationHistory()
    south_migrationhistory_1.app_name = u'friendlib'
    south_migrationhistory_1.migration = u'0001_initial'
    south_migrationhistory_1.applied = datetime.datetime(2011, 7, 30, 17, 28, 55, 745772)
    south_migrationhistory_1.save()

    south_migrationhistory_2 = MigrationHistory()
    south_migrationhistory_2.app_name = u'friendlib'
    south_migrationhistory_2.migration = u'0002_auto__add_field_book_nb_pages'
    south_migrationhistory_2.applied = datetime.datetime(2011, 7, 30, 17, 39, 8, 720667)
    south_migrationhistory_2.save()
    """

    from friendlib.models import Media


    from friendlib.models import Book

    friendlib_book_1 = Book()
    friendlib_book_1.specialization_type = '/book/'
    friendlib_book_1.title = u'Le Zahir'
    friendlib_book_1.description = u''
    friendlib_book_1.owner = auth_user_1
    friendlib_book_1.borrower = None
    friendlib_book_1.borrowed = False
    friendlib_book_1.nb_pages = None
    friendlib_book_1.save()

    friendlib_book_2 = Book()
    friendlib_book_2.specialization_type = '/book/'
    friendlib_book_2.title = u'Alice au pays de merveilles'
    friendlib_book_2.description = u''
    friendlib_book_2.owner = auth_user_1
    friendlib_book_2.borrower = None
    friendlib_book_2.borrowed = False
    friendlib_book_2.nb_pages = None
    friendlib_book_2.save()

    friendlib_book_3 = Book()
    friendlib_book_3.specialization_type = '/book/'
    friendlib_book_3.title = u"C'est vert et \xe7a marche"
    friendlib_book_3.description = u''
    friendlib_book_3.owner = auth_user_3
    friendlib_book_3.borrower = auth_user_2
    friendlib_book_3.borrowed = True
    friendlib_book_3.nb_pages = None
    friendlib_book_3.save()

    from friendlib.models import Movie


    from friendlib.models import DVD

    friendlib_dvd_1 = DVD()
    friendlib_dvd_1.specialization_type = '/movie/dwd/'
    friendlib_dvd_1.title = u'Film-de-ouf'
    friendlib_dvd_1.description = u''
    friendlib_dvd_1.owner = auth_user_1
    friendlib_dvd_1.borrower = None
    friendlib_dvd_1.borrowed = False
    friendlib_dvd_1.allocine_id = None
    friendlib_dvd_1.number_of_disc = None
    friendlib_dvd_1.save()

    friendlib_dvd_2 = DVD()
    friendlib_dvd_2.specialization_type = '/movie/dwd/'
    friendlib_dvd_2.title = u'Film-de-merde'
    friendlib_dvd_2.description = u''
    friendlib_dvd_2.owner = auth_user_1
    friendlib_dvd_2.borrower = None
    friendlib_dvd_2.borrowed = False
    friendlib_dvd_2.allocine_id = None
    friendlib_dvd_2.number_of_disc = None
    friendlib_dvd_2.save()

    from friendlib.models import Divx

    friendlib_divx_1 = Divx()
    friendlib_divx_1.specialization_type = '/movie/divx/'
    friendlib_divx_1.title = u"Un bon gros divx \xe0 l'ancienne !"
    friendlib_divx_1.description = u''
    friendlib_divx_1.owner = auth_user_2
    friendlib_divx_1.borrower = None
    friendlib_divx_1.borrowed = False
    friendlib_divx_1.allocine_id = None
    friendlib_divx_1.quality = u''
    friendlib_divx_1.save()

    friendlib_divx_2 = Divx()
    friendlib_divx_2.specialization_type = '/movie/divx/'
    friendlib_divx_2.title = u'Un divx de pi\xe8tre qualit\xe9'
    friendlib_divx_2.description = u"N'est-ce pas ?"
    friendlib_divx_2.owner = auth_user_2
    friendlib_divx_2.borrower = None
    friendlib_divx_2.borrowed = False
    friendlib_divx_2.allocine_id = None
    friendlib_divx_2.quality = u'B'
    friendlib_divx_2.save()

    from friendlib.models import BoardGame

    friendlib_boardgame_1 = BoardGame()
    friendlib_boardgame_1.specialization_type = '/boardgame/'
    friendlib_boardgame_1.title = u'Doooble'
    friendlib_boardgame_1.description = u'Be fast'
    friendlib_boardgame_1.owner = auth_user_1
    friendlib_boardgame_1.borrower = None
    friendlib_boardgame_1.borrowed = True
    friendlib_boardgame_1.number_players = None
    friendlib_boardgame_1.save()

