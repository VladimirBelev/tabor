from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):
	user = models.ForeignKey( User, null = True )
	phone = models.CharField(max_length=20)
	dob = models.DateField(blank = True, null = True)


def user_post_save(sender, instance, **kwargs):
    ( profile, new ) = UserProfile.objects.get_or_create(user=instance)
 
models.signals.post_save.connect(user_post_save, sender=User)