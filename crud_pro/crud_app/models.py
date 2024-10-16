from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class User(BaseUserManager):
    def create_user(self,email,password):
        if not email:
            raise ValueError("User must have an email")
        user = self.model(
            email = self.normalize_email(email),
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self,email,password):
        user = self.create_user(
            email,
            password=password
        )
        user.is_admin = True
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user
    
class NewUser(AbstractBaseUser):
    email = models.EmailField(verbose_name='email',max_length=100,unique=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    objects = User()
    USERNAME_FIELD = 'email'
    def __str__(self):
        return self.email
    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True
    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin

class Task(models.Model):
    STATUS = [
        ('pending','Pending'),
        ('in-progress','In Progress'),
        ('completed','Completed')
    ]
    Priority = [
        ('low','Low'),
        ('medium','Medium'),
        ('high','High')
    ]
    title = models.CharField(max_length=200)
    description = models.TextField(null=True,blank=True)
    status = models.CharField(max_length=15,choices=STATUS,default='pending')
    priority = models.CharField(max_length=20,choices=Priority,default='medium')
    due_date = models.DateField()

    def __str__(self):
        return self.title
# Create your models here.
