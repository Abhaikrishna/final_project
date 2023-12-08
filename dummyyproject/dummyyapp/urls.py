from . import views
from django.urls import path
app_name='dummyyapp'
urlpatterns = [
    path('',views.dummyy,name='dummyy'),
    path('Form', views.Form, name='Form')

]