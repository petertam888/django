from django import forms
from .models import Product


class ProductForm(forms.ModelForm):
    title = forms.CharField(label='', widget=forms.TextInput(attrs={"placeholder": "Your Title"}))
    description = forms.CharField(widget=forms.Textarea(attrs={"placeholder": "Description is written here"}))
    price = forms.DecimalField()

    class Meta:
        model = Product
        fields = [
            'title',
            'description',
            'price'
        ]

    def clean_title(self, *args, **kwargs):
        title = self.cleaned_data.get("title")
        if "peter" in title:
            return title
        else:
            raise forms.ValidationError("This is not a valid title")

class RawProduction(forms.Form):
    title = forms.CharField(label='', widget=forms.TextInput(attrs={"placeholder": "Your Title"}))
    description = forms.CharField(widget=forms.Textarea(attrs={"placeholder": "Description is written here"}))
    price = forms.DecimalField()
