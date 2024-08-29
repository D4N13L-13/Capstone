from django.apps import AppConfig


# Sets the default auto field to `BigAutoField` for 'polls'.
class PollsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'polls'
