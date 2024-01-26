from django.urls import path
from dashboard.views import telainicial_view

urlpatterns = [
    path('',telainicial_view),
    path('telainicial/', telainicial_view, name='telainicial'), 
]