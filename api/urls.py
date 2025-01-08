from django.urls import path, include
from main_app.urls import urlpatterns as main_app_urls  # Import the main app's urls

urlpatterns = [
    path('auth/', include(main_app_urls)),  # auth is still under this
    path('users/', include('main_app.api.users_urls')), #auth for users url
    path('therapists/', include('main_app.api.therapists_urls')), #auth for therapists url
    path('sessions/', include('main_app.api.sessions_urls')), #auth for sessions url
    path('payments/', include('main_app.api.payments_urls')), #auth for payments url
    # path('register/', include(main_app_urls)),
]