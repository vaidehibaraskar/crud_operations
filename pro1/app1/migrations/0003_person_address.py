# Generated by Django 5.0.6 on 2024-06-25 07:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_person_gender_person_profile_picture'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='address',
            field=models.TextField(default=None),
        ),
    ]
