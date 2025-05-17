from django.urls import path
from . import views

app_name = 'store'

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('category/<slug:category_slug>/', views.product_list, name='product_list_by_category'),
    path('product/add/', views.product_add, name='product_add'),
    path('product/<slug:slug>/', views.product_detail, name='product_detail'),
    path('product/<slug:slug>/edit/', views.product_edit, name='product_edit'),
    path('product/<slug:slug>/soft-delete/', views.product_soft_delete, name='product_soft_delete'),
    path('product/<slug:slug>/hard-delete/', views.product_hard_delete, name='product_hard_delete'),
    path('categories/', views.category_list, name='category_list'),
    path('categories/add/', views.category_add, name='category_add'),
    path('categories/<slug:slug>/', views.category_detail, name='category_detail'),
    path('categories/<slug:slug>/edit/', views.category_edit, name='category_edit'),
    path('categories/<slug:slug>/soft-delete/', views.category_soft_delete, name='category_soft_delete'),
    path('categories/<slug:slug>/hard-delete/', views.category_hard_delete, name='category_hard_delete'),
]
