# -*- coding: utf-8 -*-
import ast

from django.contrib.auth import get_user_model
from push_notifications.models import GCMDevice
from rest_framework.permissions import AllowAny
from rest_framework.response import Response


def send_push_notification_token(request):
    token = request.POST.get('token')

    GCMDevice.objects.create(
        user=get_user_model().objects.first(),
        registration_id=token
    )
    return Response(status=200)