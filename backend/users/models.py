from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    age = models.PositiveIntegerField(null=True, blank=True)
    gender = models.CharField(max_length=10, choices=[('M', 'Male'), ('F', 'Female')])
    weight = models.DecimalField(max_digits=5, decimal_places=2)
    height = models.DecimalField(max_digits=5, decimal_places=2)
    dietary_preference = models.CharField(max_length=50, choices=[
        ('Vegan', 'Vegan'),
        ('Vegetarian', 'Vegetarian'),
        ('Omnivore', 'Omnivore')
    ])
    dietary_goal = models.CharField(max_length=50, choices=[
        ('Weight Loss', 'Weight Loss'),
        ('Muscle Gain', 'Muscle Gain'),
        ('Maintenance', 'Maintenance')
    ])

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return self.username
