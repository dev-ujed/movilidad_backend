from django.urls import path
from .views import RegisterUserView, LoginUserView, LogoutApiView
urlpatterns = [
    path('register/', RegisterUserView.as_view(), name='register'),
    path('login/', LoginUserView.as_view(), name='login'),
    path('logout/', LogoutApiView.as_view()), 
]
