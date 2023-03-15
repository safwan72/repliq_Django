from django.db import models
import uuid
# To Create A Custom User Model and admin panel
from django.contrib.auth.models import (
    BaseUserManager,
    AbstractBaseUser,
    PermissionsMixin,
)


# Create your models here.


class MyuserManager(
    BaseUserManager
):  # To Manage new users using this baseusermanaegr class
    """ A Custom User Manager to deal with Emails  as an unique Identifier """

    def _create_user(self, email, username, password, **extra_fields):
        """Creates and Saves an user with given email and password """

        if not email:
            raise ValueError("Email Must Be Set")

        email = self.normalize_email(email)
        user = self.model(email=email, username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_superuser(self, email, username, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("SuperUser is_staff must be True")

        if extra_fields.get("is_superuser") is not True:
            raise ValueError("SuperUser is_superuser must be True")

        return self._create_user(email, username, password, **extra_fields)


# custom user model created
class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True, null=False)
    username = models.CharField(max_length=264)
    is_staff = models.BooleanField(
        default=False,
        help_text="Determines Whether They Can Log in this Site or not",
    )
    is_active = models.BooleanField(
        default=True,
        help_text="Determines Whether their Account Status is Active or not",
    )
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]
    objects = MyuserManager()

    class Meta:
        verbose_name_plural = "User"
        db_table = "User"

    def __str__(self):
        return self.email


def upload_image(instance, filename):
    return "company/{instance.company_name.company.username}/{instance.company_name}logo.png".format(instance=instance)


# model for companies
class Company(models.Model):
    company_name=models.CharField(max_length=255)
    created_by = models.OneToOneField(User, related_name='company', on_delete=models.CASCADE)
    logo=models.ImageField(upload_to=upload_image,blank=True,default='/default-image-icon.png')    
    address=models.TextField(max_length=264,blank=True)
    city=models.CharField(max_length=40,blank=True)
    zipcode=models.CharField(max_length=10,blank=True)
    country=models.CharField(max_length=40,blank=True)
    phone=models.CharField(max_length=20,blank=True)
    company_id=models.CharField(default=uuid.uuid4,max_length=40,unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    

    class Meta:
        verbose_name_plural = "Company"
        db_table = "Company"

    def __str__(self):
        return self.company_name+" -----> "+self.created_by.username

