from django.db import models

# Create your models here.

class UploadSurvey(models.Model):
    surveytitle = models.CharField('Survey Title', max_length=100)
    surveylink = models.URLField('Survey Link', max_length=200)
    surveydescription = models.CharField('Survey Description',
        max_length=5000,
        help_text="Include your survey dscription here!")
    surveytype_choices = [('EDN','Education'),('HTC','Healthcare'),('OTH','Others')]
    surveytype = models.CharField('Survey Type',choices=surveytype_choices, max_length=100)

    def __str__(self):
        return self.surveytitle
