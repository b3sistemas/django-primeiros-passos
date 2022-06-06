from urllib.parse import urlparse
from django.urls import path
from .views import ListaPessoaView, PessoaCreateView, PessoaDeleteView, PessoaUpdateView


urlpatterns = [
    path('', ListaPessoaView.as_view(), name='TestePrjPessoaApp.index'),
    path('novo/', PessoaCreateView.as_view(), name='TestePrjPessoaApp.novo'),
    path('editar/<int:pk>', PessoaUpdateView.as_view(), name='TestePrjPessoaApp.editar'),
    path('deletar/<int:pk>', PessoaDeleteView.as_view(), name='TestePrjPessoaApp.deletar')
]
