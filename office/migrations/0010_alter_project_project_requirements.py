# Generated by Django 4.0.4 on 2022-05-28 04:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('office', '0009_alter_project_project_requirements'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='project_requirements',
            field=models.ManyToManyField(blank=True, to='office.skill'),
        ),
    ]
