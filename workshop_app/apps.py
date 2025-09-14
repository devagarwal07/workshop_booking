from __future__ import unicode_literals

from django.apps import AppConfig


class WorkshopAppConfig(AppConfig):
    name = 'workshop_app'

    def ready(self):  # noqa: D401
        """Import signal handlers."""
        from . import signals  # noqa: F401

