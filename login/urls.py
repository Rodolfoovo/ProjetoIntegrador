from django.urls import path
from django.contrib.auth import views as auth_views
from .views import login_view, logout_view

urlpatterns = [
    path('', login_view),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name="logout"),

    path('ResetarSenha/', auth_views.PasswordResetView.as_view(template_name='ResetarSenha.html'), name="reset_senha"),

    path('Envio_Reset_Senha/', auth_views.PasswordResetDoneView.as_view(), name='Reset_Senha_Done'),

    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='Reset_Senha_Confirmado'),

    path('Reset_Senha_Completado/',auth_views.PasswordResetCompleteView.as_view(), name='Reset_Senha_Completado'),
]