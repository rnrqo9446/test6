
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username", "password1", "password2")

    def save(self, commit=True):
        user = super(CreateUserForm, self).save(commit=False)
        # user.nickname = self.cleaned_data["nickname"]
        # user.email = self.cleaned_data["email"]

        if commit:
            user.save()
        return user