# Generated by Django 4.2.1 on 2023-05-07 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doc', '0002_rename_field1_mymodel_italic_remove_mymodel_field2_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='mymodel',
            name='description',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
