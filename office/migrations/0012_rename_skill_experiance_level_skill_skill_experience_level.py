# Generated by Django 4.0.4 on 2022-05-28 04:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('office', '0011_alter_employee_current_projects_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='skill',
            old_name='skill_experiance_level',
            new_name='skill_experience_level',
        ),
    ]