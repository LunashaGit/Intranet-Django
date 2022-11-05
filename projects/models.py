from django.core.validators import validate_image_file_extension
from django.db import models
from base.models import BaseModel

class Category(BaseModel):
    category_name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, null=True,  blank=True)
    category_description = models.TextField()
    category_image = models.ImageField(upload_to='category_images', blank=True, null=True, validators=[validate_image_file_extension])

    def __str__(self):
        return self.category_name

class Product(BaseModel):
    name = models.CharField(max_length=255)
    description = models.TextField()
    slug = models.SlugField(max_length=255, unique=True, null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="products")
    product_description = models.TextField()
    product_image = models.ImageField(upload_to="products_images", blank=True, null=True, validators=[validate_image_file_extension])

    def __str__(self):
        return self.name
