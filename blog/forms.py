from django import forms

class AutorFormulario(forms.Form):
    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)
    email = forms.EmailField()


class SeccionFormulario(forms.Form):
    nombre = forms.CharField(max_length=30)

class PostFormulario(forms.Form):
    titulo = forms.CharField(max_length=30)
    sub_titulo = forms.CharField(max_length=30)
    cuerpo = forms.CharField(widget=forms.Textarea)