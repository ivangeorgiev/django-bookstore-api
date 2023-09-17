from django.apps import AppConfig


class DevelopConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'develop'

    def ready(self) -> None:
        from iris.urls import urlpatterns
        from django.urls import include, path
        urlpatterns.append(path("__debug__/", include("develop.urls")))
