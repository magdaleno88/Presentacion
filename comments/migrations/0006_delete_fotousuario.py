# Generated by Django 4.2.7 on 2023-12-22 19:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0005_fotousuario_delete_fotoperfil'),
    ]

    operations = [
        migrations.DeleteModel(
            name='FotoUsuario',
        ),
    ]
