from django.urls import path
from .views import index, home

# Tutor
from . views import tutor_cadastrar, tutor_listar, tutor_editar, tutor_deletar, tutor_unico
from . views import pet_cadastrar


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
    path('tutor_unico/<int:id_tutor>/', tutor_unico, name='tutor_unico'),
    
    # Pet
    path('pet_cadastrar/<int:id_tutor>/',pet_cadastrar, name='pet_cadastrar' ),
    
]