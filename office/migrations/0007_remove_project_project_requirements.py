# Generated by Django 4.0.4 on 2022-05-27 21:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('office', '0006_remove_project_project_requirements_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='project_requirements',
        ),
    ]
