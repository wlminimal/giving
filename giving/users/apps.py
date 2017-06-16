from django.apps import AppConfig


class UsersConfig(AppConfig):
    name = 'giving.users'
    verbose_name = "Users"

    def ready(self):
        """Override this to put in:
            Users system checks
            Users signal registration
        """
        # Using @receiver() so just import signal module
        # import giving.users.signals

        # if using connect function do something like this
        # user_signed_up.connect(create_stripe_customer, sender=User)
        pass
