# Generated by Django 4.2.7 on 2024-01-14 21:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0005_alter_usuario_foto_perfil'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='password',
            field=models.CharField(max_length=128),
        ),
    ]