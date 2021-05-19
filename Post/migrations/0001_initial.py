# Generated by Django 3.1.7 on 2021-04-29 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_title', models.CharField(max_length=100)),
                ('post_content', models.CharField(max_length=200)),
                ('post_type', models.IntegerField(choices=[('1', 'Link'), ('2', 'Video'), ('3', 'Article')], max_length=1)),
                ('post_datetime', models.DateTimeField(auto_now_add=True)),
                ('post_status', models.IntegerField(choices=[('1', 'Active'), ('0', 'InActive')], max_length=1)),
                ('post_additionalContext', models.CharField(max_length=200)),
            ],
        ),
    ]
