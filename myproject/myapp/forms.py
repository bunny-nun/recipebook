from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import *


class UserForm(UserCreationForm):
    email = forms.EmailField(
        required=True,
        label='Электронная почта',
        widget=forms.EmailInput(attrs={
            'class': 'form-control placeholder',
        })
    )
    first_name = forms.CharField(
        min_length=1,
        max_length=150,
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control placeholder',
        }),
        label='Имя'
    )
    last_name = forms.CharField(
        min_length=1,
        max_length=150,
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control placeholder',
        }),
        label='Фамилия'
    )

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'first_name',
            'last_name',
            'password1',
            'password2',
        ]
        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'form-control placeholder',
            }),
            'password1': forms.PasswordInput(attrs={
                'class': 'form-control placeholder',
                'placeholder': 'Пароль'
            }),
            'password2': forms.PasswordInput(attrs={
                'class': 'form-control placeholder',
                'placeholder': 'Подтвердите пароль'
            }),
        }


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = [
            'title',
            'categories',
            'description',
            'ingredients',
            'steps',
            'cooking_time',
            'image'
        ]

    title = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control placeholder',
            'placeholder': 'Наименование блюда'}),
        label=''
    )

    categories = forms.ModelMultipleChoiceField(
        queryset=Category.objects.all(),
        widget=forms.SelectMultiple(attrs={
            'class': 'form-control placeholder',
            'placeholder': 'Выберите категорию'}),
        label=''
    )

    description = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'form-control placeholder',
            'placeholder': 'Описание рецепта'}),
        label=''
    )

    ingredients = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'form-control placeholder',
            'placeholder': 'Ингредиенты'}),
        label=''
    )

    steps = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'form-control placeholder',
            'placeholder': 'Шаги приготовления'}),
        label=''
    )

    cooking_time = forms.DurationField(
        widget=forms.TextInput(attrs={
            'class': 'form-control placeholder',
            'placeholder': 'Время приготовления'}),
        label=''
    )

    image = forms.ImageField(
        widget=forms.FileInput(attrs={
            'class': 'form-control placeholder',
            'placeholder': 'Загрузите изображение'}),
        label=''
    )