# Generated by Django 3.1.3 on 2020-11-30 18:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AppTwo', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='us_email',
            new_name='email',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='us_fname',
            new_name='first_name',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='us_lname',
            new_name='last_name',
        ),
    ]