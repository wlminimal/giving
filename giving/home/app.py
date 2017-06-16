from django.apps import AppConfig


class UserConfig(AppConfig):
    name = 'giving.home'
    verbose_name = "Homes"

    def ready(self):
        import giving.home.signals
