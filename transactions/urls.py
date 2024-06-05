from django.urls import path, include
from rest_framework.routers import DefaultRouter
from transactions.views import TransactionViewSet, CategoryViewSet

router = DefaultRouter()
router.register(r'Transaction', TransactionViewSet)
router.register(r'Category', CategoryViewSet)

urlpatterns = [
    path('', include(router.urls)),
]