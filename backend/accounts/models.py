from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models


class UserAccountManager(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError('Email must be set!')
        user = self.model(email=email)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        user = self.create_user(email, password)
        user.is_staff = True
        user.save(using=self._db)
        return user

    def get_by_natural_key(self, email):
        return self.get(**{self.model.USERNAME_FIELD: email})


class FbUser(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(('first name'), max_length=30, blank=True)
    last_name = models.CharField(('last name'), max_length=150, blank=True)
    email = models.EmailField(('email address'), unique=True, blank=True)
    USERNAME_FIELD = 'email'
    objects = UserAccountManager()

    is_staff = models.BooleanField(('staff status'),
        default=False,
        help_text=('Designates whether the user can log into this admin site.'),
    )

    def natural_key(self):
        return self.email

