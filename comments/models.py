from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Reply(models.Model):
    
    content = models.CharField(max_length=255, verbose_name='Contenido')
    image = models.ImageField(default='null', verbose_name='Imagen', upload_to="certificates")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Creado el")
    user = models.ForeignKey(User, verbose_name="Usuario", on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Respuesta'
        verbose_name_plural = 'Respuestas'
       

    def __str__(self):
        return self.user.username


class Comment(models.Model):
    
    content = models.CharField(max_length=255, verbose_name='Contenido')
    image = models.ImageField(default='null', verbose_name='Imagen', upload_to="certificates")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Creado el")
    replys = models.ManyToManyField(Reply, verbose_name='Respuesta', blank=True)
    user = models.ForeignKey(User, verbose_name="Usuario", on_delete=models.CASCADE)
    

    class Meta:
        verbose_name = 'Comentario'
        verbose_name_plural = 'Comentarios'
       

    def __str__(self):
        return self.user.username