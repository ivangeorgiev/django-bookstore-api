# pylint: disable=wildcard-import,unused-wildcard-import
from .settings import *

INSTALLED_APPS.extend(
    [
        "django_extensions",
        "debug_toolbar",
        # Local apps
        "develop",
    ]
)

MIDDLEWARE.extend(
    [
        "debug_toolbar.middleware.DebugToolbarMiddleware",
    ]
)

INTERNAL_IPS = [
    "127.0.0.1",
]
