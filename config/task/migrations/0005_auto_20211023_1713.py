# Generated by Django 2.2.24 on 2021-10-23 11:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0004_auto_20211023_1710'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='owner',
            new_name='user',
        ),
        migrations.RenameField(
            model_name='project',
            old_name='owner',
            new_name='manager',
        ),
        migrations.RenameField(
            model_name='reminder',
            old_name='owner',
            new_name='user',
        ),
        migrations.RenameField(
            model_name='task',
            old_name='owner',
            new_name='user',
        ),
    ]
