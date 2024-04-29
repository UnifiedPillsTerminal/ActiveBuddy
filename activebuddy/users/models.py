from django.db import models
from django.utils import timezone
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin


class CustomUserManager(BaseUserManager):
    def create_user(self, username, email=None, password=None, **extra_fields):
        if not username:
            raise ValueError('The username field must be set.')
        username = self.normalize_username(username)
        user = self.model(username=username, email=email, **extra_fields)
        if password is None:
            user.set_unusable_password()
        user.save()
        return user

    def create_superuser(self, username, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuse') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        
        return self.create_user(username, email, password, **extra_fields)

class MyUser(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(verbose_name='Логин', max_length=50, unique=True)
    email = models.EmailField(verbose_name='Электронная почта', unique=True)
    first_name = models.CharField(verbose_name='Имя', max_length=100, blank=True)
    last_name = models.CharField(verbose_name='Фамилия', max_length=150, blank=True)
    patronim = models.CharField(verbose_name='Отчество', max_length=150, blank=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)
#TODO: remove 'blank=True' for 'on_pause' when implementing progress pause algorithm
    on_pause = models.BooleanField(verbose_name='Прогресс приостановлен', default=False, blank=True)
    backup_email = models.EmailField(verbose_name='Резервная электронная почта', unique=True, blank=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'password']

    objects = CustomUserManager()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._meta.get_field('password').verbose_name = 'Пароль'

    def __str__(self):
        return self.username
