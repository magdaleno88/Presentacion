from django.db import models
from certificates.models import Company

# Create your models here.
class Experience(models.Model):
    title = models.CharField(max_length=150, verbose_name='Titulo')
    content = models.CharField(max_length=255, verbose_name='Contenido')
    image = models.ImageField(default='null', verbose_name='Imagen', upload_to="Experiencias")
    public = models.BooleanField(verbose_name='¿Publicado?')
    companies = models.ManyToManyField(Company, verbose_name='Empresas', blank=True)
    start_date = models.DateField(verbose_name="Fecha de inicio", default="Fecha inicio")
    end_date = models.DateField(verbose_name="Fecha de salida", default="Fecha final")

    class Meta:
        verbose_name = 'Experiencia laboral'
        verbose_name_plural = 'Experiencias laborales'

    def __str__(self):
        return self.title