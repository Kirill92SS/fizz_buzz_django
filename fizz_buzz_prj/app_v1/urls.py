from django.urls import path
from app_v1.views import index, make_fizz_buzz


urlpatterns = [
   path('', index),
   path('<int:number>', make_fizz_buzz),
]
