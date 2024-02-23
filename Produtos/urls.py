from django.urls import path
from Produtos.views import produtos_view
urlpatterns = [
    path('', produtos_view),
    path('produtos/',produtos_view, name="produtos_view"),
]