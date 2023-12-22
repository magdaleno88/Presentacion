from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Comment(models.Model):
    user = models.ForeignKey(User, verbose_name="Usuario", on_delete=models.CASCADE)
    content = models.CharField(max_length=255, verbose_name='Contenido')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Creado el")

    class Meta:
        verbose_name = 'Comentario'
        verbose_name_plural = 'Comentarios'
       

    def __str__(self):
        return self.user.username