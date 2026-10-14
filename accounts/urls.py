from django.urls import path
from accounts.views import LoginAPIView, SignupAPIView


urlpatterns = [ 
    path('register/', SignupAPIView.as_view()),
    path('login/', LoginAPIView.as_view()),
    ]