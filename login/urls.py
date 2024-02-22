from django.urls import path
from django.contrib.auth import views as auth_views
from .views import login_view, logout_view

urlpatterns = [
    path('', login_view),
    path('login/', login_view, name='login'),   
    path('ResetarSenha/', auth_views.PasswordResetView.as_view(template_name='ResetarSenha.html'), name="reset_senha"),  
    path('logout/', logout_view, name="logout")
]
