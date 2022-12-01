from django import forms

class BajosForm(forms.Form):
    marca = forms.CharField(max_length=20)
    modelo = forms.CharField(max_length=20)
    año_fabricacion = forms.IntegerField()
    cuerdas = forms.IntegerField()

class BateriasForm(forms.Form):
    marca = forms.CharField(max_length=20)
    modelo = forms.CharField(max_length=20)
    año_fabricacion = forms.IntegerField()

class GuitarrasForm(forms.Form):
    marca = forms.CharField(max_length=20)
    modelo = forms.CharField(max_length=20)
    año_fabricacion = forms.IntegerField()
    cuerdas = forms.IntegerField()