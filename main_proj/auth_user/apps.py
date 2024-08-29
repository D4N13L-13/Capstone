from django.apps import AppConfig

"""
The `User_authConfig` class in Python sets the default auto field and
specifies the name for the authentication user configuration.
"""


class User_authConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'auth_user'
