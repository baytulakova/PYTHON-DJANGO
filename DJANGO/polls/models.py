from django.db import models

class Category(models.Model):
    Name=models.CharField(max_length=100)

    def __str__(self):
        return self.Name

class Product(models.Model):
    IdCategory=models.ForeignKey(Category,on_delete=models.CASCADE)
    Name=models.CharField(max_length=100)
    Producer=models.CharField(max_length=100)
    Price=models.IntegerField

    def __str__(self):
        return self.Name

class Client(models.Model):
    Login=models.CharField(max_length=50)
    Password=models.CharField(max_length=50)
    FirstName=models.CharField(max_length=100)
    LastName=models.CharField(max_length=100)
    email_address = models.EmailField(max_length=70, blank=True, null=True, unique=True)

    def __str__(self):
        return self.Login

class Sale(models.Model):
    IdClient=models.ForeignKey(Client,on_delete=models.CASCADE)
    IdProduct=models.ForeignKey(Product,on_delete=models.CASCADE)
    SaleDate=models.DateField("data of sale")
    BuyDate=models.DateField("data of purchase")

    def __str__(self):
        return self.IdProduct
