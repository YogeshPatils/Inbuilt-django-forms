from django.urls import path
from .views import *

urlpatterns=[
    path('signup/',signUpview,name='signin'),
    path('signin/',logInView,name='signin'),
    path('home/',homeView,name='home')
]