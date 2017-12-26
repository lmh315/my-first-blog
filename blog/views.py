from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from .models import item
from .forms import itemForm

def post_list(request):
    items = item.objects.all()
    return render(request, 'blog/post_list.html', {'items':items})

def member(request):
    return render(request, 'blog/member.html', {})

def item_new(request):
	if request.method == "POST":
		form = itemForm(request.POST)
		if form.is_valid():
			form.save()
	else:
		form = itemForm()
	return render(request, 'blog/item_edit.html', {'form': form})

def item_edit(request, name):
    items = item.objects.all()
#    name.inventory += 1
    Item = get_object_or_404(item, name=name)
    print(request)
    if request.method == "POST":
        form = itemForm(request.POST, instance=item)
        Item.inventory = Item.inventory + int(request.POST['addNum'])
        Item.save()
        return redirect('post_list')
    else:
       form = itemForm(instance=item)
       Item.inventory += 1
       Item.save()
       print(Item.inventory)
    return redirect('post_list')
# Create your views here.
