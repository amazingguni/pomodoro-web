from django.shortcuts import render, redirect
from django.http import HttpResponse
from tasks.models import Task

def home_page(request):
	if request.method == 'POST':
		Task.objects.create(text=request.POST.get('task_text',''))
		return redirect('/')
	
	tasks = Task.objects.all()
	return render(request, 'home.html', {'tasks':tasks})
