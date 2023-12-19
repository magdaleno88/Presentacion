# Generated by Django 4.2.7 on 2023-12-13 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('certificates', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='certificate',
            options={'ordering': ['-obtained_at'], 'verbose_name': 'Certificado', 'verbose_name_plural': 'Certificados'},
        ),
        migrations.AddField(
            model_name='category',
            name='badge',
            field=models.CharField(max_length=100, null=True, verbose_name='insignia'),
        ),
        migrations.AlterField(
            model_name='certificate',
            name='image',
            field=models.ImageField(default='null', upload_to='certificates', verbose_name='Imagen'),
        ),
    ]
