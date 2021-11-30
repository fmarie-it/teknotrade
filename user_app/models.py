from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

# class CustomUser(models.Model): gith
#     user_id = models.OneToOneField(User, on_delete=models.SET_NULL, null=True, blank=True)
#     is_admin = models.BooleanField(default=False)
#     # created_at = models.DateTimeField(default = timezone.now)
#     # updated_at = models.DateTimeField(auto_now=True)
    
#     class Meta:
#         db_table = "CustomUser"


class Category(models.Model):
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=100, null=False, blank=False)
    # product = models.ForeignKey(
    #     Product, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
    
    user = models.ForeignKey(
        User, on_delete=models.CASCADE,  related_name='get_all_users_product') #null=True, blank=True
    product_name = models.CharField(max_length=100, null=True, blank=True) #, null=False, blank=False
    image = models.ImageField(null=False, blank=False)
    description = models.TextField()
    status = models.CharField(max_length=100, null=True, blank=True, default="In Stock")
    date_created = models.DateTimeField(default = timezone.now)
    is_deleted = models.BooleanField(default=False)
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE,  related_name='get_category')

    def __str__(self):
        return self.product_name


class Address(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='get_user_address')
	street = models.CharField(max_length = 50)
	brgy = models.CharField(max_length = 50)
	zipcode = models.IntegerField()
	cityprovince = models.CharField(max_length = 50)
	
	class Meta:
		db_table = 'Address'

class Report(models.Model):
    report_type = models.CharField(max_length=100, null=True, blank=True)
    message = models.TextField()
    image = models.ImageField(null=True, blank=True)
    status = models.CharField(max_length=100, null=True, blank=True, default="pending")
    status_details = models.TextField(null=True, blank=True)
    date_created = models.DateTimeField(default = timezone.now)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='get_all_users_report')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='get_all_product_report')

    class Meta:
        db_table = "Report"
