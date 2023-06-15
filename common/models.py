from django.db import models

class Institute(models.Model):
    title = models.CharField(max_length=255, db_index=True, verbose_name='Институт')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Институт'
        verbose_name_plural = 'Институты'
        ordering = ['id']

class Department(models.Model):
    title = models.CharField(max_length=255, db_index=True, verbose_name='Кафедра')
    institute = models.ForeignKey('Institute', on_delete=models.PROTECT, verbose_name='Институт')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Кафедра'
        verbose_name_plural = 'Кафедры'
        ordering = ['id']