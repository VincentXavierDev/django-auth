#3.3
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

#Meta class use for overwrite model or some fields
class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm): 
        model = CustomUser

        # UserCreationForm.Meta.fields is a tuple with value same (username, password, email,...)
        # + ('age',) has mean add 'age' field into this tuple
        fields = ('username', 'email', 'age',) # new

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser # update user model by default is User without age field
        fields = ('username', 'email', 'age',) # new