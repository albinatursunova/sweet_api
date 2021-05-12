from django.urls import path

from account.views import (RegistrationView, ActivationView, LoginView, LogoutView, ChangePasswordView)

urlpatterns = [
    path('register/', RegistrationView.as_view()),
    path('activation/', ActivationView.as_view()),
    path('login/', LoginView.as_view()),
    path('logout/', LogoutView.as_view()),
    path('change-password/', ChangePasswordView.as_view()), #, name='change-password'
]
