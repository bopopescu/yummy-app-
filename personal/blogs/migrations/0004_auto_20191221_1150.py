# Generated by Django 3.0 on 2019-12-21 06:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0003_comments'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogs',
            name='edate',
        ),
        migrations.RemoveField(
            model_name='blogs',
            name='eimagepath',
        ),
        migrations.AlterField(
            model_name='comments',
            name='ecomments',
            field=models.CharField(max_length=200),
        ),
    ]