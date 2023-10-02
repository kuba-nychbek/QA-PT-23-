from django.db import models

class Body(models.Model):
    avatar = models.ImageField()
    name = models.CharField(max_length=100, null=False, verbose_name='name')
    

class Mentor(models.Model):
    name = models.CharField(max_length=200, null=False, verbose_name='name')
    describtion = models.CharField(max_length=100, null=False, verbose_name='describtion', default='text field')
    image = models.ImageField(default=True)

    def __str__(self)->str:
        return self.name
    
class Statistic(models.Model):
    participant = models.IntegerField()
    

class Sponsor(models.Model):
    title = models.CharField(max_length=50, null=False, verbose_name='title')
    image = models.ImageField()
    second_image = models.ImageField(default='important one')