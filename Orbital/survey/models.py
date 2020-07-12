from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
# Create your models here.

class GenderFilter(models.Model):
    gender_filter = models.CharField(max_length=10, blank=True)

    def __str__(self):
        return self.gender_filter

class SingaporeanFilter(models.Model):
    singaporean_filter = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.singaporean_filter

class FacultyFilter(models.Model):
    faculty_filter = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.faculty_filter

class YearFilter(models.Model):
    year_filter = models.CharField(max_length=10, blank=True)

    def __str__(self):
        return self.year_filter

class ResidentialFilter(models.Model):
    residential_filter = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.residential_filter


class UploadSurvey(models.Model):
    user = models.ForeignKey(to=User, null=True, on_delete=models.SET_NULL,blank=True)
    #creator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    uploadDate = models.DateField(default=timezone.now)
    surveytitle = models.CharField('Survey Title', max_length=100)
    surveylink = models.URLField('Survey Link', max_length=200)
    surveydescription = models.CharField('Survey Description',
        max_length=5000,
        help_text="Include your survey dscription here!")

    surveycategory_choices = [
    ('EDN','Education'),
    ('HTC','Healthcare'),
    ('LFS','Lifestyle'),
    ('NUS','NUS-Related'),
    ('OTH','Others')]
    surveycategory = models.CharField('Survey Category',choices=surveycategory_choices, max_length=100, default='OTH')
    gender_filter=models.ManyToManyField(GenderFilter,blank=True)
    singaporean_filter=models.ManyToManyField(SingaporeanFilter, blank=True)
    faculty_filter=models.ManyToManyField(FacultyFilter,blank=True)
    year_filter=models.ManyToManyField(YearFilter,blank=True)
    residential_filter=models.ManyToManyField(ResidentialFilter, blank=True)

    def __str__(self):
        return self.surveytitle

    def get_absolute_url(self):
        return reverse('survey:tracksurvey-detail', kwargs={'pk':self.pk})



class CompletedSurveys(models.Model):
    user = models.ForeignKey(to=User, null=True, on_delete=models.SET_NULL,blank=True)
    completedsurveys = models.ManyToManyField(UploadSurvey)


### FOR REWARDS PAGE

# class UserPoints(models.Model):
#     user = models.ForeignKey(to=User, null=True, on_delete=models.SET_NULL,blank=True)
#     points_amount = models.IntegerField(default=1)
#     date = models.DateTimeField(auto_now_add=True)

class Reward(models.Model):
    rewardtitle = models.CharField('Title', max_length=255)
    rewarddescription = models.CharField('Reward Description',max_length=5000)
    reward_pic = models.ImageField(upload_to='reward_pics', blank=True)
    requiredpoints = models.IntegerField(default=12)
    def __str__(self):
        return self.rewardtitle

class TotalPoints(models.Model):
    user = models.ForeignKey(to=User, null=True, on_delete=models.SET_NULL,blank=True)
    points = models.IntegerField(default=0)
    def attrs(self):
        for attr, value in self.__dict__.iteritems():
            yield attr, value


class RedeemedRewards(models.Model):
    user = models.ForeignKey(to=User, null=True, on_delete=models.SET_NULL,blank=True)
    redeemedrewards = models.ManyToManyField(Reward)

class UsedRewards(models.Model):
    user = models.ForeignKey(to=User, null=True, on_delete=models.SET_NULL,blank=True)
    usedrewards = models.ManyToManyField(Reward)


### FOR REPORT PAGE

class Report(models.Model):
    user = models.ForeignKey(to=User, null=True, on_delete=models.SET_NULL,blank=True)
    #creator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    postedDate = models.DateField(default=timezone.now)
    subject = models.CharField('Report Subject', max_length=200)
    details = models.CharField('Report Details',
        max_length=10000,
        help_text="Include your report details here!")

    def __str__(self):
        return self.subject
