from rest_framework.routers import SimpleRouter

from usermanager.api import RegisterUser


router = SimpleRouter()
router.register("register", RegisterUser, basename="api-register")
