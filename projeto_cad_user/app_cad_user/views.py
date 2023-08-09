from django.shortcuts import render
from .models import Usuario

def home(request):
    return render(request,'usuarios/home.html')

def usuarios(request):
    # Salvar os dados da tela para o banco de dados.
    novo_usuario = Usuario()
    novo_usuario.nome = request.POST.get('nome')
    novo_usuario.idade = request.POST.get('idade')
    novo_usuario.save()
    # Exibix toso os usuarios já cadastradps em uma nova página
    usuarios={

        'usuarios': Usuario.objects.all()

    }
    # Retonar os dados para a pagina de listagem de usuários 
    return render(request,'usuarios/usuarios.html', usuarios)