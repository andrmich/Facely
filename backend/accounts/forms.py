from django.contrib.auth.forms import UserCreationForm
from .models import FbUser


class MyUserCreationForm(UserCreationForm):

     class Meta:
        model = FbUser
        fields = ('email',)
        field_classes = {'email address': 'email'}
