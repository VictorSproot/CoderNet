# Generated by Django 2.1.1 on 2018-10-16 19:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('video', '0002_auto_20181016_2240'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='category',
            field=models.ManyToManyField(related_name='courses', to='video.Category', verbose_name='Категория'),
        ),
        migrations.AlterField(
            model_name='video',
            name='course',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='video', to='video.Course', verbose_name='Курс'),
        ),
        migrations.AlterField(
            model_name='video',
            name='link',
            field=models.CharField(max_length=500, verbose_name='Ссылка на видео'),
        ),
    ]
