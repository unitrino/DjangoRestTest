# Generated by Django 2.1.1 on 2018-09-28 06:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TestCompanies', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='company',
            name='headquarter',
        ),
        migrations.AddField(
            model_name='office',
            name='is_headquarter',
            field=models.BooleanField(default=False),
        ),
    ]
