# pylint: disable=wildcard-import,unused-wildcard-import
from .settings import *

INSTALLED_APPS.extend(
    [
        "tests.fake_app",
    ]
)
