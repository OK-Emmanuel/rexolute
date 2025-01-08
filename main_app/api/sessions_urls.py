from django.urls import path
from . import views  # Import your views here

urlpatterns = [
    path('', views.SessionListView.as_view(), name='session-list'),
    path('<int:id>/', views.SessionDetailView.as_view(), name='session-detail'),
]
