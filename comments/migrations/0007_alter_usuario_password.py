# Generated by Django 4.2.7 on 2024-01-15 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0006_alter_usuario_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='password',
            field=models.CharField(max_length=128, verbose_name='password'),
        ),
    ]