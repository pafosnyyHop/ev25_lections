from django.urls import path

from .views import StudentAPIView

# http://localhost:8000
urlpatterns = [
    path('lists/', StudentAPIView.as_view()),
    path('delete/<int:id>/', StudentAPIView.as_view())
]