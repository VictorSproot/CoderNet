# Generated by Django 2.1.2 on 2018-10-05 17:54

import booklist.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=200, verbose_name='Название')),
                ('slug', models.SlugField(max_length=200, unique=True, verbose_name='Ссылка')),
                ('description', models.TextField(blank=True, db_index=True, verbose_name='Описание')),
                ('desc_for_find', models.TextField(blank=True, db_index=True, verbose_name='Описание для поиска')),
                ('keywords', models.CharField(blank=True, max_length=200, verbose_name='Кейвордс')),
                ('lang_category', models.IntegerField(choices=[(1, 'Русский'), (2, 'Английский')], db_index=True, default=1, verbose_name='Язык')),
                ('book_file', models.FileField(blank=True, null=True, upload_to=booklist.models.generate_filename, verbose_name='Файл PDF')),
                ('img_file', models.ImageField(blank=True, null=True, upload_to=booklist.models.generate_filename_jpg, verbose_name='IMG')),
            ],
            options={
                'verbose_name': 'Книга',
                'verbose_name_plural': 'Книги',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=200)),
                ('slug', models.SlugField(max_length=200, unique=True)),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.AddField(
            model_name='book',
            name='category',
            field=models.ManyToManyField(related_name='books', to='booklist.Category', verbose_name='Категория'),
        ),
    ]
