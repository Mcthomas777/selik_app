from django.apps import AppConfig


class ReAgentAppConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "re_agent_app"

    def ready(self):

        import re_agent_app.signals  

        return super().ready()
