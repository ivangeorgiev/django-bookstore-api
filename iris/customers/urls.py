from rest_framework import routers

from . import views

router = routers.SimpleRouter()
router.register("addresses", views.AddressViewSet)
router.register("customers", views.CustomerViewSet)

urlpatterns = router.urls
