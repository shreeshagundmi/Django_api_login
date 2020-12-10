from rest_framework.routers import SimpleRouter

from search import views

app_name = 'search'

router = SimpleRouter()
router.register(
    basename='cars',
    prefix=r'',
    viewset=views.CarViewSet
)
urlpatterns = router.urls
