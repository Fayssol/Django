from django.urls import path 
from . import views
app_name = 'notes'

urlpatterns = [
    path('',views.index, name = 'index'),
    path('eleves',views.eleves,name='eleves'),
    path('eleves/<id>',views.eleve,name='eleves'),
    path('matieres', views.matieres,name='matieres'),
    path('matieres/<id>',views.matiere, name='matieres'),
    path('niveau/<id>',views.niveau,name='niveau'),

    path('add_note/<int:matiere_id>/<int:eleve_id>',views.add_note, name = 'add_note'),
    
]
