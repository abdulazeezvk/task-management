# Generated by Django 5.0.4 on 2024-04-23 12:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='assigned_person',
            new_name='created_by',
        ),
    ]
