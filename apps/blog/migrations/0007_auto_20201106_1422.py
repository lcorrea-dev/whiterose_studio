# Generated by Django 3.1.2 on 2020-11-06 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='bio',
            field=models.TextField(blank=True, null=True),
        ),
    ]
