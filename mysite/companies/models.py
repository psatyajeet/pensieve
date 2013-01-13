from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    android_users = models.IntegerField()
    def __unicode__(self):
        return self.name
