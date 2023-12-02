from django.shortcuts import render, redirect
from .forms import ProdutoForm
from .services.ConnectionService import ConnectionService
from .services.MongoServie import MongoService
from .services.repositories.FoodManagerRepository import FoodManagerRepository
from .services.CadastroProdutoService import CadastroProdutoService


# Create your views here.


def index(request):
    return render(request, "index.html")


def cadastroProduto(request):
    if request.method == "POST":
        form = ProdutoForm(request.POST)
        if form.is_valid():
            conexao = ConnectionService()
            mongo = MongoService(conexao, "FoodManager")
            repository = FoodManagerRepository(mongo)
            service = CadastroProdutoService(repository)
            service.insert(form.cleaned_data)
        else:
            return render(request, "cadastroProduto.html", {"form": form})
    form = ProdutoForm()
    return render(request, "cadastroProduto.html", {"form": form})


def listarProdutos(request):
    conexao = ConnectionService()
    mongo = MongoService(conexao, "FoodManager")
    repository = FoodManagerRepository(mongo)
    produtos = list(repository.find("Produtos", **{}))
    return render(request, "listarProdutos.html", {"produtos": produtos})


def listarRequerentes(request):
    conexao = ConnectionService()
    mongo = MongoService(conexao, "FoodManager")
    repository = FoodManagerRepository(mongo)
    requerentes = list(repository.find("Requerentes", **{}))
    return render(request, "listarRequerentes.html", {"requerentes": requerentes})
