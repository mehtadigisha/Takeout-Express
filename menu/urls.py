from django.urls import path
from . import views

urlpatterns = [
    path('',views.menu,name='menu'),
    path('<int:menu_id>',views.detail, name='detail'),
    path('<int:menu_id>/', views.add_to_cart, name='add_to_cart'),
    path('view_cart/', views.view_cart, name='view_cart'),
    path('delete_from_cart/<int:cart_item_id>/', views.delete_from_cart, name='delete_from_cart'),
    path('order/',views.order,name='order'),
]