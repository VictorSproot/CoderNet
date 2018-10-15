# Generated by Django 2.1.2 on 2018-10-15 00:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=200)),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('desc_for_find_cat', models.TextField(blank=True, db_index=True, verbose_name='Описание для поиска')),
                ('keywords_cat', models.CharField(blank=True, max_length=200, verbose_name='Кейвордс')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course', models.CharField(db_index=True, max_length=200, verbose_name='Название курса')),
                ('link_course', models.SlugField(max_length=200, unique=True, verbose_name='Ссылка на курс')),
                ('desc_for_find_watch', models.TextField(blank=True, db_index=True, verbose_name='Описание для поиска')),
                ('keywords_watch', models.CharField(blank=True, max_length=200, verbose_name='Кейвордс')),
                ('link_watch', models.ManyToManyField(related_name='video', to='watch.Category', verbose_name='Ссылка на видео')),
            ],
            options={
                'verbose_name': 'Видео',
            },
        ),
    ]
