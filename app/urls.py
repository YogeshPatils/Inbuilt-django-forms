from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static
urlpatterns=[
    path('signup/',signUpview,name='signup'),
    path('signin/',logInView,name='signin'),
    path('home/',homeView,name='home'),
    path('logout/',logOutView,name='logout')
]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)