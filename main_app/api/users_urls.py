from django.urls import path
from . import views  # Import your views here (you'll need to create these views)

urlpatterns = [
    path('', views.UserListView.as_view(), name='user-list'),  # Example route to list users
    path('<int:id>/', views.UserDetailView.as_view(), name='user-detail'),  # Example route to get user details
]
