from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)
    parent_category = models.ForeignKey(
        "self",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="sub_category",
    )

    def __str__(self):
        return self.name


class Product(models.Model):
    product_id = models.BigIntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return self.title


class ProductAttribute(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    gender = models.CharField(max_length=10)
    base_color = models.CharField(max_length=20)
    season = models.CharField(max_length=10)
    year = models.IntegerField()
    usage = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.product.title}-{self.gender}-{self.base_color}"
