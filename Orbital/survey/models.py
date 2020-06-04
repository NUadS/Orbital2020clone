from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.

class UploadSurvey(models.Model):
    user = models.ForeignKey(to=User, null=True, on_delete=models.SET_NULL,blank=True)
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

    def __str__(self):
        return self.surveytitle
