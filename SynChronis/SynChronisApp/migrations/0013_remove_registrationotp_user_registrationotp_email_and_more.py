# Generated by Django 4.2.18 on 2025-02-12 18:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('SynChronisApp', '0012_registrationotp'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='registrationotp',
            name='user',
        ),
        migrations.AddField(
            model_name='registrationotp',
            name='Email',
            field=models.EmailField(blank=True, max_length=254, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='registrationotp',
            name='Username',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='SynChronisApp.logintable'),
        ),
    ]
