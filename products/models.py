from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=25)


    def __str__(self):
        return self.name


class Product(models.Model):
    S = 'Size S'
    M = 'Size M'
    L = 'Size L'
    XL = 'Size XL'

    SIZE = [
        (S, 'Size S'),
        (M, 'Size M'),
        (L, 'Size L'),
        (XL, 'Size XL')

    ]

    title = models.CharField(max_length=25)
    description = models.TextField(null=True, blank=True)
    color = models.CharField(max_length=12)
    size = models.CharField(max_length=9,
                            choices=SIZE,
                            default=M
                            )
    category = models.ManyToManyField(Category) #, on_delete=models.SET_NULL, null=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-updated', '-created']

    def __str__(self):
        return self.title

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    body = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.body[0:50]


