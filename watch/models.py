from django.db import models
from django.shortcuts import reverse




class Video(models.Model):
    course = models.CharField(max_length=200, db_index=True, verbose_name='Название курса')
    link_course = models.SlugField(max_length=200, db_index=True, unique=True, verbose_name='Ссылка на курс')
    description_watch = models.TextField(blank=True, db_index=True, verbose_name='Описание')
    link_video = models.ForeignKey('Link', related_name='link_video', verbose_name='Ссылки на видео', on_delete=models.CASCADE,)
    link_watch = models.ManyToManyField('Category', related_name='video', verbose_name='Категория')
    desc_for_find_watch = models.TextField(blank=True, db_index=True, verbose_name='Описание для поиска')
    keywords_watch = models.CharField(max_length=200, blank=True, verbose_name='Кейвордс')

    def get_absolute_url(self):
        cat_name = self.video.first().slug
        return reverse('video_detail_url', kwargs={'slug': self.slug, 'cat_name': cat_name})

    class Meta:
        verbose_name = 'Видео'
        verbose_name_plural = 'Видео'
    def __str__(self):
        return self.course

class Link(models.Model):
    title = models.CharField(max_length=200, db_index=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Ссылка'
        verbose_name_plural = 'Ссылки'
        ordering = ['title']

class Category(models.Model):
    title = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True)
    desc_for_find_cat = models.TextField(blank=True, db_index=True, verbose_name='Описание для поиска')
    keywords_cat = models.CharField(max_length=200, blank=True, verbose_name='Кейвордс')
    def get_absolute_url(self):
        return reverse('lang_detail_url', kwargs={'slug': self.slug})

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['title']

    def __str__(self):
        return self.title