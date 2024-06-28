# Generated by Django 5.0.6 on 2024-06-28 20:41

import datetime
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='Название категории')),
                ('image', models.ImageField(upload_to='recipes/', verbose_name='Изображение блюда')),
            ],
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128, verbose_name='Название блюда')),
                ('description', models.TextField(verbose_name='Описание рецепта')),
                ('ingredients', models.TextField(help_text='Перечислите все ингредиенты для приготовления блюда', verbose_name='Ингредиенты')),
                ('steps', models.TextField(verbose_name='Шаги приготовления')),
                ('cooking_time', models.DurationField(default=datetime.timedelta(seconds=3600), help_text='Время приготовления в формате чч:мм:сс', verbose_name='Время приготовления')),
                ('image', models.ImageField(upload_to='recipes/', verbose_name='Изображение блюда')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Автор')),
            ],
        ),
        migrations.CreateModel(
            name='RecipeCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.category', verbose_name='Категория')),
                ('recipe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.recipe', verbose_name='Рецепт')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
                'unique_together': {('recipe', 'category')},
            },
        ),
        migrations.AddField(
            model_name='recipe',
            name='categories',
            field=models.ManyToManyField(through='myapp.RecipeCategory', to='myapp.category', verbose_name='Категории'),
        ),
    ]