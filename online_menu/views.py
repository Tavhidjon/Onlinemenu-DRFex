from rest_framework import generics
from .models import *
from .serializers import *






class CategoryCreateView(generics.CreateAPIView):
        queryset = Category.objects.all()
        serializer_class = Categoryserializer
        ordering_fields = ['name']


class CategoryListView(generics.ListAPIView):
        queryset=Category.objects.all()
        serializer_class=Categoryserializer
        ordering_fields = ['name']

class CategoryUpdate(generics.UpdateAPIView):
        queryset=Category.objects.all()
        serializer_class=Categoryserializer
        ordering_fields = ['name']


class CategoryDestroy(generics.DestroyAPIView):
        queryset=Category.objects.all()
        serializer_class=Categoryserializer
        ordering_fields = ['name']


class MealCreateView(generics.CreateAPIView):
        queryset = Meal.objects.all()
        serializer_class = Mealserializer
        ordering_fields = ['name']


class MealListView(generics.ListAPIView):
        queryset=Meal.objects.all()
        serializer_class=Mealserializer
        ordering_fields = ['name']

class MealUpdate(generics.UpdateAPIView):
        queryset=Meal.objects.all()
        serializer_class=Mealserializer
        ordering_fields = ['name']


class MealDestroy(generics.DestroyAPIView):
        queryset=Meal.objects.all()
        serializer_class=Mealserializer
        ordering_fields = ['name']

class TableCreateView(generics.CreateAPIView):
        queryset = Table.objects.all()
        serializer_class = Tableserializer
        ordering_fields = ['name']


class TableListView(generics.ListAPIView):
        queryset=Table.objects.all()
        serializer_class=Tableserializer
        ordering_fields = ['name']

class TableUpdate(generics.UpdateAPIView):
        queryset=Table.objects.all()
        serializer_class=Tableserializer
        ordering_fields = ['name']


class TableDestroy(generics.DestroyAPIView):
        queryset=Table.objects.all()
        serializer_class=Tableserializer
        ordering_fields = ['name']


class OrderCreateView(generics.CreateAPIView):
        queryset = Order.objects.all()
        serializer_class = Orderserializer
        ordering_fields = ['name']


class OrderListView(generics.ListAPIView):
        queryset=Order.objects.all()
        serializer_class=Orderserializer
        ordering_fields = ['name']

class OrderUpdate(generics.UpdateAPIView):
        queryset=Order.objects.all()
        serializer_class=Orderserializer
        ordering_fields = ['name']


class OrderDestroy(generics.DestroyAPIView):
        queryset=Order.objects.all()
        serializer_class=Orderserializer
        ordering_fields = ['name']






class  BillCreateView(generics.CreateAPIView):
        queryset =  Bill.objects.all()
        serializer_class =  Billserializer
        ordering_fields = ['name']


class  BillListView(generics.ListAPIView):
        queryset= Bill.objects.all()
        serializer_class= Billserializer
        ordering_fields = ['name']

class  BillUpdate(generics.UpdateAPIView):
        queryset= Bill.objects.all()
        serializer_class= Billserializer
        ordering_fields = ['name']


class  BillDestroy(generics.DestroyAPIView):
        queryset= Bill.objects.all()
        serializer_class= Billserializer
        ordering_fields = ['name']





