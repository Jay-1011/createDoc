# Generated by Django 4.2.1 on 2023-05-13 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doc', '0006_rename_email_mymodel_email_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mymodel',
            name='email',
            field=models.EmailField(blank=True, max_length=50),
        ),
    ]
