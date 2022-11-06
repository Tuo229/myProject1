from django.db import models

from django.contrib.auth.models import AbstractUser, PermissionsMixin, BaseUserManager
from django.utils import timezone

class UserManager(BaseUserManager):

    use_in_migrations = True
    
    def _create_user(self, username, email, phone, password, **extra_fields):

        values = [username, email, phone]
        field_value_map = dict(zip(self.model.REQUIRED_FIELDS, values))
        for field_name, value in field_value_map.items():
            if not value:
                raise ValueError("Le champ {} doit etre rempli".format(field_name))
        
        email = self.normalize_email(email)
        user = self.model(
            username=username,
            email=email,
            phone=phone,
            **extra_fields
        )

        user.set_password(password)
        user.save(using=self._db)
        return user


    def create_user(self, username, email, phone, password, **extra_fields):

        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_active') is not True:
            raise ValueError("Une lié au droit d'accès c'est produite")

        return self._create_user(username, email, phone, password, **extra_fields)

    def create_superuser(self, username, email, phone, password=None, **extra_fields):

        extra_fields.setdefault('is_staff', True),
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError("Le champ is staff ne pas être faux pour l'admin")
        if extra_fields.get('is_superuser') is not True:
            raise ValueError("Le champ is superuser ne pas être faux pour l'admin")
        if extra_fields.get('is_active') is not True:
            raise ValueError("Le champ is active ne pas être faux pour l'admin")

        return self._create_user(username, email, phone, password, **extra_fields)
class User(AbstractUser, PermissionsMixin):

    username       = models.CharField('Nom utilisateur', max_length=50, unique=True)
    first_name     = models.CharField('Nom', max_length=50, null=True)
    first_name     = models.CharField('Prénom', max_length=50, null=True)
    email          =  models.EmailField(max_length=254, unique=True)
    phone          = models.CharField('Contact', max_length=30, unique=True)
    news           = models.BooleanField("Je souhaite m'abonner à la newslater")
    condition      = models.BooleanField("Conditions d'utilisation")
    ag_admin       = models.BooleanField("Administrateur agence", default=False)
    is_superuser   = models.BooleanField(default=False)
    
    objects = UserManager()

    USERNAME_FIELD  = 'email'
    REQUIRED_FIELDS = ['username', 'phone']

    def __str__(self):

        return self.username

    def save(self, *args, **kwargs):

        self.passord = self.set_password(self.password)
        super(User, self).save(*args, **kwargs)
