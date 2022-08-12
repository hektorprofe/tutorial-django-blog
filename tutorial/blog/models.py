from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=200, verbose_name="Título")
    content = models.TextField(verbose_name="Contenido")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Creado")
    modified = models.DateTimeField(auto_now=True, verbose_name="Modificado")

    # nuevo
    def __str__(self):
        return self.title

    # nuevo
    class Meta:
        verbose_name = "entrada"
        verbose_name_plural = "entradas"
