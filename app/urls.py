from django.urls import path
from .views import index, home

# Tutor
from . views import tutor_cadastrar, tutor_listar, tutor_editar, tutor_deletar


urlpatterns = [
    # Login do sistema
    path('', index, name='index'),
    
    # Home do sistemas
    path('home/', home, name='home'),
    
    # Tutores
    path('tutor_cadastrar/', tutor_cadastrar, name='tutor_cadastrar'),
    path('tutor_listar/', tutor_listar, name='tutor_listar'),
    path('tutor_editar/<int:id_tutor>/', tutor_editar, name='tutor_editar'),
    path('tutor_deletar/<int:id_tutor>/', tutor_deletar, name='tutor_deletar'),
    
]