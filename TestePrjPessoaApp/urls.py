from urllib.parse import urlparse
from django.urls import path
from .views import ListaPessoaView, PessoaCreateView


urlpatterns = [
    path('', ListaPessoaView.as_view(), name='TestePrjPessoaApp.index'),
    path('novo/', PessoaCreateView.as_view(), name='TestePrjPessoaApp.novo')
]
