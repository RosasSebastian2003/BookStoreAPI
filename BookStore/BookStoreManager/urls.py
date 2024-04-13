from rest_framework import routers
from .views import BookViewSet, AuthorViewSet, MemberViewSet, BorrowingViewSet

router = routers.DefaultRouter()
router.register(r'books', BookViewSet)
router.register(r'authors', AuthorViewSet)
router.register(r'members', MemberViewSet)
router.register(r'borrowings', BorrowingViewSet)

urlpatterns = router.urls