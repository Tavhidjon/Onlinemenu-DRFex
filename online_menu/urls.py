from django.urls import path
from .views import *

urlpatterns = [
    path('', RunMigrationsView.as_view(), name='run-migrations'),
    path('categories/',CategoryListView.as_view(), name='category-list'),
    path('categories/create/',CategoryCreateView.as_view(), name='category-create'),
    path('categories/<int:pk>/update/',CategoryUpdate.as_view(), name='category-update'),
    path('categories/<int:pk>/delete/',CategoryDestroy.as_view(), name='category-delete'),
    
    path('meals/',MealListView.as_view(), name='meal-list'),
    path('meals/create/',MealCreateView.as_view(), name='meal-create'),
    path('meals/<int:pk>/update/',MealUpdate.as_view(), name='meal-update'),
    path('meals/<int:pk>/delete/',MealDestroy.as_view(), name='meal-delete'),
    
    path('tables/',TableListView.as_view(), name='table-list'),
    path('tables/create/',TableCreateView.as_view(), name='table-create'),
    path('tables/<int:pk>/update/',TableUpdate.as_view(), name='table-update'),
    path('tables/<int:pk>/delete/',TableDestroy.as_view(), name='table-delete'),
    
    path('bills/',BillListView.as_view(), name='bill-list'),
    path('bills/create/',BillCreateView.as_view(), name='bill-create'),
    path('bills/<int:pk>/update/',BillUpdate.as_view(), name='bill-update'),
    path('bills/<int:pk>/delete/',BillDestroy.as_view(), name='bill-delete'),
    
    path('orders/',OrderListView.as_view(), name='order-list'),
    path('orders/create/',OrderCreateView.as_view(), name='order-create'),
    path('orders/<int:pk>/update/',OrderUpdate.as_view(), name='order-update'),
    path('orders/<int:pk>/delete/',OrderDestroy.as_view(), name='order-delete'),
]
