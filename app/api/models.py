from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager

class UserManager(BaseUserManager):

    def create_user(self, email, username, password, **extra_fields):
        """Create and return a `User` with an email, username and password."""
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.username=username
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password, **extra_fields):
        """
        Create and return a `User` with superuser powers.
        Superuser powers means that this use is an admin that can do anything
        they want.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        if password is None:
            raise TypeError('Superusers must have a password.')
        user = self.create_user(email, username, password, **extra_fields)
        return user

class User(AbstractUser):
    username = models.CharField(max_length=255, unique=True, blank=False)
    email=models.EmailField(max_length=255, unique=True,  blank=False)
    gender =models.CharField(max_length=255, blank=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    objects = UserManager()

    def __str__(self):
        """
        Returns a string representation of this `User`.
        This string is used when a `User` is printed in the console.
        """
        return self.email

# Create your models here.
