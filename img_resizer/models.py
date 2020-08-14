from django.db import models


class Image(models.Model):
    """Содержите в себе информацию об изначальном изображении, а так же
    об измененном"""

    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'

    name = models.CharField(max_length=256, verbose_name='Название файла',
                            blank=True)
    file = models.ImageField(verbose_name='Файл с изображением', blank=True)
    resized = models.ImageField(
        verbose_name='Изображение с измененным размером',
        blank=True
    )

    def save(self, *args, **kwargs):
        # При сохранении добавляем объекту имя
        if not self.name:
            self.name = self.file.name
        super(Image, self).save(*args, **kwargs)

    def __str__(self):
        return self.name
