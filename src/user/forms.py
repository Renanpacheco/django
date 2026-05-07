from django import forms

class CadastroForm(forms.Form):
    nome = forms.CharField(
        min_length=3,
        max_length=100,
        widget=forms.TextInput(attrs={'placeholder': 'Ex: Izadora Souza'})
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'placeholder': 'seu@email.com'})
    )
    password = forms.CharField(
        min_length=8,
        widget=forms.PasswordInput(attrs={'class': 'seu-estilo-css', 'placeholder': 'Crie uma senha'})
    )
