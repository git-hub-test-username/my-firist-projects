
from django.urls import path
from myapp.views import all_product,completed_product,waiting_product



urlpatterns = [
     path('all_product/',all_product ),
     path('completed-product/',completed_product ),
     path('waiting-product/',waiting_product ),
    
]