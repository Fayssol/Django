from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils.text import slugify
from django.utils import timezone
# Create your models here.
class Personne(models.Model):
    id = models.BigAutoField(primary_key=True)
    nom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50)
    sexe = models.CharField(max_length=1,
    choices=[("M", "Masculin"), ("F", "Féminin")])
    date_naissance = models.DateField(null=True)
    class Meta:
        abstract = True
    def __str__(self) -> str:
        return self.nom
class Enseignant(Personne):
    pass
class Meta:
    verbose_name = 'Enseignant'
    verbose_name_plural = 'Enseignant'
    def __str__(self) -> str:
        return super().__str__()
    
class Niveau(models.Model):
    nom = models.CharField(unique=True,max_length=2,null=True)
    class Meta:
        verbose_name = 'Niveau'
        verbose_name_plural = 'Niveau'
    def __str__(self) -> str:
        return self.nom 

class Matiere(models.Model):
    nom = models.CharField(unique=True,max_length=50)
    enseignant = models.ForeignKey(Enseignant,on_delete=models.SET_NULL,null=True)
    niveaux = models.ManyToManyField(Niveau)
    class Meta:
        verbose_name = 'Matière'
        verbose_name_plural = 'Matière'
    def __str__(self) -> str:
        return self.nom 
    
class Eleve(Personne):
    eleve_id = models.BigIntegerField(unique=True)
    niveau = models.ForeignKey(Niveau,on_delete=models.SET_NULL,null=True)
    matieres = models.ManyToManyField(Matiere)
    class Meta:
        verbose_name = 'Élève'
        verbose_name_plural = 'Élève'
    def __str__(self) -> str:
        return super().__str__()  

    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.eleve_id = self.generate_eleve_id(instance)
        if commit:
            instance.save()
        return instance
        def generate_eleve_id(self, instance):
            timestamp = int(timezone.now().timestamp())
            nom_abbrev = slugify(instance.nom)[:2].upper()
            return f"{timestamp}_{nom_abbrev}"  
    
class Note(models.Model):
    valeur = models.FloatField(null=True,validators=[MinValueValidator(0), MaxValueValidator(20)])
    eleve = models.ForeignKey(Eleve,on_delete=models.CASCADE)
    matiere = models.ForeignKey(Matiere,on_delete=models.CASCADE)
    def __str__(self):
        return str(self.valeur)    
