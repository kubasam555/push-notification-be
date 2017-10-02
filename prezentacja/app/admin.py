# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import requests
from django.contrib import admin

# Register your models here.

from app.models import Notification


@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ['user', 'title', 'message']
    list_editable = ['title', 'message']

    def save_model(self, request, obj, form, change):
        super(NotificationAdmin, self).save_model(request, obj, form, change)
        url = 'https://fcm.googleapis.com/fcm/send'
        token = 'fhni0vSznmA:APA91bG2PCTJH8hMSzbfclAFfxqrCASqZSey2ke5e0-BzC1A5kQ54Bd-B9qclNjazEw9KGNlfWn7RkwAKNxq0Qug-YnWcYiIa7Yv1MLB_n9SSsEQqUvBCWvOdfRwRfue8vhkIF4ZDzd-'
        body = {
            'to': token,
            'notification': {
                'title': obj.title,
                'body': obj.message,
                'icon': ''
            }
        }
        headers = {
            'Authorization': 'key=AAAA2gwq5zU:APA91bHY4ic4h7CiwYbhVdEPwttDmAiQr3zFewGW8xV_PGfITQ_AkkUzDoKbRbg0lkipiSYPM6vj9u7C9xzURxoFxUYNknnSvIYSm3KUDHAshMRqZVv_qsPET-nGitQM5Em7u9tdApBd'
        }
        requests.post(url=url, json=body, headers=headers)
