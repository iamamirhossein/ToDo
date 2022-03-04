from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

app_name = 'account'

urlpatterns = [
    path(r'token/', TokenObtainPairView.as_view(), name='token-get'),
    path(r'token/refresh', TokenRefreshView.as_view(), name='token-refresh'),
]