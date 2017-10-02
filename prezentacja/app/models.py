# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.


class Notification(models.Model):
    user = models.ForeignKey(get_user_model())
    title = models.CharField(max_length=255, blank=True, null=True)
    message = models.CharField(max_length=255)

    def __unicode__(self):
        return ': '.join([unicode(self.user), self.message])