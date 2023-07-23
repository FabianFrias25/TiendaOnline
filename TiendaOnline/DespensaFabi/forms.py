from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import User


class RegistrationForm(UserCreationForm):
    nacionalidad = forms.CharField(max_length=100)
    nacimiento = forms.DateField()
    ciudad = forms.CharField(max_length=100)
    postal = forms.CharField(max_length=10)
    direccion = forms.CharField(max_length=100)

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'nacionalidad', 'nacimiento', 'ciudad', 'postal', 'direccion']
        help_texts = {k: "" for k in fields}


class UserEditForm(UserChangeForm):
    username = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Username"}))
    email = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Email"}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "First Name"}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Last Name"}))
    nacimiento = forms.DateField(
        label="Fecha de nacimiento",
        widget=forms.DateInput(attrs={"placeholder": "Fecha de nacimiento (YYYY-MM-DD)"}),
    )
    nacionalidad = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Nacionalidad"}))
    ciudad = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Ciudad"}))
    postal = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Codigo Postal"}))
    direccion = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Direccion o Domicilio"}))

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'nacimiento', 'nacionalidad',
                  'ciudad', 'postal', 'direccion']
        help_texts = {k: "" for k in fields}


class ChangePasswordForm(PasswordChangeForm):
    old_password = forms.CharField(
        label="",
        widget=forms.PasswordInput(attrs={"placeholder": "Contraseña actual"}),
        error_messages={
            'password_incorrect': "",
        },
    )

    new_password1 = forms.CharField(
        label="",
        widget=forms.PasswordInput(attrs={"placeholder": "Nueva Contraseña"}),
    )

    new_password2 = forms.CharField(
        label="",
        widget=forms.PasswordInput(attrs={"placeholder": "Confirmar nueva Contraseña"}),
    )

    class Meta:
        model = User
        fields = ['old_password', 'new_password1', 'new_password2']
