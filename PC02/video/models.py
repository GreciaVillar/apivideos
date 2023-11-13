from django.db import models

# Create your models here.

class TipoDeVideo(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()
    categoria = models.CharField(max_length=200)
    precio_alquiler = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='video/images')
    url = models.URLField(blank=True)

    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name_plural = "Tipo de Video"


class Alquiler(models.Model):
    video_alquilado = models.ForeignKey(TipoDeVideo, on_delete=models.CASCADE)
    cliente = models.ForeignKey('Cliente', on_delete=models.CASCADE)
    fecha_alquiler = models.DateTimeField(auto_now_add=True)
    fecha_devolucion = models.DateTimeField()

    def __str__(self):
        return self.video_alquilado.nombre
    
    class Meta:
        verbose_name_plural = "Alquiler"
    

class Cliente(models.Model):
    nombre = models.CharField(max_length=200)
    direccion = models.TextField()
    numero_telefono = models.CharField(max_length=9)
    correo_electronico= models.EmailField()

    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name_plural = "Cliente"

    