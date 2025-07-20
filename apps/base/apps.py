"""AppConfig for base app."""
from django.apps import AppConfig

class BaseConfig(AppConfig):
    """Configuration for the base app."""
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.base'
