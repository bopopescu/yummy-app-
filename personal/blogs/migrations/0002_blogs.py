# Generated by Django 3.0 on 2019-12-14 04:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blogs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('etitle', models.CharField(max_length=100)),
                ('edescription', models.CharField(max_length=100)),
                ('edate', models.DateField()),
                ('eimagepath', models.CharField(max_length=15)),
            ],
            options={
                'db_table': 'Blogs',
            },
        ),
    ]
