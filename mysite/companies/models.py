from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200, blank=True)
    phone_number = models.CharField(max_length=200, blank=True)
    
    total_funding=models.IntegerField('Total Funding')
    founding_date=models.DateField('Founding Date')
    benchmark_date=models.DateField('Benchmark Date', blank=True)
    alexa_rank_global=models.IntegerField('Alexa Rank', blank=True)
    employees=models.IntegerField('Num. Employees', blank=True)
    android_users = models.IntegerField('Num. Android Users', blank=True)
    android_user_rating=models.FloatField('Android User Rating', blank=True)
    twitter_followers=models.IntegerField('Num. Twitter Followers', blank=True)
    twitter_sentiment=models.IntegerField('Twitter Positive Sentiment', blank=True)
    twitter_tweets=models.IntegerField('Num. Tweets', blank=True)
    facebook_likes=models.IntegerField('Num. Facebook Likes', blank=True)
    facebook_sentiment=models.IntegerField('Facebook Positive Sentiment', blank=True)
    facebook_messages=models.IntegerField('Num. Facebook Messages', blank=True)
    
    def get_fields(self):
        # make a list of field/values.
        return [(field.verbose_name, field.value_to_string(self)) for field in self._meta.fields]
        
    #pub_date = models.DateTimeField('date published')
    def __unicode__(self):
        return self.name
        

