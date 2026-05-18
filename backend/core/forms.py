from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User


class RegisterForm(UserCreationForm):
    ROLE_CHOICES = [
        ('donor', 'Donor'),
        ('ngo', 'NGO'),
        ('delivery', 'Delivery Person'),  # ✅ FIXED (value changed)
    ]

    email = forms.EmailField(required=True)
    role = forms.ChoiceField(choices=ROLE_CHOICES)

    class Meta:
        model = User
        fields = ['username', 'email', 'role', 'password1', 'password2']

    # 🔒 Email uniqueness validation
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Email already exists")
        return email

    # 🔒 Username uniqueness
    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("Username already taken")
        return username

    # 🎨 Styling
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs.update({
                'class': 'form-control',
                'placeholder': field.label
            })

        # 🔥 Optional: better dropdown UI label
        self.fields['role'].widget.attrs.update({
            'class': 'form-control'
        })