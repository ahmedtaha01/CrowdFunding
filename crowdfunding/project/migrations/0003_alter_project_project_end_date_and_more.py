# Generated by Django 4.1.1 on 2022-09-13 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0002_project_project_details_project_project_end_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='project_end_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='project_start_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
