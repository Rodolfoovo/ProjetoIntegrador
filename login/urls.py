from django.urls import path
from .views import login_view , reset_senha_view, logout_view
urlpatterns = [
    path('', login_view),
    path('login/', login_view, name='login'),   
    path('ResetarSenha/', reset_senha_view, name="reset_senha"),  
    path('logout/', logout_view, name="logout")
]