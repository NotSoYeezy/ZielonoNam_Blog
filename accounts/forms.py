from django.contrib.auth.forms import PasswordChangeForm, PasswordResetForm, SetPasswordForm
from django.contrib.auth.password_validation import validate_password
from django import forms
from .models import User


class UserRegisterForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form_inp', 'placeholder': 'Nazwa użytkownika'}), label='')
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form_inp', 'placeholder': 'Email'}), label='')
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form_inp', 'placeholder': 'Hasło'}), label='')
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form_inp', 'placeholder': 'Potwierdź Hasło'}), label='')
    profile_pic = forms.ImageField(label='Zdjęcie profilowe', widget=forms.FileInput(attrs={'class': 'img_fld'}))

    def clean(self):
        cleaned_data = super(UserRegisterForm, self).clean()
        password = cleaned_data['password']
        confirm_password = cleaned_data['confirm_password']

        if password != confirm_password:
            raise forms.ValidationError(
                "Hasła się różnią"
            )

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'profile_pic',)
    
    field_order = ['username', 'email', 'password', 'confirm_password', 'profile_pic']
        

class UserChangePasswordForm(PasswordChangeForm):
    def __init__(self, *args, **kwargs):
        super(UserChangePasswordForm, self).__init__(*args, **kwargs)

    old_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form_inp', 'placeholder': 'Stare hasło'}), label='')
    new_password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form_inp', 'placeholder': 'Nowe hasło'}), label='')
    new_password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form_inp', 'placeholder': 'Powtórz stare hasło'}), label='')


class UserSetPasswordForm(SetPasswordForm):
    def __init__(self, *args, **kwargs):
        super(UserSetPasswordForm, self).__init__(*args, **kwargs)

    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form_inp'}),
                               validators=[validate_password], label='')
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form_inp'}), label='')

    #   Cleaning data to get password input and check if passwords match
    def clean(self):
        cleaned_data = super(UserSetPasswordForm, self).clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password != confirm_password:
            raise forms.ValidationError(
                "Passwords do not match"
            )


class UserPasswordResetForm(PasswordResetForm):
    def __init__(self, *args, **kwargs):
        super(UserPasswordResetForm, self).__init__(*args, **kwargs)

    email = forms.EmailField(label='', widget=forms.EmailInput(attrs={'class': 'form_inp'}))