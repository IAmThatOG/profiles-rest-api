from unicodedata import name
from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin,
    BaseUserManager,
)


# Create your models here.


class ApplicationUserManager(BaseUserManager):
    """Manger for user profiles

    Args:
        BaseUserManager (BaseUserManager): Base class that manages user profiles

    Returns:
        UserProfileManager: manager for user profiles
    """

    def create_user(
        self, email: str, first_name: str, last_name: str, password: str = None
    ):
        """Creates a user

        Args:
            email (str): Email
            firstname (str): Firstname
            lasename (str): Lastname
            password (str, optional): Password. Defaults to None.

        Raises:
            ValueError: Error raised if email is not passed

        Returns:
            ApplicationUser: Created user
        """

        if not email:
            raise ValueError("User must have an email address")
        email = self.normalize_email(email=email)
        user = self.model(email=email, first_name=first_name, last_name=last_name)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(
        self, email: str, first_name: str, last_name: str, password: str
    ):
        """Creates a superuser

        Args:
            email (str): Email
            firstname (str): Firstname
            lasename (str): Lastname
            password (str, optional): Password. Defaults to None.

        Returns:
            ApplicationUser: [description]
        """
        if not password:
            raise ValueError("super user must have password")
        user = self.create_user(email, first_name, last_name, password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user


class ApplicationUser(AbstractBaseUser, PermissionsMixin):
    """Database model for users in the system

    Args:
        AbstractBaseUser (AbstractBaseUser): Django base user model
        PermissionsMixin (PermissionsMixin): Django base permission model
    """

    email = models.EmailField(name="email", unique=True, max_length=128)
    email_confirmed = models.BooleanField(name="email_confirmed", default=False)
    phone_number = models.CharField(name="phone_number", max_length=50)
    phone_number_confirmed = models.BooleanField(
        name="phone_number_confirmed", default=False
    )
    first_name = models.CharField(name="first_name", max_length=32)
    last_name = models.CharField(name="last_name", max_length=32)
    is_active = models.BooleanField(name="is_active", default=True)
    is_staff = models.BooleanField(name="is_staff", default=False)

    objects = ApplicationUserManager()

    EMAIL_FIELD = "email"
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["firstname", "lastname"]

    class Meta:
        db_table = "application_user"

    @property
    def full_name(self):
        """Retreive user's fullname"""
        return f"{self.first_name} {self.last_name}"

    @property
    def short_name(self):
        """Retrieve user's shortname"""
        return self.first_name

    def __str__(self):
        """Returns string representation of the user

        Returns:
            string: email as string representation of the user
        """
        return self.email
