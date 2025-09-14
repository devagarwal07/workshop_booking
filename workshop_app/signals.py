from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Profile


@receiver(post_save, sender=User)
def create_profile_for_new_user(sender, instance, created, **kwargs):
    """Automatically create a Profile for every newly created User.

    This prevents RelatedObjectDoesNotExist when code expects user.profile.

    We intentionally do NOT auto-verify email; the default profile is minimal
    and can be completed later via the existing profile completion flow.
    """
    if created:
        # Only create if it does not already exist (safety for unusual flows)
        Profile.objects.get_or_create(
            user=instance,
            defaults={
                'institute': 'Pending',
                'department': 'computer engineering',  # default choice
                'phone_number': '0000000000',          # placeholder; must update
                'position': 'coordinator',             # default role
                'is_email_verified': False,
            }
        )


@receiver(post_save, sender=User)
def ensure_profile_exists_on_save(sender, instance, created, **kwargs):
    """For legacy users saved again (e.g., admin edit), ensure Profile exists.

    This secondary handler covers cases where a User was created before this
    signal module was added. On any subsequent save (such as password change)
    we create the missing profile.
    """
    if not created:
        if not hasattr(instance, 'profile'):
            Profile.objects.get_or_create(
                user=instance,
                defaults={
                    'institute': 'Pending',
                    'department': 'computer engineering',
                    'phone_number': '0000000000',
                    'position': 'coordinator',
                    'is_email_verified': False,
                }
            )
