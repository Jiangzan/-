# Generated by Django 3.2.5 on 2022-04-23 12:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appUser', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='UserInfo',
            new_name='tb_user',
        ),
    ]
