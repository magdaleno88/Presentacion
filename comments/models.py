from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import User
from presentacion import settings

class UsuarioManager(BaseUserManager):
    def create_user(self,email,username,nombres,apellidos,password):
        if not email:
            raise ValueError('El usuario debe tener un correo electronico')
        
        usuario = self.model(
            username = username,
            email = self.normalize_email(email),
            nombres=nombres,
            apellidos = apellidos,
        )

        usuario.set_password(password)
        usuario.save(using=self._db)
        return usuario
    
    def create_superuser(self,username,email,nombres,apellidos,password):
        usuario = self.create_user(
            email,
            username = username,
            nombres=nombres,
            apellidos = apellidos,
            password=password
        )
        usuario.usuario_administrador = True
        usuario.save()
        return usuario

# Create your models here.
class Usuario(AbstractBaseUser):
    username = models.CharField('Nombre de usuario', unique = True, max_length=100)
    email = models.EmailField('Correo Electrónico', max_length=254, unique=True)
    nombres = models.CharField('Nombre', max_length=200, blank = True, null = True)
    apellidos = models.CharField('Apellidos', max_length=200, blank = True, null = True)
    empleo = models.CharField('¿A que te dedicas?', max_length=200, blank = False, null = False)
    foto_perfil = models.ImageField(default='null', verbose_name='Imagen de perfil',upload_to='fotos_perfil')
    usuario_activo = models.BooleanField(default = True)
    usuario_administrador = models.BooleanField(default = False)
    objects = UsuarioManager()

    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email','nombres','apellidos']

    def __str__(self):
        return f'{self.nombres}, {self.apellidos}'
    
    def has_perm(self,perm,obj = None):
        return True

    def has_module_perms(self,app_label):
        return True

    @property
    def is_staff(self):
        return self.usuario_administrador
    

class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name="Usuario", on_delete=models.CASCADE)
    content = models.CharField(max_length=255, verbose_name='Contenido')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Creado el")

    class Meta:
        verbose_name = 'Comentario'
        verbose_name_plural = 'Comentarios'
        ordering = ['-created_at']
       

    def __str__(self):
        return self.user.username