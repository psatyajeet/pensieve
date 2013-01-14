from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=200)
    
    total_funding=models.IntegerField()
    founding_date=models.DateField('founding date')
    benchmark_date=models.DateField('benchmark date')
    alexa_rank_global=models.IntegerField()
    employees=models.IntegerField()
    android_users = models.IntegerField()
    android_user_rating=models.FloatField()
    twitter_followers=models.IntegerField()
    twitter_sentiment=models.IntegerField()
    twitter_tweets=models.IntegerField()
    facebook_likes=models.IntegerField()
    facebook_sentiment=models.IntegerField()
    facebook_messages=models.IntegerField()
    
    pub_date = models.DateTimeField('date published')
    def __unicode__(self):
        return self.name
