from django.db import models
from django.shortcuts import reverse


def generate_filename_jpg(instance, filename):
    filename = instance.slug + '.jpg'
    return "{0}/{1}".format(instance, filename)

# Create your models here.
class Video(models.Model):
    title = models.CharField(max_length=200, db_index=True, blank=True, verbose_name='Название')
    link = models.CharField(max_length=500, verbose_name='Ссылка на видео')
    course = models.ForeignKey('Course', related_name='video', on_delete=models.CASCADE, null=True, blank=True, verbose_name='Курс')
    img_file_link = models.ImageField(upload_to=generate_filename_jpg, null=True, blank=True, verbose_name='IMG')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Видео'
        verbose_name_plural = 'Видео'


class Course(models.Model):
    title = models.CharField(max_length=200, db_index=True, verbose_name='Название курса')
    slug = models.SlugField(max_length=200, verbose_name='Ссылка', unique=True)
    description = models.TextField(blank=True, db_index=True, verbose_name='Описание')
    desc_for_find = models.TextField(blank=True, db_index=True, verbose_name='Описание для поиска')
    keywords = models.CharField(max_length=200, blank=True, verbose_name='Кейвордс')
    category = models.ManyToManyField('Category', related_name='courses', verbose_name='Категория')
    img_file = models.ImageField(upload_to=generate_filename_jpg, null=True, blank=True, verbose_name='IMG')

    def get_absolute_url(self):
        cat_name = self.category.first().slug
        return reverse('course_detail_url', kwargs={'slug': self.slug, 'cat_name': cat_name})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Курсы'
        verbose_name = 'Курс'


class Category(models.Model):
    title = models.CharField(max_length=200, db_index=True, verbose_name='Название категории', blank=True)
    slug = models.SlugField(max_length=200, verbose_name='Ссылка')
    desc_for_find = models.TextField(blank=True, db_index=True, verbose_name='Описание для поиска')
    keywords = models.CharField(max_length=200, blank=True, verbose_name='Кейвордс')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('category_video_detail_url', kwargs={'slug': self.slug})

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
