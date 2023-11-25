from django.shortcuts import render

# Create your views here.
# Está view está sendo utilizada para poder retornar uma request do sistema, retornando assim um template.
def home(request):
    return render(request, "index.html")
