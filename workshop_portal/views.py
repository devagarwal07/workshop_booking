# Django Imports
from django.shortcuts import redirect
from django.urls import reverse
from django.conf import settings

# Local Imports
from cms.models import Page
from django.db import OperationalError


def index(request):
    """Root entrypoint.
    Attempts to redirect to configured CMS home page; if the CMS tables are not yet
    migrated (fresh clone scenario) or the page does not exist, falls back to
    workshop_app index without raising OperationalError.
    """
    try:
        page_qs = Page.objects.filter(title=settings.HOME_PAGE_TITLE)
        if page_qs.exists():
            redirect_url = reverse("cms:home", args=[page_qs.first().permalink])
        else:
            redirect_url = reverse("workshop_app:index")
    except OperationalError:
        # Likely the cms app has not had migrations applied yet.
        redirect_url = reverse("workshop_app:index")
    return redirect(redirect_url)
