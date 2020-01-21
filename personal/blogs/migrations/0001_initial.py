# Generated by Django 3.0 on 2019-12-14 04:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ename', models.CharField(max_length=100)),
                ('eemail', models.EmailField(max_length=254)),
                ('epassword', models.CharField(max_length=20)),
                ('econtact', models.CharField(max_length=15)),
            ],
            options={
                'db_table': 'Admin',
            },
        ),
    ]