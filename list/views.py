from django.shortcuts import render, redirect, get_object_or_404
from .models import Item
from .forms import ItemForm
from django.forms import ValidationError
from django.utils.translation import gettext as _
from django.contrib import messages

# Create your views here.

# View to display the item list
def item_list(request):
    items= Item.objects.all() # Get all items one by one
    return render(request, 'item_list.html', {'items' : items})

# View to add item
def add_item(request):
    form = ItemForm()
    if request.method == 'POST':
        form = ItemForm(request.POST) # to post form from forms.py 
        if form.is_valid(): # to ceck weather submitted form is either valid or not
            messages.success(request, "your added item has saved successfully")
            form.save()
            return redirect('item_list')
    else:
        form = ItemForm()
        ValidationError(_("Invalid value"), code="invalid") # to se transition we've used "_" and to use "_" we've imported "from django.utils.translation import gettext as _"
    return render(request, 'add_item.html', {'form':form})

# View to edit item
def edit_item(request,pk):
    item = get_object_or_404(Item.objects.all(), pk= pk)
    if request.method=='POST':
        
        form = ItemForm(request.POST, instance=item) # the form user will get to see
        #form = ItemForm(request.POST, isinstance=item)
        if form.is_valid():
            # raise a editted successfully message using django messages
            messages.success(request, "your edited item has saved successfully")
            # save form
            form.save()
            # redirect to items list view after editing.
            return redirect('item_list')
    else:
        form = ItemForm()
        ValidationError(_("Invalid form"), code="invalid")
    return render(request, 'edit_item.html', {'form':form, 'item':item})
    
# View to delete item
def delete_item(request, pk):
    item = get_object_or_404(Item, pk = pk)
    if request.method == 'POST':
        item.delete()
        return redirect(item_list)
    return render(request, 'delete_item.html', {'item':item})