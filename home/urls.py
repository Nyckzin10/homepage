from django.urls import path 


#importando as views 
from .views import index

urlpatterns = [ 
    path('', index),
]