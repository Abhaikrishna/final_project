from . import views
from django.urls import path
app_name='formsapp'

urlpatterns = [
    path('form',views.form,name='form'),

]