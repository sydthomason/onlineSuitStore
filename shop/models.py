from django.db import models
from django.urls import reverse


class Collection(models.Model):  # Changed from Category to Collection
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'collection'  # Changed from 'category' to 'collection'
        verbose_name_plural = 'collections'  # Changed from 'categories' to 'collections'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_list_by_collection', args=[self.slug])  # Updated URL name if necessary


class Product(models.Model):
    collection = models.ForeignKey(Collection, related_name='products', on_delete=models.CASCADE)  # Changed 'category' to 'collection'
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True)
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    quantity = models.IntegerField(default=2)

    class Meta:
        ordering = ('name',)
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_detail', args=[self.id, self.slug])


class Suit(models.Model):
    collection = models.ForeignKey(Collection, related_name='suits', on_delete=models.CASCADE)  # Changed 'category' to 'collection'
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, unique=True)
    size = models.CharField(max_length=50)
    color = models.CharField(max_length=50)
    rental_price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)
    image = models.ImageField(upload_to='suits/%Y/%m/%d', blank=True)
    description = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name',)
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:suit_detail', args=[self.slug])
