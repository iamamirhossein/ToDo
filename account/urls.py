from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import ProfileViewSet

app_name = 'account'

urlpatterns = [
    path(r'token/', TokenObtainPairView.as_view(), name='token-get'),
    path(r'token/refresh', TokenRefreshView.as_view(), name='token-refresh'),
]

router = DefaultRouter()
router.register(r'profile', ProfileViewSet, basename='profile')

urlpatterns += router.urls
