from django.core.management.base import BaseCommand
from django.conf import settings
from cms.models import Page, Nav

HOME_TEMPLATE = """
<h1>Welcome to the Workshop Portal</h1>
<p>This is the default home page created automatically. You can edit this content in the admin under CMS > Pages.</p>
"""

class Command(BaseCommand):
    help = "Seed initial CMS home page and a basic navigation item if they do not already exist."

    def handle(self, *args, **options):
        # Create / update home page
        page_title = settings.HOME_PAGE_TITLE
        page, created = Page.objects.get_or_create(
            title=page_title,
            defaults={
                'permalink': 'home',
                'content': HOME_TEMPLATE,
            }
        )
        if created:
            self.stdout.write(self.style.SUCCESS(f"Created home page with title '{page_title}'."))
        else:
            self.stdout.write(self.style.WARNING(f"Home page '{page_title}' already exists (id={page.id})."))

        # Create navigation entry pointing to root (which redirects to page)
        nav, nav_created = Nav.objects.get_or_create(
            name='Home',
            defaults={
                'link': '/',
                'position': 1,
                'active': True,
            }
        )
        if nav_created:
            self.stdout.write(self.style.SUCCESS("Created 'Home' navigation item."))
        else:
            self.stdout.write(self.style.WARNING("'Home' navigation item already exists."))

        self.stdout.write(self.style.SUCCESS("Seeding complete."))
