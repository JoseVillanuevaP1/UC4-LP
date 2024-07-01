from django import forms
from django.core import validators

class CourseForm(forms.Form):
    code = forms.CharField(
        label="Código",
        max_length=10,
        widget=forms.TextInput(attrs={'placeholder': 'Ingrese el código del curso', 'class': 'code_form'}),
        validators=[
            validators.RegexValidator('^[A-Za-z0-9áéíóú ]+$', 'El código tiene caracteres inválidos', 'code_invalid')
        ]
    )
    name = forms.CharField(
        label="Nombre",
        max_length=100,
        widget=forms.TextInput(attrs={'placeholder': 'Ingrese el nombre del curso', 'class': 'name_form'}),
        validators=[
            validators.MinLengthValidator(4, 'El nombre es corto'),
            validators.RegexValidator('^[A-Za-z0-9áéíóúñÑ ]*$', 'El nombre tiene caracteres inválidos', 'name_invalid')
        ]
    )
    hour = forms.IntegerField(
        label="Horas",
        widget=forms.NumberInput(attrs={'placeholder': 'Ingrese horas del curso ', 'class': 'hour_form'})
    )
    credits = forms.IntegerField(
        label="Créditos",
        widget=forms.NumberInput(attrs={'placeholder': 'Ingrese créditos del curso ', 'class': 'credits_form'})
    )
    STATE_CHOICES = [
        (True, 'Habilitado'),
        (False, 'Deshabilitado'),
    ]
    state = forms.ChoiceField(
        label="Estado",
        choices=STATE_CHOICES,
        widget=forms.Select(attrs={'class': 'state_form'})
    )
