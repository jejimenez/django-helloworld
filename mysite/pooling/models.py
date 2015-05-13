from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Seeker(models.Model):
    user = models.ForeignKey(User, verbose_name='Usuario Seeker', related_name='Usuario_Seeker')
    start_lat = models.DecimalField(max_digits=19, decimal_places=10,blank=True,null=True)
    start_lng = models.DecimalField(max_digits=19, decimal_places=10,blank=True,null=True)
    end_lat = models.DecimalField(max_digits=19, decimal_places=10,blank=True,null=True)
    end_lnt = models.DecimalField(max_digits=19, decimal_places=10,blank=True,null=True)
    schedule = models.CharField('schedule', max_length=7)
    description = models.TextField('description', blank=True)

class Driver(models.Model):
    user = models.ForeignKey(User, verbose_name='Usuario_Driver', related_name='Usuario_Driver')
    json_way = models.TextField('json_way', blank=False)
    schedule = models.CharField('schedule', max_length=7)
    description = models.TextField('description', blank=True,null=True)
    rout_sumary = models.TextField('rout_sumary', blank=True,null=True)
    rout_duration = models.CharField('rout_duration', max_length=50,null=True)
    rout_distance = models.CharField('rout_duration', max_length=50,null=True)
    rout_start_lat = models.DecimalField(max_digits=19, decimal_places=10,blank=True,null=True)
    rout_start_lng = models.DecimalField(max_digits=19, decimal_places=10,blank=True,null=True)
    rout_end_lat = models.DecimalField(max_digits=19, decimal_places=10,blank=True,null=True)
    rout_end_lng = models.DecimalField(max_digits=19, decimal_places=10,blank=True,null=True)
    rout_start_address = models.TextField('rout_start_address', blank=True,null=True)
    rout_end_address = models.TextField('rout_end_address', blank=True,null=True)
    rout_overviewpolilyne = models.TextField('rout_overviewpolilyne',blank=True,null=True)
    rout_bound_sw_lat = models.DecimalField(max_digits=19, decimal_places=10,blank=True,null=True)
    rout_bound_sw_lng = models.DecimalField(max_digits=19, decimal_places=10,blank=True,null=True)
    rout_bound_ne_lat = models.DecimalField(max_digits=19, decimal_places=10,blank=True,null=True)
    rout_bound_ne_lng = models.DecimalField(max_digits=19, decimal_places=10,blank=True,null=True)

class Weight(models.Model):
    seeker = models.ForeignKey(Seeker, verbose_name='seeker', related_name='weight_seeker')
    driver = models.ForeignKey(Driver, verbose_name='driver', related_name='weight_driver')
    weight = models.IntegerField()
    start_distance = models.FloatField()
    end_distance = models.FloatField()

class Leg(models.Model):
    driver = models.ForeignKey(Driver, verbose_name='driver', related_name='leg')

class Step(models.Model):
    leg = models.ForeignKey(Leg, verbose_name='leg', related_name='step')
    start_lat = models.DecimalField(max_digits=19, decimal_places=10)
    start_lng = models.DecimalField(max_digits=19, decimal_places=10)
    end_lat = models.DecimalField(max_digits=19, decimal_places=10)
    end_lng = models.DecimalField(max_digits=19, decimal_places=10)
    polyline = models.TextField('polyline',blank=True)
    duration = models.CharField('rout_duration', max_length=50,null=True)
    html_instruction = models.TextField('html_instruction', blank=True)
    distance = models.CharField('rout_duration', max_length=50,null=True)


    
