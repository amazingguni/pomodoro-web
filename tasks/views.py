from django.shortcuts import render, redirect
from django.http import HttpResponse
from tasks.models import Task

def home_page(request):
	if request.method == 'POST':
		Task.objects.create(title=request.POST.get('task_title',''))
		return redirect('/')
	
	tasks = Task.objects.all()
	return render(request, 'home.html', {'tasks':tasks})
