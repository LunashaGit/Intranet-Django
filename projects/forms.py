from django import forms
from .models import Category


class UploadImage(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('category_name','slug','category_description','category_image')