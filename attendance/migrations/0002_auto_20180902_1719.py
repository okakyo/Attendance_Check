# Generated by Django 2.0.7 on 2018-09-02 08:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='attendance_model',
            old_name='go_home_time',
            new_name='go_home',
        ),
    ]
