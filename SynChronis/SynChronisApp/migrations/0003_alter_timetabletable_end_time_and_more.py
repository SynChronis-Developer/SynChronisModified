# Generated by Django 4.2.18 on 2025-02-08 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SynChronisApp', '0002_rename_course_studenttable_register_no_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timetabletable',
            name='end_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='timetabletable',
            name='start_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
