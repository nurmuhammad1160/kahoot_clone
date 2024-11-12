from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models





# # Create your models here.
class MyUserManager(BaseUserManager):
	def create_user(self, username, password=None, **extra_fields):
		"""
		Creates and saves a User with the given email, date of
		birth and password.
		"""

		user = self.model(username=username, **extra_fields)

		user.set_password(password)
		user.is_active = True
		user.save()
		return user

	def create_superuser(self, username, password, **extra_fields):

		extra_fields.setdefault('is_staff', True)
		extra_fields.setdefault('is_active', True)
		extra_fields.setdefault('is_superuser', True)

		if extra_fields.get('is_staff') is not True:
			raise ValueError('Superuser must have is_staff=True.')
		if extra_fields.get('is_superuser') is not True:
			raise ValueError('Superuser must have is_superuser=True.')
		return self.create_user(username, password, **extra_fields)

class Organization(models.Model):
	name = models.CharField(max_length=100)


class User(AbstractBaseUser, PermissionsMixin):
	USER_TYPE = (
		('student', 'Talaba'),
		('teacher', "O'qituvchi"),
		('personal', "Shahsiy"),
	)
	first_name = models.CharField(verbose_name='Name', max_length=255, blank=True)
	last_name = models.CharField(verbose_name='Surname', max_length=255, blank=True)
	email = models.EmailField(verbose_name='Email', unique=False, blank=True)
	username = models.CharField(verbose_name='username', max_length=255, unique=True)
	is_staff = models.BooleanField(verbose_name='Staff Status', default=False)
	is_active = models.BooleanField(verbose_name='Activity', default=True)
	is_admin = models.BooleanField(default=False)
	birthday = models.DateField(verbose_name="Date of birth", null=True, blank=True)
	# phone = models.CharField(verbose_name='Telefon raqami', max_length=255, null=True, blank=False)
	user_type = models.CharField(verbose_name='User Type', max_length=255, choices=USER_TYPE,
	                             default='student')
	folders = models.FilePathField(verbose_name="Folder", null=True, blank=True)
	image = models.ImageField(verbose_name="Avatar", null=True, blank=True)
	organization = models.ForeignKey(Organization, verbose_name="Organization", null=True, blank=True, on_delete=models.SET_NULL)

	USERNAME_FIELD = 'username'
	objects = MyUserManager()

	def __str__(self):
		return self.username

	def get_full_name(self):
		return f'{self.first_name} {self.last_name}'

	def get_short_name(self):
		return self.first_name

	class Meta:
		verbose_name = 'Foydalanuvchi'
		verbose_name_plural = 'Foydalanuvchilar'
