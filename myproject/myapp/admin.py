from django.contrib import admin
from .models import *

# class CustomerAdmin(admin.ModelAdmin):
#     list_display = ['customer_name', 'email', 'phone_number',
#                     'address', 'registration_date']
#     fields = ['customer_name', 'email', 'phone_number',
#               'address', 'registration_date']
#     readonly_fields = ['registration_date']
#     ordering = ['customer_name']
#     search_fields = ['customer_name']
#     search_help_text = ['Поиск по имени клиента']


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
    fields = ['name']
    search_fields = ['name']
    search_help_text = ['Поиск по наименованию категории']


class RecipeAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'created_at']
    list_filter = ['categories', 'created_at']
    readonly_fields = ['created_at']
    search_fields = ['name', 'ingredients', 'author']
    search_help_text = ['Поиск по наименованию, ингредиентам или автору блюда']

    fieldsets = (
        (None, {
            'fields': ('title', 'author')
        }),
        ('Recipe Details', {
            'fields': ('description', 'ingredients', 'steps', 'cooking_time')
        }),
        ('Date Information', {
            'fields': ('created_at',),
            'classes': ('collapse',)  # optional: hide this section by default
        })
    )


class RecipeCategoryAdmin(admin.ModelAdmin):
    list_display = ['recipe', 'category']


admin.site.register(Category, CategoryAdmin)
admin.site.register(Recipe, RecipeAdmin)
admin.site.register(RecipeCategory, RecipeCategoryAdmin)
