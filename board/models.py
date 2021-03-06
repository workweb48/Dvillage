from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from users.models import Profile






class Board(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description= models.CharField(max_length=50, unique=False)
    # board_image=models.ImageField(upload_to='images',default=False)
    active = models.BooleanField(default=True)
    def __str__(self):
        return self.name


class Topic(models.Model):
    title = models.CharField(max_length=70)
    description = models.CharField(max_length=500,default="لايوجد وصف")
    created_by = models.ForeignKey(User, related_name='topics',on_delete=models.CASCADE,default=True)
    board = models.ForeignKey(Board, related_name='topics',on_delete=models.CASCADE)
    created_dt = models.DateTimeField(default=timezone.now)
    # updated_at = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
    img_url =models.URLField(max_length=250)

    def get_absolute_url(self):
        return reverse('detail',kwargs={'id':self.id})

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('-created_dt',)







class Slide_Advertising(models.Model):
    name=models.CharField(max_length=100)
    # Slide_img = models.URLField(max_length=250)
    Slide_img_upload = models.ImageField(upload_to='images', default=True)


    def __str__(self):
        return self.name





class Up_img(models.Model):
    name = models.CharField(max_length=100)
    up_img_upload = models.ImageField(upload_to='images', default=True)
    url_img = models.URLField(max_length=250)
    active_img=models.BooleanField(default=False)

    def __str__(self):
        return self.name



class Topic_Advertising(models.Model):
    title = models.CharField(max_length=100)
    name = models.ForeignKey(User, related_name='Topic_Advertising',on_delete=models.CASCADE,default=True)
    description = models.CharField(max_length=100)
    AD_profile = models.ForeignKey(Profile, related_name='Topic_Advertising',on_delete=models.CASCADE,default=True)
    url_adv = models.URLField(max_length=250)

    def __str__(self):
        return self.title