from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator,  MinValueValidator
from phone_field import PhoneField


class User(AbstractUser):
    type = models.IntegerField(choices=(
        (1, 'Admin'),
        (2, 'User'),
    ), default=2)
    phone = PhoneField(blank=True, help_text='phone number', null=True)
    
    def __str__(self):
        return self.username
    
    # class Meta(AbstractUser.Meta):
    #     swappable = 'AUTH_USER_MODEL'
    #     verbose_name = 'User'
    #     verbose_name_plural = 'Users'

model = models.Model


class Slider(model):
    background_image = models.ImageField(upload_to="Slider/")
    title1 = models.CharField(max_length=40)   
    title2 = models.CharField(max_length=40, blank=True, null=True) 
    text = models.CharField(max_length=80)


class News(model):
    image = models.ImageField(upload_to="News/")
    title = models.CharField(max_length=90)  
    text = models.CharField(max_length=150)  
    date = models.DateField(auto_now_add=True)


class Player(model):
    full_name = models.CharField(max_length=50)
    number = models.IntegerField(
        validators=[
            MaxValueValidator(100),
            MinValueValidator(0)
        ]
    )
    position = models.CharField(max_length=30)
    image = models.ImageField(upload_to="Player/")
    oyinlar = models.IntegerField(default=0)
    daqiqalar_oynagan = models.IntegerField(default=0)
    boshladi = models.IntegerField(default=0)
    sub_off = models.IntegerField(default=0)

class Info(model):
    title = models.CharField(max_length=30)
    text = models.TextField()
    image = models.ImageField(upload_to="Info/")

class ContactUs(model):
    instagram = models.URLField(max_length=777)
    telegram = models.URLField(max_length=777)
    facebook = models.URLField(max_length=777)
    youtube = models.URLField(max_length=777)
    twitter = models.URLField(max_length=777)
    phone = PhoneField(help_text='phone number')
    email = models.EmailField()
