# Generated by Django 4.2.1 on 2023-05-07 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doc', '0003_mymodel_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='mymodel',
            name='signature',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='mymodel',
            name='underlinetxt',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
