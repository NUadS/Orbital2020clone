# Generated by Django 3.0.1 on 2020-06-14 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_auto_20200526_0128'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofileinfo',
            name='currentresidentialtype',
            field=models.CharField(choices=[('HDB', 'HDB'), ('Private Estate', 'PrivateEstate'), ('Condominium', 'Condominium'), ('Campus Accomodation', 'Campus Accomodation')], default='HDB', max_length=100, verbose_name='Current Residential Type'),
        ),
        migrations.AlterField(
            model_name='userprofileinfo',
            name='faculty',
            field=models.CharField(choices=[('Arts and Social Sciences', 'Arts and Social Sciences'), ('Business and Accountancy', 'Business and Accountancy'), ('Computing', 'Computing'), ('Dentistry', 'Dentistry'), ('Design and Environment', 'Design and Environment'), ('Engineering', 'Engineering'), ('Law', 'Law'), ('Medicine', 'Medicine'), ('Nursing', 'Nursing'), ('Music', 'Music'), ('Science', 'Science')], default='Arts and Social Sciences', max_length=50),
        ),
        migrations.AlterField(
            model_name='userprofileinfo',
            name='year_in_school',
            field=models.CharField(choices=[('Freshman', 'Freshman'), ('Sophomore', 'Sophomore'), ('Junior', 'Junior'), ('Senior', 'Senior'), ('Graduate', 'Graduate')], default='Freshman', max_length=10),
        ),
    ]
