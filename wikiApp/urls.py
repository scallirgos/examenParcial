from django.urls import path
from . import views

app_name='wikiApp'

urlpatterns = [
    path('',views.vistaPrincipal,name='vistaPrincipal'),
    path('nuevoArticulo',views.nuevoArticulo,name='nuevoArticulo'),
    path('nuevoTema',views.nuevoTema,name='nuevoTema'),
    path('articulos',views.articulos,name='articulos'),
    path('temas',views.temas,name='temas'),
    path('verTema/<str:idTema>',views.verTema,name='verTema')
]   