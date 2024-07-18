from django import forms
from .models import CustomUser  # Importa tu modelo de usuario personalizado
from django.contrib.auth.hashers import make_password

class UserForm(forms.ModelForm):
    confirm_password = forms.CharField(widget=forms.PasswordInput(), label='Confirmar Contraseña', required=False)
    auth_IM_photo = forms.ImageField(label='Foto', required=False)

    class Meta:
        model = CustomUser
        fields = ['email', 'password', 'is_superuser', 'is_active', 'auth_CH_email_Alter', 'auth_CH_telf', 'auth_CH_telfAlter', 'auth_IM_photo']

    dni = forms.CharField(label='DNI de la Persona', required=False)

    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        self.fields['email'].required = True
        self.fields['is_superuser'].required = False
        self.fields['is_active'].required = False
        self.fields['password'].widget = forms.PasswordInput()

        # Si se proporciona una instancia (es decir, estamos actualizando), establece los campos de contraseña y DNI como no requeridos
        if 'instance' in kwargs:
            self.fields['password'].required = False
            self.fields['dni'].required = False

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        # Verifica si se proporciona una nueva contraseña y si las contraseñas coinciden
        if password and password != confirm_password:
            raise forms.ValidationError("Las contraseñas no coinciden")

        return cleaned_data
    
class UserConfigForm(forms.ModelForm):

    class Meta:
        model = CustomUser
        fields = ['email', 'auth_CH_email_Alter', 'auth_CH_telf', 'auth_CH_telfAlter', 'auth_IM_photo']


class ResetPasswordForm(forms.ModelForm):
    confirm_password = forms.CharField(widget=forms.PasswordInput(), label='Confirmar Contraseña', required=False)
    
    class Meta:
        model = CustomUser
        fields = []  # Elimina el campo password del formulario
        
    def save(self, commit=True):
        instance = super().save(commit=False)
        password = self.cleaned_data.get("password")
        if password:  # Verifica si se proporciona una nueva contraseña
            instance.password = make_password(password)  # Hashea la contraseña antes de guardarla
        if commit:
            instance.save()
        return instance

