from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.contrib import messages
from .forms import PersonForm
from .models import Person

# Create your views here.
def index(request):
    return render(request, 'index.html')

def view(request):
    
    data = {}
    data['create'] = Person.objects.all()

    return render(request, 'view.html', data)

def create(request):

    form = PersonForm()
    context = {'form': form}
        
    if request.method == 'POST':
        name_1 = request.POST['name-1']
        name_2 = request.POST['name-2']
        email = request.POST['email']
        gender = request.POST['gender']
    
        person = Person.objects.create(name=name_1 + ' ' + name_2, email=email, gender=gender)
        messages.success(request, 'User created successfully')
        person.save()
        return redirect('view')

    return render(request, 'create.html', context)

def read(request, pk):

    data = {}
    data['read'] = Person.objects.get(pk=pk)

    return render(request, 'read.html', data)


def delete(request, pk):
    db = Person.objects.get(pk=pk)
    db.delete()
    messages.info(request, 'User deleted sucessfully!')

    return redirect('view')

def edit(request, pk):

    data = {}
    data['form'] = PersonForm()
    data['user'] = get_object_or_404(Person, pk=pk)

    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        gender = request.POST['gender']
        date = request.POST['date']

        new_user = Person.objects.filter(pk=pk).update(name=name, email=email, gender=gender, date=date)
        messages.success(request, 'User edited sucessfully!')
        return redirect('view')

    return render(request, 'edit.html', data)


def charts(request):

    data = {}

    data['man'] = len(Person.objects.filter(gender='Man'))
    data['woman'] = len(Person.objects.filter(gender='Woman'))

    data['october'] = len(Person.objects.filter(date__month='10'))
    data['november'] = len(Person.objects.filter(date__month='11'))
    data['december'] = len(Person.objects.filter(date__month='12'))

    return render(request, 'charts.html', data)