from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

# Token authentication & access control
urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.asview(), name='token_refresh'),
]