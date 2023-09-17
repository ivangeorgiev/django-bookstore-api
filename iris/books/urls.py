from rest_framework import routers

from . import views

router = routers.SimpleRouter()
router.register("authors", views.AuthorViewSet)
router.register("publishers", views.PublisherViewSet)
router.register("books", views.BookViewSet)

urlpatterns = router.urls
