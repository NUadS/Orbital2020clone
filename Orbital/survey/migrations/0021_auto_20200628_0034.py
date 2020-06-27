# Generated by Django 3.0.6 on 2020-06-27 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0020_reward_usereward'),
    ]

    operations = [
        migrations.AddField(
            model_name='reward',
            name='requiredpoints',
            field=models.IntegerField(default=12),
        ),
        migrations.AlterField(
            model_name='reward',
            name='rewardtitle',
            field=models.CharField(max_length=255, verbose_name='Title'),
        ),
        migrations.DeleteModel(
            name='UseReward',
        ),
    ]