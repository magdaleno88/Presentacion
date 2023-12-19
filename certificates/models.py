from django.db import models

# Create your models here.
class Company(models.Model):
    name = models.CharField(max_length=100, verbose_name='Nombre')
    description = models.CharField(max_length=255, verbose_name='Descripcion')
    badge = models.CharField(max_length=100, null=True, verbose_name="insignia")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Creado el")

    class Meta:
        verbose_name = 'Empresa'
        verbose_name_plural = 'Empresas'

    def __str__(self):
        return self.name
    
class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Nombre')
    description = models.CharField(max_length=255, verbose_name='Descripcion')
    badge = models.CharField(max_length=100, null=True, verbose_name="insignia")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Creado el")

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'

    def __str__(self):
        return self.name

class Certificate(models.Model):
    title = models.CharField(max_length=150, verbose_name='Titulo')
    content = models.CharField(max_length=255, verbose_name='Contenido')
    image = models.ImageField(default='null', verbose_name='Imagen', upload_to="certificates")
    public = models.BooleanField(verbose_name='¿Publicado?')
    companies = models.ManyToManyField(Company, verbose_name='Empresas', blank=True)
    categories = models.ManyToManyField(Category, verbose_name='Categorias', blank=True)
    obtained_at = models.DateField(verbose_name="Obtenido el", default="Fecha")

    class Meta:
        verbose_name = 'Certificado'
        verbose_name_plural = 'Certificados'
        ordering = ['-obtained_at']

    def __str__(self):
        return self.title