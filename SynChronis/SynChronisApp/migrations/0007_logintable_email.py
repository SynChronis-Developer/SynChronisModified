# Generated by Django 4.2.18 on 2025-02-10 06:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SynChronisApp', '0006_alter_logintable_password_passwordresettoken'),
    ]

    operations = [
        migrations.AddField(
            model_name='logintable',
            name='Email',
            field=models.EmailField(blank=True, max_length=254, null=True, unique=True),
        ),
    ]
