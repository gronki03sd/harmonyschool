from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, Role

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    phone = forms.CharField(required=False)
    role = forms.ModelChoiceField(queryset=Role.objects.filter(name__in=['Student', 'Staff']), required=True)

    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'phone', 'role', 'password1', 'password2')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user
    


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'phone']
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].disabled = True  # Email shouldn't be changed