from django.db import models


class Task(models.Model):
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True, null=False, blank=False, verbose_name='Created at', help_text='Время создания')
    deadline = models.DateTimeField(auto_now=False, auto_now_add=False, null=True, blank=False, verbose_name='Deadline', help_text='Дедлайн')
    title = models.CharField(max_length=127, null=False, blank=False, verbose_name='Title', help_text='Заголовок')
    desc = models.TextField(null=True, blank=False, verbose_name='Description', help_text='Описание')

    def __str__(self):
        return self.title
