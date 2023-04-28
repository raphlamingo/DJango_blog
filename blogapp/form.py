from .models import Users, Posts
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserForm(ModelForm):
    class Meta:
        model= Users
        fields=['first_name','last_name','email','about_me','profile_picture']

    def save(self, commit=True, user=None):
        instance = super(UserForm, self).save(commit=False)
        if user:
            instance.user = user
        if commit:
            instance.save()
        return instance

class PostForm(ModelForm):
    class Meta:
        model= Posts
        fields=["writer","title","content","upload_picture"]

