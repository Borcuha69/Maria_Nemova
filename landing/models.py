from django.db import models


class Section2(models.Model):
    name = models.CharField(max_length=128, verbose_name="Название")
    image = models.ImageField(upload_to='images/', verbose_name="Изображение")

    def __str__(self):
        return '%s' % self.name

    class Meta:
        verbose_name = "Section 2"
        verbose_name_plural = "Section 2"