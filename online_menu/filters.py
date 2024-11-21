import django_filters
from .models import *

class CategoryFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')  

    class Meta:
        model = Category
        fields = ['name']

class MealFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')
    price_min = django_filters.NumberFilter(field_name='price', lookup_expr='gte')
    price_max = django_filters.NumberFilter(field_name='price', lookup_expr='lte')

    class Meta:
        model = Meal
        fields = ['name', 'price']

class TableFilter(django_filters.FilterSet):
    status = django_filters.CharFilter(lookup_expr='icontains')
    table_number = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Table
        fields = ['status', 'table_number']

class BillFilter(django_filters.FilterSet):
    customer_name = django_filters.CharFilter(lookup_expr='icontains')
    is_paid = django_filters.BooleanFilter()

    class Meta:
        model = Bill
        fields = ['customer_name', 'is_paid']

class OrderFilter(django_filters.FilterSet):
    quantity_min = django_filters.NumberFilter(field_name='quantity', lookup_expr='gte')
    quantity_max = django_filters.NumberFilter(field_name='quantity', lookup_expr='lte')

    class Meta:
        model = Order
        fields = ['quantity']
