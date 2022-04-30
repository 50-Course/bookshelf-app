from rest_framework.routers import DefaultRouter

from apps.books.api.views import BookViewSet

router = DefaultRouter()
router.register('', BookViewSet, basename='book')
urlpatterns = router.urls
print(urlpatterns) # For quick debugging