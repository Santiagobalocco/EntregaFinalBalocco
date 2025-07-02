from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)
    bio = models.TextField(max_length=500, blank=True)
    birth_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f'Perfil de {self.user.username}'

    def get_absolute_url(self):
        return reverse('profile')

def get_profile(self):
    profile, created = Profile.objects.get_or_create(user=self)
    return profile

User.add_to_class('profile', property(get_profile))
