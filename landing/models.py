from django.db import models


class Subscriber(models.Model):
    name = models.CharField(max_length=64, blank=True, null=True, default=None,verbose_name="Имя")
    phone_number = models.CharField(max_length=48, blank=True, null=True, default=None, verbose_name="Номер телефона")
    email = models.EmailField(max_length=128, blank=True, null=True, default=None, verbose_name="Email")
    description = models.TextField(blank=True, null=True, default=None, verbose_name="Вопрос")

    def __str__(self):
        return '%s' % self.name

    class Meta:
        verbose_name = "Subscriber"
        verbose_name_plural = "Subscribers"
