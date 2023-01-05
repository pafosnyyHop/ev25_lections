from django.urls import path
from . import views


urlpatterns = [
    path('', views.UserListView.as_view()),
    path('<int:pk>/', views.UserDetailViews.as_view()),
    path('login/', views.CustomLoginView.as_view()),
    path('logout/', views.CustomLogoutView.as_view()),
    path('register/', views.UserRegisterView.as_view()),
]
