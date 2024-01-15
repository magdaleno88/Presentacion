# Generated by Django 4.2.7 on 2024-01-14 21:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0003_alter_usuario_foto_perfil'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['-created_at'], 'verbose_name': 'Comentario', 'verbose_name_plural': 'Comentarios'},
        ),
        migrations.AlterModelOptions(
            name='usuario',
            options={'verbose_name': 'Usuario', 'verbose_name_plural': 'Usuarios'},
        ),
        migrations.AlterField(
            model_name='usuario',
            name='foto_perfil',
            field=models.ImageField(default='', upload_to='fotos_perfil', verbose_name='Imagen de perfil'),
        ),
    ]