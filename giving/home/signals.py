from allauth.account.signals import user_signed_up, user_logged_in
from django.dispatch import receiver
from giving.users.models import User
from pinax.stripe.actions import customers


@receiver(user_signed_up, sender=User)
def create_stripe_customer(sender, **kwargs):
    customers.create(user=kwargs['user'])


@receiver(user_logged_in)
def is_it_working(sender, **kwargs):
    print('it is working')
