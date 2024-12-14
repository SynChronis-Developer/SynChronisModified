# Generated by Django 4.2.16 on 2024-12-03 09:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('SynChronisApp', '0014_noticetable_leaveapplicationtable'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentNoticeTable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Notice_name', models.CharField(blank=True, max_length=50, null=True)),
                ('Notice', models.CharField(blank=True, max_length=50, null=True)),
                ('Date', models.DateField(blank=True, null=True)),
                ('Student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SynChronisApp.studenttable')),
            ],
        ),
        migrations.CreateModel(
            name='TeacherNoticeTable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Notice_name', models.CharField(blank=True, max_length=50, null=True)),
                ('Notice', models.CharField(blank=True, max_length=50, null=True)),
                ('Date', models.DateField(blank=True, null=True)),
                ('Teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SynChronisApp.teachertable')),
            ],
        ),
        migrations.DeleteModel(
            name='NoticeTable',
        ),
    ]
