from django.urls import path
from .views import RegisterUserView, LoginUserView

from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('register/', RegisterUserView.as_view(), name='register'),
    path('login/', LoginUserView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
]