from django.db import models
from django.contrib.auth.models import User
from datetime import timedelta


class Category(models.Model):
    name = models.CharField(max_length=128, blank=False,
                            verbose_name='Название категории')
    image = models.ImageField(upload_to='recipes/',
                              verbose_name='Изображение блюда')

    def __str__(self):
        return self.name


class Recipe(models.Model):
    title = models.CharField(max_length=128, verbose_name='Название блюда',
                             blank=False)
    categories = models.ManyToManyField(Category, through='RecipeCategory',
                                        verbose_name='Категории')
    description = models.TextField(verbose_name='Описание рецепта',
                                   blank=False)
    ingredients = models.TextField(verbose_name='Ингредиенты',
                                   help_text='Перечислите все ингредиенты '
                                             'для приготовления блюда',
                                   blank=False)
    steps = models.TextField(blank=False, verbose_name='Шаги приготовления')
    cooking_time = models.DurationField(verbose_name='Время приготовления',
                                        help_text='Время приготовления '
                                                  'в формате чч:мм:сс',
                                        default=timedelta(hours=1))
    image = models.ImageField(upload_to='recipes/',
                              verbose_name='Изображение блюда')
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               verbose_name='Автор', blank=False)
    created_at = models.DateTimeField(auto_now_add=True,
                                      verbose_name='Дата создания')

    def __str__(self):
        return self.title


class RecipeCategory(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE,
                               verbose_name='Рецепт')
    category = models.ForeignKey(Category, on_delete=models.CASCADE,
                                 verbose_name='Категория')

    class Meta:
        unique_together = ('recipe', 'category')
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'