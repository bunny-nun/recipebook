from django.urls import path
from . import views

handler404 = views.page_not_found

urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', views.signup, name='signup'),
    path('signup/', views.signup, name='signup'),
    path('signup_success/', views.signup_success, name='signup_success'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('add/', views.add_recipe, name='add'),
    path('recipes/', views.show_all_recipes, name='recipes'),
    path('recipe/<int:recipe_id>/', views.recipe_detail, name='recipe_detail'),
    path('myrecipes/', views.my_recipes, name='my_recipes'),
    path('edit/<int:recipe_id>/', views.edit_recipe, name='edit_recipe'),
]