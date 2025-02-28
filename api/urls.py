from django.urls import path
from .views import userApiView

urlpatterns=[
    path('userapi/',userApiView,name='userapi')
]