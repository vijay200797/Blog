# Generated by Django 3.1.7 on 2021-04-25 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='last_name',
            field=models.CharField(max_length=100),
        ),
    ]
