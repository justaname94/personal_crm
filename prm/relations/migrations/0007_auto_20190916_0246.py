# Generated by Django 2.2.5 on 2019-09-16 02:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('relations', '0006_auto_20190916_0109'),
    ]

    operations = [
        migrations.RenameField(
            model_name='activity',
            old_name='short_id',
            new_name='code',
        ),
        migrations.RenameField(
            model_name='activitylog',
            old_name='short_id',
            new_name='code',
        ),
        migrations.RenameField(
            model_name='contact',
            old_name='short_id',
            new_name='code',
        ),
    ]
