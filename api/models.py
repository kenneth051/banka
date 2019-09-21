from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
import jwt
from datetime import datetime, timedelta
from app import settings
from api.requestMiddleware import RequestMiddleware
from api.constants import ACTIONS, TIME


class UserManager(BaseUserManager):
    def create_user(self, email, username, password, **extra_fields):
        """Create and return a `User` with an email, username and password."""
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.username = username
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
    email = models.EmailField(max_length=255, unique=True, blank=False)
    gender = models.CharField(max_length=255, blank=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    objects = UserManager()

    def __str__(self):
        """
        Returns a string representation of this `User`.
        This string is used when a `User` is printed in the console.
        """
        return self.email

    def token(self):
        credentials = {
            "id": self.id,
            "username": self.username,
            "is_staff": self.is_staff,
            "is_active": self.is_active,
            "is_superuser": self.is_superuser,
            "email": self.email,
            "exp": datetime.now() + timedelta(days=1)
        }
        return jwt.encode(credentials, settings.SECRET_KEY).decode("utf-8")


class BaseModel(models.Model):
    created_on = models.DateTimeField(auto_now=True)
    added_by = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        import pdb
        pdb.set_trace()
        request = RequestMiddleware.get_request()
        self.added_by = request.user
        super().save(*args, **kwargs)


class Clients(BaseModel):
    client_name = models.CharField(max_length=255, unique=True, blank=False)
    email = models.EmailField(max_length=255, unique=True, blank=False)
    occupation = models.CharField(max_length=255, blank=False)
    contact = models.IntegerField(default=0)
    address = models.CharField(max_length=255, blank=False)
    gender = models.CharField(max_length=255, blank=False)
    image = models.URLField(blank=True)

    def __str__(self):
        return self.client_name


class Account(BaseModel):
    client = models.OneToOneField("Clients", on_delete=models.CASCADE)
    balance = models.DecimalField(max_digits=15, decimal_places=2)

    def __str__(self):
        return self.client.client_name


class Loans(BaseModel):
    client_account = models.ForeignKey(Account, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=15, decimal_places=2)
    interest = models.DecimalField(max_digits=15, decimal_places=2)
    time_category = models.CharField(max_length=10,
                                     null=False,
                                     blank=False,
                                     choices=TIME,
                                     editable=False)
    time = models.DecimalField(max_digits=15, decimal_places=2)


class Transactions(BaseModel):
    client_account = models.ForeignKey(Account,
                                       null=True,
                                       on_delete=models.CASCADE)
    loan = models.ForeignKey(Loans, null=True, on_delete=models.CASCADE)
    action = models.CharField(max_length=10,
                              null=False,
                              blank=False,
                              choices=ACTIONS,
                              editable=False)
    amount = models.DecimalField(max_digits=15,
                                 null=False,
                                 blank=False,
                                 decimal_places=2)

    def __str__(self):
        return self.amount
