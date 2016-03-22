from django.shortcuts import render, redirect
from django.http import HttpResponse
from lists.models import Item

def home_page(request):
	if request.method == 'POST':
		Item.objects.create(title=request.POST.get('item_title',''))
		return redirect('/lists/the-only-item-in-the-world/')
	
	lists = Item.objects.all()
	return render(request, 'home.html', {'lists':lists})
