# Generated by Django 3.0.1 on 2020-06-28 05:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0017_usedrewards'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usedrewards',
            old_name='redeemedrewards',
            new_name='usedrewards',
        ),
    ]
