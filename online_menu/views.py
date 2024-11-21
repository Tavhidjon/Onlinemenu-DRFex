from rest_framework import generics
from .models import *
from .serializers import *
from rest_framework.filters import *
from django_filters.rest_framework import DjangoFilterBackend

class CategoryCreateView(generics.CreateAPIView):
        queryset = Category.objects.all()
        serializer_class = Categoryserializer



class CategoryListView(generics.ListAPIView):
        queryset=Category.objects.all()
        serializer_class=Categoryserializer
        filter_backends=[DjangoFilterBackend,SearchFilter]
        filterset_fields=['name']
        search_fields = ['name']
class CategoryUpdate(generics.UpdateAPIView):
        queryset=Category.objects.all()
        serializer_class=Categoryserializer


class CategoryDestroy(generics.DestroyAPIView):
        queryset=Category.objects.all()
        serializer_class=Categoryserializer


class MealCreateView(generics.CreateAPIView):
        queryset = Meal.objects.all()
        serializer_class = Mealserializer


class MealListView(generics.ListAPIView):
        queryset=Meal.objects.all()
        serializer_class=Mealserializer
        filter_backends=[DjangoFilterBackend,SearchFilter]
        filterset_fields=['name']
        search_fields = ['name']

class MealUpdate(generics.UpdateAPIView):
        queryset=Meal.objects.all()
        serializer_class=Mealserializer


class MealDestroy(generics.DestroyAPIView):
        queryset=Meal.objects.all()
        serializer_class=Mealserializer

class TableCreateView(generics.CreateAPIView):
        queryset = Table.objects.all()
        serializer_class = Tableserializer


class TableListView(generics.ListAPIView):
        queryset=Table.objects.all()
        serializer_class=Tableserializer
        filter_backends=[DjangoFilterBackend,SearchFilter]
        filterset_fields=['table_number']
        search_fields = ['table_number']
class TableUpdate(generics.UpdateAPIView):
        queryset=Table.objects.all()
        serializer_class=Tableserializer


class TableDestroy(generics.DestroyAPIView):
        queryset=Table.objects.all()
        serializer_class=Tableserializer


class OrderCreateView(generics.CreateAPIView):
        queryset = Order.objects.all()
        serializer_class = Orderserializer


class OrderListView(generics.ListAPIView):
        queryset=Order.objects.all()
        serializer_class=Orderserializer
        filter_backends=[DjangoFilterBackend,OrderingFilter]
        filterset_fields=['quantity']
        search_fields = ['quantity']


class OrderUpdate(generics.UpdateAPIView):
        queryset=Order.objects.all()
        serializer_class=Orderserializer


class OrderDestroy(generics.DestroyAPIView):
        queryset=Order.objects.all()
        serializer_class=Orderserializer






class  BillCreateView(generics.CreateAPIView):
        queryset =  Bill.objects.all()
        serializer_class =  Billserializer
        ordering_fields = ['name']


class  BillListView(generics.ListAPIView):
        queryset= Bill.objects.all()
        serializer_class= Billserializer
        filter_backends=[DjangoFilterBackend,SearchFilter]
        filterset_fields=['Customer_name']
        search_fields = ['Customer_name']

class  BillUpdate(generics.UpdateAPIView):
        queryset= Bill.objects.all()
        serializer_class= Billserializer
        ordering_fields = ['name']


class  BillDestroy(generics.DestroyAPIView):
        queryset= Bill.objects.all()
        serializer_class= Billserializer
        ordering_fields = ['name']





