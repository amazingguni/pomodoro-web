from django.shortcuts import render
from django.http import HttpResponse

def home_page(request):
	return render(request, 'home.html',{
		'new_task_text':request.POST.get('task_text',''),
	})
