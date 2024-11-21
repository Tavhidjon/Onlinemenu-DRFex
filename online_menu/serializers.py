from rest_framework import serializers
from .models import *



class Categoryserializer(serializers.ModelSerializer):
    class Meta:
            model = Category
            fields='__all__'



class Mealserializer(serializers.ModelSerializer):
    class Meta:
            model = Meal
            fields='__all__'
            



class Tableserializer(serializers.ModelSerializer):
    class Meta:
            model = Table
            fields='__all__'






class Orderserializer(serializers.ModelSerializer):
    class Meta:
            model = Order
            fields='__all__'




class Billserializer(serializers.ModelSerializer):
    class Meta:
            model = Bill
            fields='__all__'

