from . import views
from django.urls import path
app_name='dummy2app'

urlpatterns = [
    path('register',views.register,name='register'),
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout'),
    path('about',views.about,name='about')

 ]