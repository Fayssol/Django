from django.forms import ModelForm
from django.core.validators import MinValueValidator, MaxValueValidator
from notes.models import Note,Eleve


class NoteForm(ModelForm):
    class Meta:
        model = Note
        fields = ["valeur"]
        labels = {"valeur": "Note sur 20"}
        validators = [
            MinValueValidator(0, message="La note doit être supérieure ou égale à 0."),
            MaxValueValidator(20, message="La note doit être inférieure ou égale à 20.")
        ]
class EleveForm(ModelForm):
    class Meta:
        fields = '__all__'
        model = Eleve  

    def clean(self):
        cleaned_data = super().clean()
        nom = cleaned_data.get('nom')
        prenom = cleaned_data.get('prenom')

        if any(char.isdigit() for char in nom):
            self.add_error('nom', 'Le nom ne doit pas contenir de chiffres.')

        if any(char.isdigit() for char in prenom):
            self.add_error('prenom', 'Le prénom ne doit pas contenir de chiffres.')          
            