
from django.shortcuts import render,get_object_or_404,redirect

# Create your views here.
from django.http import HttpResponse
from notes.models import Matiere,Enseignant,Eleve,Niveau,Note
from notes.forms import NoteForm
def index(request):
	return render(request, "notes/index.html")

def eleves(request):
	eleves = Eleve.objects.all()
	return render(request,'notes/eleves.html',{'eleves':eleves})


def eleve(request, id):
	eleve = get_object_or_404(Eleve,pk=id)
	matieres = eleve.matieres.all()
	return render(request,'notes/eleve.html',{'eleve':eleve,'matieres':matieres})
	
def matieres(request):
	matieres = Matiere.objects.all()
	return render(request,'notes/matieres.html',{'matieres':matieres})
	

def matiere(request, id):
	matiere = get_object_or_404(Matiere,pk=id)
	return render(request,'notes/matiere.html',{'matiere':matiere})

def niveau(request, id):
	niveau = get_object_or_404(Niveau,pk=id)
	return render(request,'notes/niveau.html',{'niveau':niveau})

def add_note(request, matiere_id, eleve_id):
	matiere = Matiere.objects.get(pk=matiere_id)
	eleve = Eleve.objects.get(pk=eleve_id)

	# if request.method == "POST":
	# 	valeur = request.POST.get("note")
	# 	note = Note(eleve_id=eleve_id, matiere_id=matiere_id,valeur=valeur)
	# 	note.save()
	# 	return redirect("/notes/eleves")
	# else:
	# 	if eleve.matieres.filter(pk=matiere_id).exists():
	# 		return render(request, 'notes/add_note.html', locals())
	# 	else:
	# 		raise ValueError(f"The student ({eleve_id}) is not enrolled in the subject ({matiere_id}).")
	if request.method == "POST":
		form = NoteForm(request.POST)
		if form.is_valid():
			try:
				note = form.save(commit=False)
				note.eleve = eleve
				note.matiere = matiere
				note.save()
				return redirect('/notes/eleves')
			except:
				pass	
		
	
	else:
		form = NoteForm()
		return render(request, 'notes/add_note.html',{"form":form})
	

