# Generated by Django 4.2.7 on 2024-01-13 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0002_alter_usuario_foto_perfil'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='foto_perfil',
            field=models.ImageField(default='null', upload_to='fotos_perfil', verbose_name='Imagen_perfil'),
        ),
    ]
