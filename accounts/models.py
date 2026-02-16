from django.db import models
import uuid

# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager

# Create your models here.
class UseManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('role', 'admin')

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, password, **extra_fields)
    
class User(AbstractUser):
    USER_ROLES = [
        ('student', 'Student'),
        ('manager', 'Hostel Manager'),
        ('admin', 'Admin'),
    ]
    role = models.CharField(max_length=20, choices=USER_ROLES)
    username=None
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    profile_image = models.ImageField(upload_to='profiles/', blank=True, null=True)

    SCHOOLS = [
        ('GCTU', 'Ghana Communication Technology University'),
        ('UG', 'University of Ghana'),
        ('KNUST', 'Kwame Nkrumah University of Science and Technology'),
        ('UPSA ', 'University of Professional Studies Accra'),
    ]
    school = models.CharField(max_length=50, choices=SCHOOLS, blank=True, null=True)


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    
    objects = UseManager()


    def __str__(self):
        return f'{self.email} - {self.role}'


class Manager(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="manager_profile",
    )

    whatsapp = models.CharField(max_length=13, blank=True)
    address = models.CharField(max_length=13,blank=True, null=True)

    # Use the same profile image from User model so we don't duplicate
    # or allow manager-specific override:
    def __str__(self):
        return self.user.email


class PasswordReset(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    reset_id = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)
    created_when = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Password reset for {self.user.email} at {self.created_when}'
