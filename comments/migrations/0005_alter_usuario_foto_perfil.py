# Generated by Django 4.2.7 on 2024-01-14 21:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0004_alter_comment_options_alter_usuario_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='foto_perfil',
            field=models.ImageField(default='null', upload_to='fotos_perfil', verbose_name='Imagen de perfil'),
        ),
    ]