
from django.urls import path,include
from account.views import RegisterView
urlpatterns=[
    path('account/',include('account.urls')),
    path('home/',include('home.urls')),
    ]