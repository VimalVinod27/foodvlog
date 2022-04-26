from . import views
from django.urls import path
app_name='accounts'
urlpatterns=[
    path('register/',views.register,name='register'),
    path('login/',views.loginuser,name='loginuser'),
    path('logout/',views.logoutuser,name='logoutuser')
    ]