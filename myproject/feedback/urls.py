from django.urls import path
from .views import feedback_list

app_name = 'feedback'

urlpatterns = [
       path('', feedback_list, name='feedback_list'),
   ]