from django import forms
from .models import Item

class ItemForm(forms.ModelForm):
    # Bcz we used ModelForm of forms which we've imported from django
    # Django provides a way to automatically create forms using ModelForm.
    
    class Meta:
        model = Item # name of model we will be using
        fields = ("item_name","item_description")
