# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.apps import AppConfig


class IdcopsConfig(AppConfig):
    name = 'idcops'
    verbose_name = "神经元管理平台"

    def ready(self):
        from idcops.lib import signals
