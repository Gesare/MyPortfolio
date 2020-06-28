from django.apps import AppConfig


class PortappConfig(AppConfig):
    name = 'portapp'

    def ready(self):
        import portapp.signals
