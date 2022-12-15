from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from .forms import PersonForm
from .models import Person

# Create your views here.
def index(request):
    return render(request, 'index.html')

def create(request):

    form = PersonForm()
    context = {'form': form}
        
    if request.method == 'POST':
        name_1 = request.POST['name-1']
        name_2 = request.POST['name-2']
        email = request.POST['email']
        gender = request.POST['gender']
    
        person = Person.objects.create(name=name_1 + ' ' + name_2, email=email, gender=gender)
        person.save()

    return render(request, 'create.html', context)

def view(request):
    
    data = {}
    data['create'] = Person.objects.all()

    return render(request, 'view.html', data)

def read(request, pk):

    data = {}
    data['read'] = Person.objects.get(pk=pk)

    return render(request, 'read.html', data)


def delete(request, pk):
    db = Person.objects.get(pk=pk)

    db.delete()

    return render(request, 'view.html')

def edit(request, pk):

    data = {}
    data['form'] = PersonForm()
    data['user'] = get_object_or_404(Person, pk=pk)

    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        gender = request.POST['gender']

        new_user = Person.objects.filter(pk=pk).update(name=name, email=email, gender=gender)
        return redirect('index')

    return render(request, 'edit.html', data)
