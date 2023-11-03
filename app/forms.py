from django import forms

class ImageUploadForm(forms.Form):
    customer_name = forms.CharField()
    file = forms.FileField()
