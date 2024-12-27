from django.apps import AppConfig


class PersonalaiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'PersonalAI'

# def ready(self):
#     import PersonalAI.signals