from __future__ import unicode_literals
# -*- coding: utf-8 -*-
from django.apps import AppConfig

class CompfestConfig(AppConfig):
    name = 'compfest'

    def ready(self):
        import compfest.signals
