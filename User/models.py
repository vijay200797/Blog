from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager, User
    )

class MyAccountManager(BaseUserManager):
    def create_user(self, email, username, first_name, last_name, password=None):
        if not email:
            raise ValueError("Users must have an email address")
        if not username:
            raise ValueError("Users must have an user name")
        if not first_name:
            raise ValueError("Required First Name")

        user = self.model(
            email = self.normalize_email(email),
            username = username,
            first_name = first_name,
            last_name = last_name
            )
        
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, first_name, last_name, password=None):
        user = self.create_user(
            email = self.normalize_email(email),
            username = username,
            first_name = first_name,
            last_name = last_name,
            password = password
            )

        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user      




# # Create your models here.
# class User(AbstractBaseUser):
#     email                       = models.EmailField(verbose_name="email", max_length=60, unique=True)
#     username                    = models.CharField(max_length=50, unique=True)
#     date_joined                 = models.DateTimeField(verbose_name="date joined", auto_now_add=True)
#     last_login                  = models.DateTimeField(verbose_name="last login", auto_now_add=True)
#     is_admin                    = models.BooleanField(default=False)
#     is_active                   = models.BooleanField(default=True)
#     is_staff                    = models.BooleanField(default=False)
#     is_superuser                = models.BooleanField(default=False)
#     first_name                  = models.CharField(max_length=100)
#     last_name                   = models.CharField(max_length=100, default=None)

#     objects = MyAccountManager()

#     USERNAME_FIELD  =   "email"
#     REQUIRED_FIELDS  =   ['username', 'first_name', 'last_name']

#     def __str__(self):
#         return self.username

#     def has_perm(self, perm, obj=None):
#         return self.is_admin

#     def has_module_perms(self, app_label):
#         return True

AddressType =[
    ("H", "House"),
    ("O", "Office")
]

Status =[
    (1, "Active"),
    (0, "In-Active")
]
class Address(models.Model):
    userID = models.ForeignKey(User, on_delete=models.PROTECT)
    name = models.CharField(max_length=100)
    mobileNo = models.IntegerField()
    pincode = models.IntegerField()
    locality = models.CharField(max_length=150)
    address = models.TextField(max_length=250)
    citytown = models.CharField(max_length=150)
    state = models.CharField(max_length=100)
    landmark = models.CharField(max_length=150)
    alternatephone = models.IntegerField()
    addressType = models.CharField(choices=AddressType, max_length=1, default="H")
    status = models.IntegerField(choices=Status, default=1)

    def __str__(self):
        return str(self.id)