from django.urls import path
from .views import login_view , reset_senha
urlpatterns = [
    path('', login_view),
    path('login/', login_view, name='login'),   
    path('ResetarSenha/', reset_senha, name="reset_senha"),  
]