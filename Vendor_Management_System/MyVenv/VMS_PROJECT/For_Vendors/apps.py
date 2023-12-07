from django.apps import AppConfig


class ForVendorsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'For_Vendors'

    def ready(self):
        import For_Vendors.signals
