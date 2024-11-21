from django.db import models


class Category(models.Model):
    name=models.CharField(max_length=50)
    def __str__(self):
        return self.name




class Meal(models.Model):
    name=models.CharField(max_length=50)
    price=models.IntegerField()
    category_id=models.ForeignKey(Category, on_delete=models.CASCADE)
    image=models.FileField(upload_to=None, max_length=100)
    description=models.TextField()
    is_active=models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name 

KOLA=[
    ('Free' ,'Free'),
    ('FULL','Full')
    ]

class Table(models.Model):
    status=models.CharField(choices=KOLA, max_length=50)
    table_number=models.CharField( max_length=50)

    def __str__(self):
        return self.status


class Bill(models.Model):
    table_id=models.ForeignKey(Table, on_delete=models.CASCADE)
    Customer_name=models.CharField( max_length=50)
    Total_sum=models.DecimalField( max_digits=5, decimal_places=2)
    created_at=models.DateTimeField(auto_now_add=True)
    is_paid=models.BooleanField(default=False)

    def __str__(self):
        return self.Customer_name




class Order(models.Model):
    bill_id=models.ForeignKey( Bill,on_delete=models.CASCADE)
    meal_id=models.ForeignKey(Meal, on_delete=models.CASCADE)
    quantity=models.IntegerField()



    def __str__(self):
        return self.quantity
    



