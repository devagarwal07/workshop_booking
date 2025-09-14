# Create your views here.
from django.forms import model_to_dict
from django.http import Http404
from django.shortcuts import render

from cms.models import Page, Nav, SubNav
from workshop_app.views import is_email_checked, get_landing_page
from django.shortcuts import redirect


def home(request, permalink=''):
    if permalink == '':
        permalink = 'home'
    page = Page.objects.filter(permalink=permalink, active=True)
    if page.exists():
        page = page.first()
    else:
        raise Http404("The requested page does not exists")

    # If user is authenticated & email verified and this is the root/home page,
    # send them straight to their dashboard (keeps CMS page for anonymous users).
    if request.user.is_authenticated and is_email_checked(request.user) and permalink == 'home':
        return redirect(get_landing_page(request.user))
    nav_objs = Nav.objects.filter(active=True).order_by('-position')

    navs = []

    for nav in nav_objs:
        nav_obj = model_to_dict(nav)
        nav_obj['subnavs'] = nav.subnav_set.filter(
            active=True).order_by('position')
        navs.insert(-1, nav_obj)

    return render(
        request, 'cms_base.html', {'page': page, 'navs': navs}
    )
