from django import forms

class UserForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'input', 'placeholder': 'Nombre'}))
    surnames = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'input', 'placeholder': 'Apellidos'}))
    email = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'input', 'placeholder': 'Correo electrónico'}))
    phone = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'input', 'placeholder': 'Móvil'}))
    hobbies = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'input', 'placeholder': 'Aficiones'}))
