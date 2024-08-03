from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .models import Student
from .forms import StudentForm

def home(request):
    return render(request, 'home.html')

def register(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('history')
    else:
        form = StudentForm()
    return render(request, 'register.html', {'form': form})

def history(request):
    students = Student.objects.all()
    return render(request, 'history.html', {'students': students})

