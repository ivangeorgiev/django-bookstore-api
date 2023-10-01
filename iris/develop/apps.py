from django.apps import AppConfig


class DevelopConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "develop"

    def ready(self) -> None:
        # pylint: disable=import-outside-toplevel)
        from django.urls import include, path

        from iris.urls import urlpatterns

        urlpatterns.append(path("__debug__/", include("develop.urls")))
