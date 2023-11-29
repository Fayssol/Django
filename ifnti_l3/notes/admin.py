from django.contrib import admin
from notes.forms import EleveForm
from notes.models import Niveau,Eleve,Enseignant,Matiere,Note
# Register your models here.
class EleveAdmin(admin.ModelAdmin):
    form = EleveForm


admin.site.register(Eleve, EleveAdmin)
admin.site.register(Niveau)
admin.site.register(Enseignant)
admin.site.register(Matiere)
admin.site.register(Note)
#admin.site.register(Eleve)