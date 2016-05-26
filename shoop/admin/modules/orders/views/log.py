# -*- coding: utf-8 -*-
# This file is part of Shoop.
#
# Copyright (c) 2012-2016, Shoop Ltd. All rights reserved.
#
# This source code is licensed under the AGPLv3 license found in the
# LICENSE file in the root directory of this source tree.
from django.contrib.auth import get_user_model
from django.http.response import JsonResponse
from django.utils.encoding import force_text
from django.views.generic import View

from shoop.core.models import Order, OrderLogEntry
from shoop.utils.analog import LogEntryKind
from shoop.utils.i18n import get_locally_formatted_datetime


class NewLogEntryView(View):
    """
    Create a log `note` item associated with a particular order.
    """
    def post(self, request, *args, **kwargs):
        order = Order.objects.get(pk=kwargs["pk"])
        message = request.POST["message"]
        entry = OrderLogEntry.objects.create(
            target=order,
            message=message,
            kind=LogEntryKind.NOTE,
            user=request.user,
        )

        return JsonResponse({
            "message": entry.message,
            "kind": force_text(entry.kind.label),
            "created_on": get_locally_formatted_datetime(entry.created_on),
            "user": force_text(getattr(entry.user, get_user_model().USERNAME_FIELD)),
        })
