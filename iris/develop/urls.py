from django.urls import include, path

urlpatterns = [
    path("__debug__/", include("debug_toolbar.urls")),
]
