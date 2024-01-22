from django.urls import path
from .views import login
urlpatterns = [
    path('', login),
    path('login/', login, name="login"),    
]