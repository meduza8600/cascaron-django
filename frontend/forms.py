from django import forms


class SolicitarForm(forms.Form):
    nombre = forms.CharField(widget=forms.TextInput())

    apellido = forms.CharField(widget=forms.TextInput())

    correo = forms.EmailField(widget=forms.EmailInput())

    telefono = forms.CharField(widget=forms.TextInput())

    puesto = forms.CharField(widget=forms.TextInput())

    pais = forms.CharField(widget=forms.TextInput())

    # cv_fichero = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))
    cv_fichero = forms.FileField(widget=forms.ClearableFileInput(attrs={'class': 'd-none'}), required=False)
