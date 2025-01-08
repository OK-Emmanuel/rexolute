from django.urls import path
from . import views  # Import your views here

urlpatterns = [
    path('', views.TherapistListView.as_view(), name='therapist-list'),
    path('<int:id>/', views.TherapistDetailView.as_view(), name='therapist-detail'),
]
