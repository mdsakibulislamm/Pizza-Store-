from django.db import models

# Create your models here.
class Product(models.Model):
    choice=(
        ('pizza','pizza'),
        ('pasta','pasta'),
        ('drinks','drinks'),
        ('deals','deals'),
        ('appetiser','appetiser'),
    )
  
    product_id=models.AutoField
    product_name=models.CharField(max_length=50)
    catagory=models.CharField(max_length=50,choices=choice)
    description=models.CharField(max_length=300)
    price=models.IntegerField(default=0)
    image=models.ImageField(upload_to="PizzaStore/images")

    def __str__(self):
        return self.product_name