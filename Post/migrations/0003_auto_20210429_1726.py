# Generated by Django 3.1.7 on 2021-04-29 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Post', '0002_auto_20210429_1719'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='post_status',
            field=models.IntegerField(choices=[(1, 'Active'), (0, 'InActive')]),
        ),
        migrations.AlterField(
            model_name='post',
            name='post_type',
            field=models.IntegerField(choices=[(1, 'Link'), (2, 'Video'), (3, 'Article')]),
        ),
    ]
