from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin, UserManager
from django.contrib.auth.validators import UnicodeUsernameValidator
from datetime import datetime, timedelta, timezone
from django.contrib.auth.hashers import make_password
import jwt
from django.conf import settings

# Create your models here.

class ProdUserManager(UserManager):
    def _create_user(self,email, password, code, **extra_fields):
        """
        Create and save a user with the given username, email, and password.
        """
        if not code:
            raise ValueError('The given username must be set')
        email = self.normalize_email(email)
        # Lookup the real model class from the global app registry so this
        # manager method can be used in migrations. This is fine because
        # managers are by definition working on the real model.
        GlobalUserModel = apps.get_model(self.model._meta.app_label, self.model._meta.object_name)
        username = GlobalUserModel.normalize_username(username)
        user = self.model(code=code, email=email, **extra_fields)
        # user.password = make_password(password)
        user.password = password
        user.save(using=self._db)
        return user

    def create_user(self, code, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(code, email, password, **extra_fields)

    def create_superuser(self, username, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(username, email, password, **extra_fields)

class User(AbstractBaseUser, PermissionsMixin):

    """
    An abstract base class implementing a fully featured User model with
    admin-compliant permissions.

    Username and password are required. Other fields are optional.
    """
    # username_validator = UnicodeUsernameValidator()

    # username = models.CharField(
    #     _('username'),
    #     max_length=150,
    #     unique=True,
    #     help_text=('Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.'),
    #     # validators=[username_validator],
    #     error_messages={
    #         'unique':("A user with that username already exists."),
    #     },
    # )

    objects = ProdUserManager()

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'code'
    # REQUIRED_FIELDS = ['code']

    code = models.CharField(max_length=100, blank=False, unique=True)
    nom = models.CharField(max_length=20, blank=True, null=True)
    prenom = models.CharField(max_length=20, blank=True, null=True)
    adresse = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(max_length=30, blank=True, null=True)
 
    @property
    def token(self):
        token = jwt.encode({'username':self.code, 'email': self.code,'exp' :datetime.utcnow() + timedelta(days=7)},settings.SECRET_KEY, algorithm='HS256')
